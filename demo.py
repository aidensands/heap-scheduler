from scheduler import Scheduler
import time
import random
from tkinter import *
from tkinter import ttk

schedule = Scheduler()
root = Tk()
root.title('Scheduler')
root.geometry('1440x1080')

task_entry = Label(root, text='Enter info for task below')
task_entry.pack()

task_name = Label(root, text='Task Title:')
task_name.pack()
task_name_box = Entry(root, width=20)
task_name_box.pack()

task_priority = Label(root, text='Priority:')
task_priority.pack()
task_priority_box = Entry(root, width=10)
task_priority_box.pack()

desc = Label(root, text='Description:')
desc.pack()
desc_box = Entry(root, width=100)
desc_box.pack()

tree_frame = Frame(root)
tree_frame.pack(fill=BOTH, expand=True, pady=10)
tree = ttk.Treeview(tree_frame, columns=('Priority', 'Name', 'Description'), show="headings")
tree.pack()

tree.heading('Priority', text='Priority')
tree.heading('Name', text='Task')
tree.heading('Description', text='Description')

tree.column('Priority', width=100)
tree.column('Name', width=200)
tree.column('Description', width=500)


def add_button_action():
    result = schedule.add_task(task_name_box.get(),
                               task_priority_box.get(),
                               desc_box.get())
    add_popup.configure(text=result)
    update_table()

def update_table():
    for item in tree.get_children():
        tree.delete(item)

    tasks = schedule.get_tasks()
    for task in tasks:
        tree.insert('', 'end', values=(task.priority, task.name, task.description))

add_button = Button(root, text='Add Task', command=add_button_action)
add_button.pack()

add_popup = Label(root, text='')
add_popup.pack()

def do_button_action():
    result = schedule.do_task()
    do_popup.configure(text=result)
    update_table()


do_button = Button(root, text='Do Task', command=do_button_action)
do_button.pack()

do_popup = Label(root, text='')
do_popup.pack()

if __name__ == '__main__':
    root.mainloop()
