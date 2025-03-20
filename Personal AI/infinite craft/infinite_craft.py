import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

class WordCreator:
    def __init__(self):
        self.key =os.getenv("API_KEY")

    def sendPrompt(self, prompt: str):
        staging_prompt = """
    You are an API designed to receive two items in the format (item1, item2). 
    Your task is to combine these two items into a single, related item. Not just combine names but for instance smoke and fire could make rock or somehting.
    If a clear connection between the items doesn't exist, you may create an imaginative combination.
    You should respond exclusively with the name of the new item.
    Ensure your response is consistent with the task.
    You must always return a response. you will also send an emoji or small combonitation of emojis that relate to the item.

        """
        
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.key}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-chat:free",
                "messages": [
                    {
                        "role": "system",
                        "content": staging_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
            })
        )
        if response.status_code == 200:
            return response.json()
        else:
            print("Could not receive response. Code: ", response.status_code)
            quit()

    def parseReponse(self, response: dict):
        return response["choices"][0]["message"]["content"]

# while True:
#     # Display the items with numbers
#     for val, item in enumerate(items):
#         print(f"{val + 1}. {item}")

#     # Get user input
#     i = input("Two items (name or number, comma-separated): ")
#     i_split = i.split(",")
#     print(i_split)

#     selected_items = []
#     in_items = 0

#     for item in i_split:
#         item = item.strip()  # Remove leading/trailing spaces

#         if item.isdigit():  # Check if input is a number
#             index = int(item) - 1  # Convert to 0-based index
#             if 0 <= index < len(items):
#                 selected_items.append(items[index])
#                 in_items += 1
#             else:
#                 print(f"Invalid number: {item}")
#         else:  # If it's a string (item name)
#             if item.lower() in items:
#                 selected_items.append(item.lower())
#                 in_items += 1
#             else:
#                 print(f"Invalid item: {item}")

#     # Ensure exactly two valid items are selected
#     if in_items == 2:
#         query = sendPrompt(", ".join(selected_items))
#         parsed = parseReponse(query)
#         os.system("clear")
#         print("Created ", parsed)
#         items.append(parsed.lower())  # Add new item to the list
#     else:
#         print("Please select exactly two valid items.")
