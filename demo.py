from scheduler import Scheduler
import time
import random
from tkinter import *

schedule = Scheduler()
root = Tk()
root.title('Scheduler')
root.geometry('1440x1080')

task_entry = Label(root, text='Enter info for task below')
task_entry.grid()

task_name = Label(root, text='Task Title:')
task_name.grid()
task_name_box = Entry(root, width=100)
task_name_box.grid()

task_priority = Label(root, text='Priority:')
task_priority.grid()
task_priority_box = Entry(root, width=100)
task_priority_box.grid()

desc = Label(root, text='Description:')
desc.grid()
desc_box = Entry(root, width=100)
desc_box.grid()

def add_button_action():
    result = schedule.add_task(task_name_box.get(),
                               task_priority_box.get(),
                               desc_box.get())
    add_popup.configure(text=result)



add_button = Button(root, text='Add Task', command=add_button_action)
add_button.grid()

add_popup = Label(root, text='')
add_popup.grid()

def do_button_action():
    result = schedule.do_task()
    do_popup.configure(text=result)


do_button = Button(root, text='Do Task', command=do_button_action)
do_button.grid()

do_popup = Label(root, text='')
do_popup.grid()

if __name__ == '__main__':
    root.mainloop()
