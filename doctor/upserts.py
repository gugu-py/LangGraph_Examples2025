import chromadb
import json

def process_jsonl(input_file, output_file):
    output_data = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for idx, line in enumerate(infile, start=1):
            # Load each JSON object from a line
            record = json.loads(line.strip())
            question = record.get("question", "")
            answer = record.get("answer", "")
            # Combine the question and answer into one string for the truth field
            truth = f"{question} {answer}"
            # Create a new record with the required fields
            new_record = {
                "id": idx,
                "truth": truth,
                "question": question,
                "answer": answer
            }
            output_data.append(new_record)
    
    # Write the new records to a JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=2)

def extract_documents_and_ids(processed_file):
    documents = []
    ids = []
    
    # Read the processed JSON file
    with open(processed_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        for record in data:
            # Append the truth field to documents
            documents.append(record.get("truth", ""))
            # Create id string in the format "idX" (e.g., "id1")
            ids.append(f"id{record.get('id', '')}")
            
    return documents, ids
chroma_client = chromadb.PersistentClient()
# chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")

if __name__ == "__main__":

    input_filename = "train.jsonl"
    output_filename = "output.json"
    process_jsonl(input_filename, output_filename)
    print(f"Processed {input_filename} and created {output_filename}")

    processed_filename = output_filename  # use your processed file path here
    documents, ids = extract_documents_and_ids(processed_filename)


    # switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time

    # switch `add` to `upsert` to avoid adding the same documents every time
    collection.upsert(
        documents=documents,
        ids=ids
    )

    