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

def get_date ():
    Now = datetime.datetime.now()
    date_get = Now.strftime("%d/%m")
    return date_get

def get_time ():
    Now = datetime.datetime.now()
    time_get=[0,0]
    time_get[0] = Now.strftime("%H")
    time_get[1] = Now.strftime("%M")
    return time_get

def MSSV_check (MSSV, row_position = -1, MSSV_row = 6, MSSV_col = 3, Total_Stu_row = 3, Total_Stu_col = 3):
    Total_Stu = int(work_sheet.cell(Total_Stu_row,Total_Stu_col).value)

    while True:
        print (MSSV_col, MSSV_row)
        MSSV_sheet = work_sheet.cell(MSSV_row, MSSV_col).value
        if str(type(MSSV_sheet)) == "<class 'NoneType'>":
            return row_position
        elif MSSV_sheet != MSSV:
            MSSV_row = MSSV_row + 1
        else:
            row_position = MSSV_row
            return row_position

def date_check (date, col_position=-1, date_row = 5, date_col = 4):
    while True:
        date_cell = work_sheet.cell(date_row, date_col).value
        if str(type(date_cell)) == "<class 'NoneType'>":
            return col_position
        elif date_cell != date:
            date_col = date_col + 1
        else:
            col_position = date_col
            return col_position

def time_check(check_in_time, class_period, i = 0, class_start_time = 0, lesson_period = [1,2,3,4,5,6,7,8,9,10,11,12,13], lesson_start_time = [6,7,8,9,10,11,12,13,14,15,16,17,18]):
    for period in lesson_period:
        if class_period == period:
            class_start_time = int(lesson_start_time[i])
        i = i + 1
    if class_start_time	== 0:
        return "Null"

    if (int(check_in_time[0]) < class_start_time) & (int(check_in_time[0])> class_start_time-1):
        return "On time"
    elif int(check_in_time[0]) == class_start_time:
        if int(check_in_time[1]) <= 15:
            return "On time"
        else: 
            return "Late"
    else: 
        return "Null"

def UART_isr():
    UART_received = "1813841"
    MSSV_received = UART_received

    class_period = work_sheet.cell(2,3).value

    row_position = MSSV_check(MSSV_received)

    if row_position != -1:
        time_state = time_check([8,20], int(class_period))
        if time_state != "Null":
            col_position = date_check(get_date())
            work_sheet.update_cell(row_position, col_position, time_state)
        else: print("Worng time")
    else: 
        print ("khong co MSSV")

if __name__ == "__main__":
    UART_isr()
