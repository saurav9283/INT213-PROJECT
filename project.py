import time
from tkinter import *
import datetime
from tkinter.ttk import *
#global variables for stopwatch and timer
stopwatch_counter_num=66600
stopwatch_running=False
timer_counter_num=66600
timer_running=False
#Clock Function which controls the Time and Date Labels.
def clock():
    date_time=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S/%p") #taking Date and Time
    #converting in PM and AM time
    date,time1=date_time.split()
    time2,time3=time1.split('/')
    hour,minute,second=time2.split(':')
    if int(hour)>12 and int(hour)<=24:
        time= str(int(hour)-12)+":"+minute+":"+second+" "+time3
    else:
        time=time2+" "+time3
    time_label.config(text = time)
    current_time.config(text=time)
    date_label.config(text=date)
    time_label.after(1000,clock)
#Creating alarm Function which is called by The alarm_button
def alarm():
    main_time=datetime.datetime.now().strftime("%H:%M %p") #Taking  time form datetime module and formating it
    #spliting maintime and alarm time in hour,minute,second,AM/PM
    main_time1,main_time2=main_time.split(' ')
    main_hour1,main_minute=main_time1.split(":")
    alarm_time=alarm_input.get()
    alarm_time1,alarm_time2=alarm_time.split(' ')
    alarm_hour,alarm_minute=alarm_time1.split(":")
    #converting maintime in PM and AM time
    if int(main_hour1)>12 and int(main_hour1)<=24:
        main_hour=str(int(main_hour1)-12)
    else:
        main_hour=main_hour1
    # checking if the time entered is same or not
    if int(main_hour)==int(alarm_hour) and int(main_minute)==int(alarm_minute) and main_time2==alarm_time2:
        #changing alarm status label
        alarm_status.config(text="Weak Up")
        alarm_button.config(state="enabled")
        alarm_input.config(state="enabled")

    else:
        # changing alarm status label
        alarm_status.config(text="Alarm has started")
        alarm_button.config(state="disabled")
        alarm_input.config(state="disabled")
    alarm_status.after(1000,alarm)

# This function adds 1 to the Stopwatch counter num in every one second
def stopwatch_counter(label):
    def counter():
        if stopwatch_running:
            global  stopwatch_counter_num
            tt = datetime.datetime.fromtimestamp(stopwatch_counter_num)
            string = tt.strftime("%H:%M:%S")
            display = string
            label.config(text=display)
            label.after(1000,counter)
            stopwatch_counter_num+=1
    counter()
#stopwatch function which controls the stopwatch and is called by the Stopwatch Buttons
def stopwatch(work):
    global stopwatch_running
    if work=="start":
        stopwatch_running=True
        stopwatch_start.config(state="disabled")
        stopwatch_stop.config(state="enabled")
        stopwatch_rest.config(state="enabled")
        stopwatch_counter(stopwatch_label)
    elif work=="stop":
        stopwatch_running = False
        stopwatch_start.config(state="enabled")
        stopwatch_stop.config(state="disabled")
        stopwatch_rest.config(state="enabled")
    else:
        global  stopwatch_counter_num
        stopwatch_running = False
        stopwatch_counter_num=66600
        stopwatch_start.config(state="enabled")
        stopwatch_stop.config(state="disabled")
        stopwatch_rest.config(state="disabled")
        stopwatch_label.config(text="00:00:00")
#this function subtracts 1 to the Timer counter num in every one second.
def timer_counter(label):

    def count():
        global timer_running
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 66600:
                display = "Time is up"
                timer_running = False
                timer("reset")
            else:
                tt = datetime.datetime.fromtimestamp(timer_counter_num)
                string = tt.strftime("%H:%M:%S")
                display = string
                timer_counter_num -= 1
            label.config(text=display)
            label.after(1000, count)
    count()
#Timer function which controls the Timer and is called by the Timer Buttons
def timer(work):
    if work=="start":
        global timer_running, timer_counter_num
        timer_running=True
        if timer_counter_num==66600:
            timer_time_str = timer_entry.get()
            hour, minute, second = timer_time_str.split(":")
            minute = int(minute) + int(hour) * 60
            second = (minute * 60) + int(second)
            timer_counter_num += second
        timer_counter(timer_label)
        timer_start.config(state="disable")
        timer_rest.config(state="enable")
        timer_stop.config(state="enable")
        timer_entry.config(state="disable")
    elif work=="stop":
        timer_running=False
        timer_start.config(state="enable")
        timer_rest.config(state="enable")
        timer_stop.config(state="disable")
    elif work=="reset":
        timer_running=False
        timer_counter_num=66600
        timer_label.config(text='00:00:00')
        timer_start.config(state="enable")
        timer_stop.config(state="disable")
        timer_rest.config(state="disable")
        timer_entry.config(state="enable")
        timer_entry.delete(0, END)

