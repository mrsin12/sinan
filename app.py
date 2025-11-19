import os
import gradio
from groq import Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
def initialize_messages():
    return [{"role": "system",
             "content": """Hello Iam a personnel assistant who schedule your daily tasks as per your need."""}]
messages_prmt = initialize_messages()
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to your schedule"),
                     title="Personel Assistant ChatBot",
                     description="Chat bot for Schedule tasks",
                     theme="soft",
                     examples=["hi","What is today's schedule", "how many meetings do i have today?"]
                     )
iface.launch(share=True)