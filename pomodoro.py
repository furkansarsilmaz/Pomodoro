from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.title("Pomodoro")
short_break = 300
long_break = 900
pomodoro_duration = 1500
pomodoro_count = 0
count_id = None
time_left = pomodoro_duration
on_break = False



def count_function(time):
    global count_id, time_left, pomodoro_count, on_break

    time_minute = time // 60
    time_second = time % 60
    time_label.config(text=f"{time_minute:02d}:{time_second:02d}")
    
    if time > 0:
        count_id = time_label.after(1000, count_function, time - 1)
        time_left = time

    elif time == 0:
        if on_break:
            messagebox.showinfo("Pomodoro", "Time to get back to work!")
            on_break = False
            count_function(pomodoro_duration)

        else:
            pomodoro_count += 1
            update_function(pomodoro_count)
            if pomodoro_count % 4 == 0:  
                messagebox.showinfo("Long Break", "Long break time!")
                on_break = True
                count_function(long_break)
            else:  
                messagebox.showinfo("Short Break", "Short break time!")
                on_break = True
                count_function(short_break)


def stop_function():
    global count_id
    if count_id:
        time_label.after_cancel(count_id)


def continue_function():
    global time_left
    count_function(time_left)

def update_function(pomodoro_count):
    pomodoro_label.config(text=f"Pomodoro count : {pomodoro_count}")


time_label = Label(root, text="", bg="blue", fg="white", width=30, height=2)
time_label.pack()

pomodoro_label = Label(root,text=pomodoro_count,height=2,width=20)
pomodoro_label.pack()

start_button = Button(root, text="Start", command=lambda: count_function(pomodoro_duration), width=7, height=1).pack(pady=10)
stop_button = Button(root, text="Stop", command=stop_function, width=7, height=1).pack(pady=10)
continue_button = Button(root, text="Continue", command=continue_function, width=7, height=1).pack(pady=5)


if __name__ == "__main__":
    root.mainloop()