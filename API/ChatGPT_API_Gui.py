import requests
import json
import tkinter as tk
from tkinter import ttk
import threading

api_key = "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"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

def send_message(prompt):
    gpt_prefix = "你是一个多语言的 ChatGPT助手，根据提问的语言来回答问题。如果提问者要求使用特定语言，请遵循要求。用户："
    data = {
        "prompt": f"{gpt_prefix}{prompt}",
        "max_tokens": 50,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        response_text = response_data["choices"][0]["text"]
        return response_text.strip()
    else:
        print(f"Error: {response.status_code}")
        return None

def on_send_click():
    user_input = user_entry.get()
    user_entry.delete(0, 'end')
    chat_text.insert('end', f"你：{user_input}\n")
    send_button.config(state='disabled')

    def process_response():
        response = send_message(user_input)
        if response:
            chat_text.insert('end', f"{response.strip()}\n")
        send_button.config(state='normal')

    threading.Thread(target=process_response).start()

def on_return_press(event):
    on_send_click()

app = tk.Tk()
app.title("ChatGPT")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_text = tk.Text(frame, wrap='word', width=50, height=20, exportselection=True)
chat_text.grid(row=0, column=0, columnspan=2, padx=(0, 10), pady=(0, 10))
chat_text.config(selectbackground='blue', selectforeground='white')

user_entry = ttk.Entry(frame, width=40)
user_entry.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))
user_entry.bind('<Return>', on_return_press)

send_button = ttk.Button(frame, text="发送", command=on_send_click)
send_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

app.mainloop()
