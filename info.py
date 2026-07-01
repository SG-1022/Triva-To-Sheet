import requests

class GetInfo:

    def __init__(self, URL="https://opentdb.com/api.php?amount=1&type=multiple"):
        self.URL = URL
        self.data = None

    def get_question(self):
        response = requests.get(self.URL).json()

        if response["response_code"] == 5:
            return self.get_question()

        self.data = response["results"]

        self.data = self.data[0]

        return self.data


