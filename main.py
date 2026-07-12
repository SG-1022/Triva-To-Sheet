from info import GetInfo
from Sheet import SheetIt


import time


# If you want to use this, you need to put your sheety api in the .env.test
# https://docs.google.com/spreadsheets/d/1V42UHx4cXx-WYrobiZdOmcX79f4r2fbEELFgtEDOwU8/copy
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