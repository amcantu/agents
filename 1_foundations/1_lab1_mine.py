from dotenv import load_dotenv
import openai


load_dotenv(override=True)

# First create the messages:
user_input = "Who was Miguel Hidalgo y Costilla?"
messages = [
    {
        "role": "user", 
        "content": "Taking the user request, please respond using compact answer in plain text, no markdown, no code blocks, no emojis, no links, no images, no lists, no numbers, no quotes, no headings. Try to build the response in a json format for attributes you think may matter. User request: " + user_input
    }
]

# Then make the first call:
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

# Then read the business idea:
business_idea = response.choices[0].message.content
print(business_idea)
