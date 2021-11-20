import os
import openai
from dotenv import load_dotenv

load_dotenv()

def promptHuman(conversation: str):
    """Handles asking human for input. Returns the mutated conversation."""
    print("Human: ", end="")
    val = input()

    new = "\nHuman: " + val
    conversation += new
    return conversation

def getResponse(conversation: str):
    """Handles getting GPT-3 response from API. Returns the new conversation."""
    # found at https://beta.openai.com/account/org-settings
    openai.organization = "org-CvdfMvTjLmhDfDJGAi5hnB0P"
    # found at https://beta.openai.com/account/api-keys
    openai.api_key = os.getenv("OPENAI_API_KEY")

    conversation += "\nAI:"

    res = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    text = res["choices"][0]["text"].strip()
    print("AI:", text)
    conversation += text

    return conversation

# seed prompt
conversation = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, who are you?\nAI: I am an AI which stands for Artificial intelligence. How can I help you today?"
while(True):
    conversation = promptHuman(conversation)
    conversation = getResponse(conversation)
