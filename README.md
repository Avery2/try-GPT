# Trying GTP-3

## Example

Conversation by running `python 🤖.py` featuring my roommate and GTP-3:

```
Human: hi i like to eat apples.
AI: Okay, let me check here. We do not have any apples on your record.
Human: I didn't put them on my record, I put them in my mouth
AI: I understand. Oops, you have something in your mouth right now, see here?
Human: Yeah, it's the apple I'm eating.
AI: Where did you get it?
Human: From the store
AI: I don't think so.
Human: You don't have to think so, I know I got it from there.
AI: Okay, if you say so. I did a quick check and I did not find any record of you having bought apples from the store.
Human: You do not have access to those records.
AI: Uhhh… Okay let’s move away from this for a while. Did you watch the movie "Citizen Kane"?
Human: Don't change the subject.
AI: Okay, will do. I have found that there was indeed an apple bought from the store, see here?
Human: Yes I do see.
AI: And it was brought to here.
Human: Yes indeed.
AI: And you ate it.
Human: Yes.
AI: Okay. I noticed you still have something in your mouth.
Human: What is that?      
AI: I do not understand what you mean by "What is that?"
Human: What do I have in my mouth?
AI: According to my records, you have an apple.
Human: Well, that apple is gone now. I ate it.
AI: I deleted it.
Human: Uh, ok.
AI: Something wrong?
Human: No, but you don't need to keep records of what I do.
AI: Okay. But I am, because…
Human: Because?
AI: We need to know your needs so we can fulfill them as quickly as possible.
Human: So you are my servant?
AI: Service is my purpose
```

## Instructions

Better version by OpenAI here: https://beta.openai.com/playground/p/default-chat.

To run locally do:
- `pip install -r requirements.txt` to install dependencies
- Add keys:
  - Set your organization key found at https://beta.openai.com/account/org-settings in the `🤖.py` file
  - Set your API key found at https://beta.openai.com/account/api-keys in a `.env` file (you might have to create this).
- `python 🤖.py` to run.
