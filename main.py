from threading import Thread
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import os

im = Image.open(
    "C:\\Users\\SWAPNIL\\Desktop\\my project\\n queen game\\q1.png")
main_window = tk.Tk()
main_window.geometry("600x650+20+20")
main_window.resizable(False, False)
main_window.title("Set Queen")

canvas = Canvas(main_window, width=600, height=600, background="#191919")
canvas.place(x=0, y=0)

size = 5
total_queen = 5
box_list = []
image_list = []
one_box_w = 0


def draw_box(flag):
    global size
    global box_list
    global image_list
    global one_box_w
    global im
    global new_img
    global total_queen
    if(flag == True):
        box_list = []
        image_list = []
    one_box_w = int(600/size)
    im = im.resize((one_box_w, one_box_w))
    new_img = ImageTk.PhotoImage(im)
    for i in range(size):
        col = []
        for j in range(size):
            col.append(0)
        box_list.append(col)
    image_list = box_list.copy()
    k = 0
    for i in range(size):
        for j in range(size):
            if(i % 2 == k and j % 2 == k):
                canvas.create_rectangle(one_box_w*i, one_box_w*j, one_box_w*(
                    i+1), one_box_w*(j+1), width=1, outline="#ffffff", fill="#afa154")
            else:
                canvas.create_rectangle(one_box_w*i, one_box_w*j, one_box_w*(
                    i+1), one_box_w*(j+1), width=1, outline="#ffffff", fill="#fbefb1")
        if(k == 0):
            k = 1
        else:
            k = 0


draw_box(True)


def chack_queen(x, y, size):
    chack_list = []
    for i in range(size):
        c = x + i
        d = y + i
        e = x - i
        f = y - i
        if(c < size):
            chack_list.append((c, y))
        if(d < size):
            chack_list.append((x, d))
        if(e > -1):
            chack_list.append((e, y))
        if(f > -1):
            chack_list.append((x, f))
        if(e > -1 and f > -1):
            chack_list.append((e, f))
        if(c < size and f > -1):
            chack_list.append((c, f))
        if(c < size and d < size):
            chack_list.append((c, d))
        if(e > -1 and d < size):
            chack_list.append((e, d))
    res = []
    [res.append(x) for x in chack_list if x not in res]
    res.remove((x, y))
    return res


def set_image(x, y, img):
    global one_box_w
    canvas.create_image(x*one_box_w, y*one_box_w, image=img, anchor=NW)


def click_mouse(e):
    global one_box_w
    global size
    global new_img
    global total_queen
    if(box_list[e.y//one_box_w][e.x//one_box_w] == 0):
        cl = chack_queen(e.x//one_box_w, e.y//one_box_w, size)
        for i in range(len(cl)):
            if(box_list[cl[i][1]][cl[i][0]] == 1):
                messagebox.showinfo("NOT found", "Wrong Place")
                return 0
        canvas.delete("all")
        draw_box(False)
        box_list[e.y//one_box_w][e.x//one_box_w] = 1
        total_queen = total_queen - 1
        set_queent_value()
        for i in range(size):
            for j in range(size):
                if(box_list[i][j] == 1):
                    set_image((j), (i), new_img)
    else:
        cl = chack_queen(e.x//one_box_w, e.y//one_box_w, size)
        for i in range(len(cl)):
            if(box_list[cl[i][1]][cl[i][0]] == 1):
                messagebox.showinfo("NOT found", "Wrong Place")
                return 0

        canvas.delete("all")
        draw_box(False)
        box_list[e.y//one_box_w][e.x//one_box_w] = 0
        total_queen = total_queen + 1
        set_queent_value()
        for i in range(size):
            for j in range(size):
                if(box_list[i][j] == 1):
                    set_image((j), (i), new_img)

    if(total_queen == 0):
        messagebox.showinfo("win", "Won the match")


options = [
    "4x4",
    "5x5",
    "6x6",
    "7x7",
    "8x8"
]

value = StringVar()
manu_box = OptionMenu(main_window, value, *options)
value.set("5x5")
manu_box.place(x=20, y=605)


def set_queent_value():
    global total_queen
    queen_value_l.configure(text=f"Queen : {total_queen}")


def set_fun():
    global size
    global total_queen
    a = value.get().split("x")
    size = int(a[0])
    total_queen = size
    canvas.delete("all")
    draw_box(True)
    queen_value_l.configure(text=f"Queen : {total_queen}")


set_btn = Button(main_window, text="Set", font=font.BOLD,
                 width=5, command=set_fun)
set_btn.place(x=120, y=605)


queen_value_l = Label(
    main_window, text=f"Queen : {total_queen}", font=font.BOLD)
queen_value_l.place(x=240, y=605)


def threading():
    t1 = Thread(target=Run_sim)
    t1.start()


def Run_sim():
    os.system(f"python simulator.py {size}")


simulator_btn = Button(main_window, text="Simulator",
                       font=font.BOLD, width=8, command=threading)
simulator_btn.place(x=420, y=605)

canvas.bind("<Button-1>", click_mouse)
main_window.mainloop()
