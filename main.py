from info import GetInfo
from Sheet import SheetIt


import time


"""
If you want to use this, you need to put your sheety api in the .env.test
https://docs.google.com/spreadsheets/d/1V42UHx4cXx-WYrobiZdOmcX79f4r2fbEELFgtEDOwU8/copy
Use this link for the google sheet.

--DEBUG-- - ModuleNotFoundError
To see the result, in the terminal, run
'pip install -r requirements.txt'
if doesn't work, first run
'python -m venv venv'
then try 
'pip install -r requirements.txt'
again

"""

question_number = 1

sheet = SheetIt()

seconds = -1 # Change to -1 to get fastest result with no wait.

try:
    while True:
        data = GetInfo()
        data.get_question()

        sheet.put_info_in_sheet(data=data.data)

        if seconds != -1:
            time.sleep(seconds)

        print(f"Question #{question_number} is done.")

except KeyboardInterrupt:
    print("Done")
    exit()