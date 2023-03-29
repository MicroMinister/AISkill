import json
import requests
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QTextEdit,
                             QLineEdit, QPushButton)

class ChatGPT(QWidget):

    def __init__(self):
        super().__init__()
        self.api_key = "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"
        self.url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
        self.gpt_prefix = "你是一个多语言的ChatGPT助手，根据提问的语言来回答问题。如果提问者要求使用特定语言，请遵循要求。用户："
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle("ChatGPT")
        self.setFixedSize(640, 480)

        # 创建控件
        self.chat_text = QTextEdit(self)
        self.chat_text.setReadOnly(True)
        self.chat_text.setStyleSheet("background-color: white;")
        self.user_entry = QLineEdit(self)
        self.user_entry.setStyleSheet("background-color: white;")
        self.send_button = QPushButton("发送", self)
        self.send_button.setShortcut("Return")

        # 创建网格布局并添加控件
        layout = QGridLayout()
        layout.addWidget(self.chat_text, 0, 0, 1, 2)
        layout.addWidget(self.user_entry, 1, 0)
        layout.addWidget(self.send_button, 1, 1)
        layout.setRowStretch(0, 1)
        layout.setColumnStretch(0, 1)
        self.setLayout(layout)

        # 信号连接槽
        self.send_button.clicked.connect(self.on_send_click)
        self.user_entry.returnPressed.connect(self.on_send_click)

    def send_message(self, prompt):
        data = {
            "prompt": f"{self.gpt_prefix}{prompt}",
            "max_tokens": 50,
            "temperature": 0.5
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(self.url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            response_text = response_data["choices"][0]["text"]
            return response_text.strip()
        else:
            print(f"Error: {response.status_code}")
            return None

    def on_send_click(self):
        user_input = self.user_entry.text()
        self.user_entry.setText("")
        self.chat_text.append(f"你：{user_input}")
        self.send_button.setEnabled(False)

        def process_response():
            response = self.send_message(user_input)
            if response:
                self.chat_text.append(f"ChatGPT：{response.strip()}")
            self.send_button.setEnabled(True)

        threading.Thread(target=process_response).start()

if __name__ == '__main__':
    app = QApplication([])
    chat_gpt = ChatGPT()
    chat_gpt.show()
    app.exec_()
