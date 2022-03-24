import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pytz import timezone
from datetime import datetime

def addToSpreadsheet(users,userList):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open("Face-recognition").sheet1


    now_utc = datetime.now(timezone('UTC'))
    time = now_utc.astimezone(timezone('Asia/Kolkata'))
    date  = time.strftime('%d-%m-%Y')
    time = time.strftime("%I:%M:%S %p")

    count = len(sheet.col_values(1))
    for i,Id in enumerate(userList):
        
        row = [count+i,Id, users[str(Id)]['name'], date, time]
        index = count+1+i
        sheet.insert_row(row, index)
