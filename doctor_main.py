from doctor import workflow, BotState

test_data  = BotState(
    message="I've been experiencing severe headache and fever for the past 48 hours."
    )

result = workflow.invoke(test_data)
print(result['documents'])
print("_________________")
print(result['answer'])
print("_________________")