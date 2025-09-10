from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load free, open-source model (change 'distilgpt2' to other available models if you like)
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply[len(user_input):].strip()  # Remove echo

print("Free Chatbot AI (type 'exit' to quit)")
while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit"]:
        break
    bot_reply = chat(user_message)
    print("Bot:", bot_reply)