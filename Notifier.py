import time
from tkinter import *
from tkinter import messagebox
from plyer import notification
from gtts import gTTS
from playsound import playsound


t = Tk()
t.title('Notifier')
t.geometry("500x300")

# alert before notification
def alert():
    global title
    title = title1.get()
    global msg
    msg = msg1.get()
    global Time
    Time = time1.get()

    if title == "" or msg == "" or time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(Time))
        min_to_sec = int_time * 30
        messagebox.showinfo("notifier set", "set notification ?")
        a = "Half of the time has been over"
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=title,
                            message= a,
                            app_name="Notifier",
                            timeout=10)
        # alert sound
        playsound('alert.mp3')

        get_details()

# get details
def get_details():
    language = 'en'
    output = gTTS(text=msg, lang=language)

    int_time = int(float(Time))
    min_to_sec = int_time * 30
    time.sleep(min_to_sec)

    notification.notify(title=title,
                            message=msg,
                            app_name="Notifier",
                            timeout=10)
    playsound('siren.wav')

    #speak-Text (output)
    output.save("output.mp3")
    playsound('output.mp3')


# Label - Title
t_label = Label(t, text="Title to Notify", font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title1 = Entry(t, width=25, font=("poppins", 13))
title1.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg1 = Entry(t, width=40, font=("poppins", 13))
msg1.place(x=123, height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width=5, font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=alert)
but.place(x=170, y=230)

t.mainloop()