my_win=Tk()
my_win.title("Clock") #title
my_win.geometry("600x400") #setting  window size
my_win.minsize(550,400)
my_win.maxsize(600,400)
#creating Tabs by using Notebook
main_tab=Notebook(my_win)
clock_tab=Frame(main_tab)
alarm_tab=Frame(main_tab)
stopwatch_tab=Frame(main_tab)
timer_tab=Frame(main_tab)
main_tab.add(clock_tab,text="Clock")
main_tab.add(alarm_tab,text="Alarm")
main_tab.add(stopwatch_tab,text="Stopwatch")
main_tab.add(timer_tab,text="Timer")
main_tab.pack(expand=1,fill="both")
clock_label=Label(clock_tab,text="Clock",foreground="red",font="calibri 45 bold")
clock_label.pack(pady=20)
              #clock
#creating time and date labels which will get data from clock function
time_label=Label(clock_tab,foreground="green",font="calibri 35 bold")
time_label.pack(pady=5)
date_label=Label(clock_tab,foreground="green",font="calibri 35 bold")
date_label.pack()
#creating Alarm and current_time labels,current time label get input from clock function
alarm_label=Label(alarm_tab,text="Alarm",foreground="red",font="calibri 45 bold")
alarm_label.pack(pady=20)
current_time=Label(alarm_tab,font="calibri 12 bold")
current_time.pack(pady=5)
                   #Alarm
# Creating Alarm Entry Box, Alarm Instructions and Set Alarm button which call alarm function
alarm_input=Entry(alarm_tab,font="calibri 15 bold")
alarm_input.pack()
alarm_input_details=Label(alarm_tab,font = 'calibri 10 bold',text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
alarm_input_details.pack()
alarm_button=Button(alarm_tab,text="Set Alarm",command=alarm)
alarm_button.pack(pady=20)
#Creating Alarm Status Label
alarm_status=Label(alarm_tab,font = 'calibri 15 bold')
alarm_status.pack()
            #stopwatch
#Stopwatch Heading label ,stopwatch Label, Start , Pause, Reset Buttons which calls the stopwatch function.
stopwatch_heading=Label(stopwatch_tab,text="Stopwatch",foreground="red",font="calibri 45 bold")
stopwatch_heading.pack(pady=20)
stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='00:00:00')
stopwatch_label.pack()
stopwatch_start=Button(stopwatch_tab,text="Start",command=lambda :stopwatch("start"))
stopwatch_start.pack(side=LEFT,padx=70)
stopwatch_stop=Button(stopwatch_tab,text="Pause",state="disable",command=lambda :stopwatch("stop"))
stopwatch_stop.pack(anchor="center",side=LEFT,padx=40)
stopwatch_rest=Button(stopwatch_tab,text="Reset",state="disable",command=lambda :stopwatch("reset"))
stopwatch_rest.pack(side=LEFT,padx=50,fill=X)
                   #timer
#Timer heading label,Timer entry, instructions label,timer label and Start, Stop, Reset Button which calls Timer function
timer_label1=Label(timer_tab,text="Timer",foreground="red",font="calibri 45 bold")
timer_label1.pack()
timer_entry=Entry(timer_tab,font="calibri 15 bold")
timer_entry.pack()
timer_label2=Label(timer_tab,text="Enter Timer Time. Eg -> 01:30:30")
timer_label2.pack()
timer_label=Label(timer_tab,text="00:00:00",font="calibri 40 bold")
timer_label.pack()
timer_start=Button(timer_tab,text="Start",command=lambda :timer("start"))
timer_start.pack(side=LEFT,padx=70)
timer_stop=Button(timer_tab,text="Pause",state="disable",command=lambda :timer("stop"))
timer_stop.pack(anchor="center",side=LEFT,padx=40)
timer_rest=Button(timer_tab,text="Reset",state="disable",command=lambda :timer("reset"))
timer_rest.pack(side=LEFT,padx=50,fill=X)
#creating Exit button with quit command
end_button=Button(my_win,text="Exit",command=quit)
end_button.pack(side=RIGHT)
clock() #starting clock function
my_win.mainloop()
