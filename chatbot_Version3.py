from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "distilgpt2"  # You can change this to other Hugging Face models

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def chat(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply[len(user_input):].strip()

if __name__ == "__main__":
    print("Free Chatbot AI (type 'exit' to quit)")
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        bot_reply = chat(user_message)
        print("Bot:", bot_reply)