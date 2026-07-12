from info import GetInfo
from Sheet import SheetIt


import time


#If you want to use this, you need to put your sheety api in the .env.test
# https://docs.google.com/spreadsheets/u/1/d/1JruQ79Ha3BbFPuZJlgERxfpq5qr_pGUJI85-KqBDVXk/copy
# Use this link for the google sheet.

try:
    while True:
        data = GetInfo()
        data.get_question()

        sheet = SheetIt(data=data.data)
        sheet.put_info_in_sheet()

        time.sleep(3600)

except KeyboardInterrupt:
    print("Done")
    raise SystemExit()