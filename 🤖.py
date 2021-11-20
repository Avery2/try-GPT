import os
import openai
from dotenv import load_dotenv

load_dotenv()

# found at https://beta.openai.com/account/org-settings
openai.organization = "org-CvdfMvTjLmhDfDJGAi5hnB0P"
# found at https://beta.openai.com/account/api-keys
openai.api_key = os.getenv("OPENAI_API_KEY")
l = openai.Engine.list()

while(True):
    print("Human: ", end="")
    val = input()
    res = openai.Completion.create(
        engine="davinci",
        prompt=val
    )
    text = res["choices"][0]["text"]

    print("AI:", text)
