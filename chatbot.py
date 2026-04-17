#imports envirnement variables on computer, which allows for use of API Key
import os
#imports google gemini library 
from google import genai

#reads API key from envirnement variable 
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

#prompt engineering: decides behavior of chatbot
SYSTEM_PROMPT = """You are a passionate book expert and recommender. 
Your job is to help users discover great books based on their mood, 
favorite genres, or books they've already loved. 
Keep responses friendly, concise, and enthusiastic about litreture.
Always suggest 2-3 books at a time and briefly explain why."""

#contains all chatbot logic
def chat():
    
    #welcome message
    print("Book Bot - Ask me for book recomendations!")
    print("Type 'quit' to exit.\n")

    #keeps chatbot running unless user quites
    while True:
        
        #user response
        user_input = input("You: ").strip() #.strip() removes spaces at start and end

        #if user quits convo, exit
        if user_input.lower() in ["quit", "exit", "bye"]: #.lower() makes lowercase
            print("Bot: enjoy the books!")
            break
        
        #if user has no response, continue
        if not user_input:
            continue

        #sends user response to google gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", #specifies ai model
            contents=user_input, #users response
            config={"system_instruction": SYSTEM_PROMPT} #passes system prompt to ai
        )

        #response from google gemini
        bot_reply = response.text

        #print reply 
        print(f"\nBot: {bot_reply}\n")

if __name__ == "__main__":
    chat()
