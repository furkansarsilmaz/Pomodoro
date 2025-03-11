from tkinter import *
from tkinter import messagebox
from StopButton import *
#from Update import Update

class Pomodoro:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("Pomodoro")
        self.root.configure(background="gray")        
        self.short_break = 300  
        self.long_break =  900 
        self.pomodoro_duration = 1500 
        self.pomodoro_count = 0
        self.count_id = None
        self.time_left = self.pomodoro_duration
        self.on_break = False

        self.time_label = Label(root, text="",width=30, height=2)
        self.time_label.pack(pady=5)

        self.pomodoro_label = Label(root,text=self.pomodoro_count,height=2,width=20)
        self.pomodoro_label.pack(pady=5)

        self.start_button = Button(root, text="Start", command=lambda: self.count_function(self.pomodoro_duration), width=7, height=1)
        self.start_button.pack(pady=5)
        
        self.StopButton = Stopbutton(self.time_label)
        self.stop_button = Button(root, text="Stop", command= lambda: self.StopButton.stop_function(self.count_id), width=7, height=1)
        self.stop_button.pack(pady=5)

        self.continue_button = Button(root, text="Continue", command=self.continue_function, width=7, height=1)
        self.continue_button.pack(pady=5)

    def count_function(self,time):
        self.time_left = time
        time_minute = time // 60
        time_second = time % 60
        self.time_label.config(text=f"{time_minute:02d}:{time_second:02d}")

        if time > 0:
            self.count_id = self.time_label.after(1000, self.count_function, time - 1)
            self.time_left = time

        elif time == 0:
            if self.on_break:
                messagebox.showinfo("Pomodoro", "Time to get back to work!")
                self.on_break = False
                self.count_function(self.pomodoro_duration)

            else:
                self.pomodoro_count += 1
                self.update_function(self.pomodoro_count)
                if self.pomodoro_count % 4 == 0:  
                    messagebox.showinfo("Long Break", "Long break time!")
                    self.on_break = True
                    self.count_function(self.long_break)
                else:  
                    messagebox.showinfo("Short Break", "Short break time!")
                    self.on_break = True
                    self.count_function(self.short_break)    

    def continue_function(self):
        self.count_function(self.time_left)

    def update_function(self,pomodoro_count):
        self.pomodoro_label.config(text=f"Pomodoro count : {pomodoro_count}")



if __name__ == "__main__":
    root = Tk()
    Pomodoro(root)
    root.mainloop()