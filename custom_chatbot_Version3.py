import openai

# ==== Configuration ====
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key
MODEL = "gpt-3.5-turbo"  # Or use "gpt-4" if you have access

# ==== Personality/Customization ====
SYSTEM_PROMPT = (
    "You are a helpful, friendly assistant. "
    "Customize your behavior here! "
    "For example, you can act as a technical expert, a funny friend, etc."
)

# ==== Chatbot Logic ====
def get_response(user_message):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ]
    )
    return response.choices[0].message["content"]

# ==== Main Loop ====
if __name__ == "__main__":
    print("Custom Chatbot AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        bot_reply = get_response(user_input)
        print("Bot:", bot_reply)