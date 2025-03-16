import chromadb

chroma_client = chromadb.PersistentClient()
# chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")

if __name__ == "__main__":

    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")
    results = collection.query(
        query_texts=["A 28-year-old patient reports experiencing a severe, throbbing headache accompanied by sensitivity to light and sound, along with occasional nausea. The headache has persisted for several hours and is impacting daily activities."], # Chroma will embed this for you
        n_results=3 # how many results to return
    )

    print(results)
    print("____________________________")