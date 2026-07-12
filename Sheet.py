import os
import requests
from datetime import datetime
import random
from html import unescape
from dotenv import load_dotenv

load_dotenv()

class SheetIt:

    def __init__(self, data, URL=os.environ.get("SheetyPOSTURL")):
        self.URL = URL
        self.data = data
        print(os.environ.get("SheetyPOSTURL"))

    def put_info_in_sheet(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        answers = [i for i in self.data["incorrect_answers"]] + [self.data["correct_answer"]]

        random.shuffle(answers)


        payload = {
            "sheet1": {
                "time": timestamp,
                "category": unescape(self.data["category"]),
                "question": unescape(self.data["question"]),
                "answer #1": unescape(answers[0]),
                "answer #2": unescape(answers[1]),
                "answer #3": unescape(answers[2]),
                "answer #4": unescape(answers[3]),
                "answer": unescape(self.data["correct_answer"]),
                "#If you want to see the answer, triple click the cell": " ",

            }
        }

        response = requests.post(self.URL, json=payload)

        if response.status_code == 200 or response.status_code == 201:
            pass
        else:
            print(f"Failed with status code {response.status_code}")
            print(f"Error details: {response.text}")