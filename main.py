from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
tick_str = ""
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # while reps < 8:

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)

    elif reps % 2 != 0:
        # if it's 1, 3, 5, 7 time - do:
        count_down(work_sec)
        timer.config(text="WORK", fg=GREEN)

    else:
        # if it's 2, 4, 6 = do
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global tick_str

    mins = math.floor(count / 60)
    sec = math.floor(count % 60)
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_str += CHECKMARK
            tick.config(text=tick_str)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

# 2 buttons
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

# 2 labels - timer and tick
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

tick = Label(fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
tick.grid(column=1, row=3)

window.mainloop()
