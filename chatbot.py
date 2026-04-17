import os
from google import genai

#configure client with API Key
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

#chatbot focus
SYSTEM_PROMPT = """You are a passionate book expert and recommender. 
Your job is to help users discover great books based on their mood, 
favorite genres, or books they've already loved. 
Keep responses friendly, concise, and enthusiastic about litreture.
Always suggest 2-3 books at a time and briefly explain why."""

def chat():
    print("Book Bot - Ask me for book recomendations!")
    print("Type 'quit' to exit.\n")


    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: enjoy the books!")
            break
        
        if not user_input:
            continue

        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=user_input,
            config={"system_instruction": SYSTEM_PROMPT}
        )

        bot_reply = response.text

        print(f"\nBot: {bot_reply}\n")

if __name__ == "__main__":
    chat()
