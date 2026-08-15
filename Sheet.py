import os
import requests
from datetime import datetime
import random
from html import unescape
from dotenv import load_dotenv

load_dotenv()

class SheetIt:

    def __init__(self, URL=os.environ.get("SheetyPOSTURL")):
        self.URL = URL
        print(os.environ.get("SheetyPOSTURL"))

    def put_info_in_sheet(self, data=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        answers = [i for i in data["incorrect_answers"]] + [data["correct_answer"]]

        random.shuffle(answers)


        payload = {
            "sheet1": {
                "time": timestamp,
                "category": unescape(data["category"]),
                "question": unescape(data["question"]),
                "answer #1": unescape(answers[0]),
                "answer #2": unescape(answers[1]),
                "answer #3": unescape(answers[2]),
                "answer #4": unescape(answers[3]),
                "answer": unescape(data["correct_answer"]),
                "|": "|",

            }
        }

        response = requests.post(self.URL, json=payload)

        if response.status_code == 200 or response.status_code == 201:
            pass
        else:
            print(f"Failed with status code {response.status_code}")
            print(f"Error details: {response.text}")

    #Chatgpt
    def get_random_question(self):
        response = requests.get(self.URL)

        if response.status_code == 200:
            questions = response.json()["sheet1"]

            if not questions:
                return None

            return random.choice(questions)

        else:
            print(f"Failed with status code {response.status_code}")
            print(f"Error details: {response.text}")
            return None