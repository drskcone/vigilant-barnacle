from tkinter import *
from datetime import date

window = Tk()
window.title("Workshop Check-In")
window.geometry("450x350")
window.configure(bg="#EAF3F8")

title_label = Label(
    window,
    text="Welcome to Our Workshop",
    fg="white",
    bg="#1261A0",
    font=("Arial", 16, "bold"),
    pady=12
)
title_label.pack(fill="x")

participant_label = Label(
    window,
    text="Enter Your Name:",
    bg="#EAF3F8",
    font=("Arial", 11)
)
participant_label.pack(pady=12)

participant_entry = Entry(
    window,
    width=30,
    font=("Arial", 11)
)
participant_entry.pack()

def welcome_participant():
    participant = participant_entry.get().strip()

    output_box.delete("1.0", END)

    if participant:
        welcome_text = (
            f"Hello {participant}!\n"
            "Thank you for attending our workshop.\n"
            f"Today's Date: {date.today()}"
        )
    else:
        welcome_text = "Please enter your name to check in."

    output_box.insert(END, welcome_text)

output_box = Text(
    window,
    height=5,
    width=42,
    font=("Arial", 10),
    wrap=WORD
)
output_box.pack(pady=15)

checkin_button = Button(
    window,
    text="Submit Check-In",
    command=welcome_participant,
    bg="#1261A0",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
checkin_button.pack(pady=5)

window.mainloop()