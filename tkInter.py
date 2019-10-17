# import tkinter as tk

# def write_slogan():
#     # print("Tkinter is easy to use!")
#     import datetime
#     loginTime = datetime.datetime.now()
#     print('You are logged at : ', loginTime)
#     import openpyxl 
#     # Call a Workbook() function of openpyxl  
#     # to create a new blank Workbook object 
#     wb = openpyxl.Workbook() 
    
#     # Get workbook active sheet   
#     # from the active attribute 
#     sheet = wb.active 
#     # One can change the name of the title 
#     c1 = sheet.cell(row = 1, column = 1) 
#     # writing values to cells 
#     c1.value = "logged In"

#     c2 = sheet.cell(row= 1 , column = 2) 
#     c2.value = loginTime



#     # Once have a Worksheet object, one can 
#     # access a cell object by its name also. 
#     # A2 means column = 1 & row = 2. 
#     # c3 = sheet['A2'] 
#     # c3.value = "RAHUL"

#     # # B2 means column = 2 & row = 2. 
#     # c4 = sheet['B2'] 
#     # c4.value = "RAI"

#     # Anytime you modify the Workbook object 
#     # or its sheets and cells, the spreadsheet 
#     # file will not be saved until you call 
#     # the save() workbook method. 
#     wb.save("attendence.ods") 

# # print(write_slogan.loginTime)

# def logout():
#     import datetime
#     logoutTime = datetime.datetime.now()
#     print('You are logged Out : ', logoutTime)
#     import openpyxl 
#     # Call a Workbook() function of openpyxl  
#     # to create a new blank Workbook object 
#     wb = openpyxl.Workbook() 
#     # Get workbook active sheet   
#     # from the active attribute 
#     sheet = wb.active 
#     # One can change the name of the title 
#     c3 = sheet['A2'] 
#     c3.value = "logout"

#     # B2 means column = 2 & row = 2. 
#     c4 = sheet['B2'] 
#     c4.value = logoutTime
#     wb.save("attendence.ods")

# # diff = loginTime - logoutTime
# # days, seconds = diff.days, diff.seconds
# # hours = days * 24 + seconds // 3600
# # minutes = (seconds % 3600) // 60
# # seconds = seconds % 60
# # print('hours: ',hours)
# # print('minutes: ',minutes)
# # print('seconds: ',seconds)


# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, 
#                    text="Stop", 
#                    fg="red",
#                    command=logout)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Start",
#                    command=write_slogan)
# slogan.pack(side=tk.LEFT)

# root.mainloop()




# import tkinter as tk
# import datetime
# def uptime():
#     try:
#         f = open( "/proc/uptime" )
#         contents = f.read().split()
#         f.close()
#     except:
#         return "Cannot open uptime file: /proc/uptime"

#     total_seconds = float(contents[0])

#     # Helper vars:
#     MINUTE  = 60
#     HOUR    = MINUTE * 60
#     DAY     = HOUR * 24

#     # Get the days, hours, etc:
#     days    = int( total_seconds / DAY )
#     hours   = int( ( total_seconds % DAY ) / HOUR )
#     minutes = int( ( total_seconds % HOUR ) / MINUTE )
#     seconds = int( total_seconds % MINUTE )

#     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
#     string = ""
#     if days > 0:
#         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
#     if len(string) > 0 or hours > 0:
#         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
#     if len(string) > 0 or minutes > 0:
#         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
#     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
#     print('string: ',string)
#     now = datetime.datetime.now()
#     print(now)
#     import openpyxl 
#     # Call a Workbook() function of openpyxl  
#     # to create a new blank Workbook object 
#     wb = openpyxl.Workbook() 
    
#     # Get workbook active sheet   
#     # from the active attribute 
#     sheet = wb.active 
#     # One can change the name of the title 
#     c1 = sheet.cell(row = 1, column = 1) 
#     # writing values to cells 
#     c1.value = "logged In"

#     c2 = sheet.cell(row= 1 , column = 2) 
#     c2.value = string

#     c3 = sheet.cell(row=1,column=3)
#     c3.value = now
#     wb.save("attendence.ods") 

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, 
#                    text="Stop", 
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Start",
#                    command=uptime)
# slogan.pack(side=tk.LEFT)

# root.mainloop()

import tkinter as tk
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import getpass

import os
import time
import re
from pynput import mouse
from pynput.keyboard import Key, Listener
from pynput import keyboard



def uptime():
    try:
        f = open( "/proc/uptime" )
        contents = f.read().split()
        f.close()
    except:
        return "Cannot open uptime file: /proc/uptime"

    total_seconds = float(contents[0])

    # Helper vars:
    MINUTE  = 60
    HOUR    = MINUTE * 60
    DAY     = HOUR * 24

    # Get the days, hours, etc:
    days    = int( total_seconds / DAY )
    hours   = int( ( total_seconds % DAY ) / HOUR )
    minutes = int( ( total_seconds % HOUR ) / MINUTE )
    seconds = int( total_seconds % MINUTE )

    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
    string = ""
    if days > 0:
        string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
    if len(string) > 0 or hours > 0:
        string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
    if len(string) > 0 or minutes > 0:
        string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
    string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
    # print('string: ',string)
    now = datetime.now()
    # print(now)
    date = str(now.strftime("%m/%d/%Y"))
    # print("date and time:",date)	
    time =str(now.strftime("%H:%M:%S"))
    # print("time:", time)
    
    username = str(getpass.getuser())
    print('username:',username)
    scope =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials= ServiceAccountCredentials.from_json_keyfile_name('SpreadsheetExample-1e7ddd7a4913.json',scope)
    gc = gspread.authorize(credentials)
    wks= gc.open('Test').sheet1
    # print(wks.get_all_records())

    wks.append_row([username,date,time,string])

    # def on_click(x, y, button, pressed):
    #     f=open('maniac1.txt','a')
    #     if button == mouse.Button.left:
    #         print ('Left')
    #         #f.write('left\n')
    #     if button == mouse.Button.right:
    #         # key_listener.stop()
    #         print ('right')
    #         #f.write('right\n')
    #     if button == mouse.Button.middle:
    #         print ('middle')
    #         #f.write('middle\n')
    # with mouse.Listener(on_click=on_click) as listener:
    #         listener.join()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Stop",
                   fg="red", width=25, padx=10, pady=10,bg='white',
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Start",fg='green',width=25,padx=10, pady=10,bg='white',  
                   command=uptime)
slogan.pack(side=tk.LEFT)

root.mainloop()