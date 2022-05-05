import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import null

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize (creds)
name_class = "LVTN"

sheet = client.open("gg_sheet_com")
work_sheet = sheet.worksheet(name_class)

lesson_period = [1,2,3,4,5,6,7,8,9,10,11,12,13]
lesson_start_time = [6,7,8,9,10,11,12,13,14,15,16,17,18]

def get_date ():
    Now = datetime.datetime.now()
    date_get = Now.strftime("%d/%m")
    return date_get

def get_time ():
    Now = datetime.datetime.now()
    time_get=[]
    time_get.append(Now.strftime("%H"))
    time_get.append(Now.strftime("%M"))
    return time_get

def time_check(check_in_time, class_period, i = 0, class_start_time = 0):
    for period in lesson_period:
        if class_period == period:
            class_start_time = int(lesson_start_time[i])
        i = i + 1
    if class_start_time	== 0:
        return "Null"

    if int(check_in_time[0]) < class_start_time:
        return "On time"
    else:
        if int(check_in_time[1]) <= 15:
            return "On time"
        else: 
            return "Late"


MSSV_sheet = work_sheet.cell(8, 3).value
print (str(type(MSSV_sheet)))
if str(type(MSSV_sheet)) == "<class 'NoneType'>":    
    print("1")
else: print ("0")

