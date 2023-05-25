import numpy as np
from tkinter import *
from sympy import *
from tkinter import ttk
from sympy import var
from PIL import ImageTk, Image

ws = Tk()
ws.title('Numerical Analysis')
ws.geometry('1000x700')
# Loads the image from the file "background.png"
img = ImageTk.PhotoImage(file="background.png")
label = Label(ws, image=img)
label.place()

# Create a Canvas
canvas = Canvas(ws, width=800, height=400)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=img, anchor='nw')

# Function to resize the window
def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("background.png")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS )
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
# Bind the function to configure the parent window
ws.bind("<Configure>", resize_image)

color = "#f9f5eb"
color2 = "#e5dccf"
red_color = "#ea5355"
blue_color = "#012b5b"
font = 'Kefa Bold'
font_default = 'kefa'
border = 0.2

def start():
    # Create a new Tkinter window for the next page
    new_window = Tk()
    new_window.title('Next Page')
    new_window.geometry('1000x700')
    new_window.config(bg=color)

    # Create container frame in the new window
    container2 = Frame(new_window, background=color)
    container2.place(relx=0.5, rely=0.5, anchor='center')

    # Create functions button
    buttonfunc2 = Button(
        container2, text='Functions', relief='raised', font=(font, 20),
        bg=color2, fg=blue_color, borderwidth=border, command=functions
    )
    buttonfunc2.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    # Create matrices button
    buttonmat2 = Button(
        container2, text='Matrices', relief='raised', font=(font, 20),
        bg=color2, fg=blue_color, borderwidth=border, command=matrices
    )
    buttonmat2.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)


def functions():
    # Toplevel object which will
    # be treated as a new window
    functions_window = Toplevel(ws, background=color)
    functions_window.title("Functions")
    functions_window.geometry("1000x700")

    # create container
    container = Frame(functions_window)
    container.config(bg = color)
    container.pack(expand=True, pady=100)

    # Bisection button
    button_bis = Button(container, text='Bisection', relief=RAISED, font=(font, 20), bg=color2,
                        fg=blue_color, borderwidth=border, command=bisection)
    button_bis.pack(side=TOP, pady = 10)

    # False position button
    button_fal = Button(container, text='False position', relief=RAISED, font=(font, 20), bg=color2,
                        fg=blue_color, borderwidth=border, command=falsepos)
    button_fal.pack(side=TOP, pady = 10)

    # Simple Fixed Point button
    button_simp = Button(container, text='Simple Fixed Point', relief=RAISED, font=(font, 20), bg=color2,
                         fg=blue_color, borderwidth=border, command=simple)
    button_simp.pack(side=TOP, pady = 10)

    # Newton button
    button_new = Button(container, text='Newton', relief=RAISED, font=(font, 20), bg=color2,
                        fg=blue_color, borderwidth=border, command=newton)
    button_new.pack(side=TOP, pady = 10)

    # Secant button
    button_sec = Button(container, text='Secant', relief=RAISED, font=(font, 20), bg=color2,
                        fg=blue_color, borderwidth=border, command=secant)
    button_sec.pack(side=TOP, pady = 10)



def bisection():
    # create window
    bisec_window = Tk()
    bisec_window.title('Bisection Method')
    canvas1 = Canvas(bisec_window, width=800, height=400, bg = color, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(bisec_window, text='Enter function (f(x))', fg=blue_color)
    label1.config(font=(font_default, 12), bg=color)
    canvas1.create_window(400, 80, window=label1)
    entry1 = Entry(bisec_window)
    entry1.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(400, 110, window=entry1)

    # Xu
    label2 = Label(bisec_window, text='Xu', fg=blue_color)
    label2.config(font=(font_default, 12), bg=color)
    canvas1.create_window(240, 150, window=label2)
    entry2 = Entry(bisec_window)
    entry2.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(240, 180, window=entry2)

    # Xl
    label3 = Label(bisec_window, text='Xl', fg=blue_color)
    label3.config(font=(font_default, 12), bg=color)
    canvas1.create_window(400, 150, window=label3)
    entry3 = Entry(bisec_window)
    entry3.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(400, 180, window=entry3)

    # Error
    label4 = Label(bisec_window, text='Error', fg=blue_color)
    label4.config(font=(font_default, 12), bg=color)
    canvas1.create_window(560, 150, window=label4)
    entry4 = Entry(bisec_window)
    entry4.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(560, 180, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global eps
        eps = float(entry4.get())
        bisection_method(xl, xu)

    button1 = Button(bisec_window ,text='solve', command=solve_method, bg=color2, fg=blue_color, font=(font, 15), borderwidth=border)
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(bisec_window)
    style = ttk.Style(bisec_window)
    style.configure("Custom.Treeview", fieldbackground=blue_color)

    my_table = ttk.Treeview(bisec_window, style="Custom.Treeview")
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("xr", anchor=CENTER, width=100)
    my_table.column("f(xr)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("xr", text="Xr", anchor=CENTER)
    my_table.heading("f(xr)", text="f(xr)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def bisection_method(xl, xu):
        error = abs(xu - xl) * 100
        xr = 0
        step = 0
        # Check if the function values at xl and xu have the same sign, indicating no root or multiple roots
        if f.subs(x, xl) * f.subs(x, xu) >= 0:
            lable5 = Label(bisec_window, text='no root or multiple roots present')
            canvas1.create_window(400, 400, window=lable5)
            quit()
        # Iterate until the error is smaller than a predefined threshold (eps)
        while error > eps:
            xrold = xr
            xr = (xu + xl) / 2
            error = abs((xr - xrold) / xr) * 100

             # Insert values into a table for tracking the bisection steps
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), "-"))
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), error))
            step = step + 1
            if f.subs(x, xr) * f.subs(x, xl) > 0:
                xl = xr
            elif f.subs(x, xr) * f.subs(x, xl) < 0:
                xu = xr
            else:
                quit()
        printroot(xr)

    def printroot(xr):

        rootlabel = Label(bisec_window, text="Root=", bg = color ,fg = red_color)  # shows as text in the window
        rootlabel.config(font=(font, 12))
        canvas1.create_window(540, 230, window=rootlabel)
        root = Label(bisec_window, text=xr)  # shows as text in the window
        root.config(font=(font, 12), bg = color, fg = blue_color) 
        canvas1.create_window(620, 230, window=root)
    bisec_window.mainloop()
def falsepos():
    # create window
    FalsePosition_window = Tk()
    FalsePosition_window.title('False Position Method')
    canvas1 = Canvas(FalsePosition_window, width=800, height=400, relief='raised', bg=color)
    canvas1.pack()

    # equation
    label1 = Label(FalsePosition_window, text='Enter function (f(x))', bg=color, fg=blue_color)
    label1.config(font=(font_default, 12))
    canvas1.create_window(430, 50, window=label1)  # Updated y-coordinate for label
    entry1 = Entry(FalsePosition_window, width=40)
    entry1.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(FalsePosition_window, text='Xu', bg=color, fg=blue_color)
    label2.config(font=(font_default, 12))
    canvas1.create_window(220, 120, window=label2)  # Updated y-coordinate for label
    entry2 = Entry(FalsePosition_window)
    entry2.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(FalsePosition_window, text='Xl', bg=color, fg=blue_color)
    label3.config(font=(font_default, 12))
    canvas1.create_window(420, 120, window=label3)  # Updated y-coordinate for label
    entry3 = Entry(FalsePosition_window)
    entry3.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(420, 150, window=entry3)

    # Error
    label4 = Label(FalsePosition_window, text='Error', bg=color, fg=blue_color)
    label4.config(font=(font_default, 12))
    canvas1.create_window(620, 120, window=label4)  # Updated y-coordinate for label
    entry4 = Entry(FalsePosition_window)
    entry4.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(620, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global eps
        eps = float(entry4.get())
        bisection_method(xl, xu)

    button1 = Button(FalsePosition_window ,text='solve', command=solve_method, bg=color2, fg=blue_color, font=(font, 15), borderwidth=border)
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(FalsePosition_window)
    style = ttk.Style(FalsePosition_window)
    style.configure("Custom.Treeview", fieldbackground=blue_color)

    my_table = ttk.Treeview(FalsePosition_window, style="Custom.Treeview")
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("xr", anchor=CENTER, width=100)
    my_table.column("f(xr)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("xr", text="Xr", anchor=CENTER)
    my_table.heading("f(xr)", text="f(xr)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def bisection_method(xl, xu):
        error = abs(xu - xl) * 100
        xr = 0
        step = 0
        if f.subs(x, xl) * f.subs(x, xu) >= 0:
            lable5 = Label(FalsePosition_window, text='no root or multiple roots present')
            canvas1.create_window(400, 400, window=lable5)
            quit()
        while error > eps:
            xrold = xr
            xr = xu - ((f.subs(x, xu) * (xl - xu)) / (f.subs(x, xl) - f.subs(x, xu)))
            error = abs((xr - xrold) / xr) * 100
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), "-"))
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), error))
            step = step + 1
            if f.subs(x, xr) * f.subs(x, xl) < 0:
                xu = xr
            elif f.subs(x, xr) * f.subs(x, xu) < 0:
                xl = xr
            else:
                quit()
        printroot(xr)


    def printroot(xr):
        rootlabel = Label(FalsePosition_window, text="Root=", bg=color, fg = red_color)  # shows as text in the window
        rootlabel.config(font=(font, 12))
        canvas1.create_window(540, 230, window=rootlabel)
        root = Label(FalsePosition_window, text=xr)  # shows as text in the window
        root.config(font=(font, 12), fg=blue_color, bg=color)
        canvas1.create_window(620, 230, window=root)

    FalsePosition_window.mainloop()
def simple():
    # create window
    FixedPoint_window = Tk()
    FixedPoint_window.title('Simple fixed point Method')
    canvas1 = Canvas(FixedPoint_window, width=800, height=400, relief='raised', bg=color)
    canvas1.pack()

    # equation f(x)
    label1 = Label(FixedPoint_window, text='Enter function (f(x))', fg=blue_color)
    label1.config(font=(font_default, 12), bg=color)
    canvas1.create_window(200, 80, window=label1)
    entry1 = Entry(FixedPoint_window)
    entry1.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(200, 110, window=entry1)

    # equation g(x)
    label2 = Label(FixedPoint_window, text='Enter function (g(x))', fg=blue_color)
    label2.config(font=(font_default, 12), bg=color)
    canvas1.create_window(600, 80, window=label2)
    entry2 = Entry(FixedPoint_window)
    entry2.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(600, 110, window=entry2)

    # Xi
    label3 = Label(FixedPoint_window, text='Xi', fg=blue_color)
    label3.config(font=(font_default, 12), bg=color)
    canvas1.create_window(200, 150, window=label3)
    entry3 = Entry(FixedPoint_window)
    entry3.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(200, 180, window=entry3)

    # Error
    label4 = Label(FixedPoint_window, text='Error', fg=blue_color)
    label4.config(font=(font_default, 12), bg=color)
    canvas1.create_window(600, 150, window=label4)
    entry4 = Entry(FixedPoint_window)
    entry4.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(600, 180, window=entry4)


    def solve_method():
        x1 = entry1.get()
        x2 = entry2.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        global g
        f = sympify(x1)
        g = sympify(x2)
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        fixedpoint_method(xi)

    button1 = Button(FixedPoint_window, text='solve', command=solve_method, bg=color2, fg=blue_color, borderwidth=border, font=(font, 15))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(FixedPoint_window)
    style = ttk.Style(FixedPoint_window)
    style.configure("Custom.Treeview", fieldbackground=blue_color)

    my_table = ttk.Treeview(FixedPoint_window, style="Custom.Treeview")
    my_table['columns'] = ('i', 'xi', 'f(xi)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi", anchor=CENTER, width=100)
    my_table.column("f(xi)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi", text="Xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def fixedpoint_method(xi):
        step = 0
        condtion = True
        while condtion:
            xiplus1 = g.subs(x, xi)
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, xiplus1, "-"))
                error = abs((xiplus1 - xi) / xiplus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, xiplus1, error))
            step = step + 1
            condtion = error > eps
            error = abs((xiplus1 - xi) / xiplus1) * 100
            if error<eps:
                rootlabel = Label(FixedPoint_window, text="Root=", bg=color, fg = blue_color)  # shows as text in the window
                rootlabel.config(font=(font, 12))
                canvas1.create_window(540, 230, window=rootlabel)
                root = Label(FixedPoint_window, text=xi)  # shows as text in the window
                root.config(font=(font, 12), bg=color, fg=red_color)
                canvas1.create_window(620, 230, window=root)
            xi = xiplus1

    FixedPoint_window.mainloop()
def newton():
    # create window
    newton_window = Tk()
    newton_window.title('Newton Method')
    canvas1 = Canvas(newton_window, width=800, height=400, relief='raised', bg = color)
    canvas1.pack()

    # equation f(x)
    label1 = Label(newton_window, text='Enter function (f(x))', bg=color, fg=blue_color)
    label1.config(font=(font_default, 12))
    canvas1.create_window(270, 50, window=label1)  # Updated y-coordinate for label
    entry1 = Entry(newton_window)
    entry1.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(270, 80, window=entry1)

    # equation g(x)
    label2 = Label(newton_window, text='Enter function (g(x))', bg=color, fg=blue_color)
    label2.config(font=(font_default, 12))
    canvas1.create_window(600, 50, window=label2)  # Updated y-coordinate for label
    entry2 = Entry(newton_window)
    entry2.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(600, 80, window=entry2)

    # xi
    label3 = Label(newton_window, text='Xi', bg=color, fg=blue_color)
    label3.config(font=(font_default, 12))
    canvas1.create_window(300, 120, window=label3)  # Updated y-coordinate for label
    entry3 = Entry(newton_window)
    entry3.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(300, 150, window=entry3)

    # Error
    label4 = Label(newton_window, text='Error', bg=color, fg=blue_color)
    label4.config(font=(font_default, 12))
    canvas1.create_window(580, 120, window=label4)  # Updated y-coordinate for label
    entry4 = Entry(newton_window)
    entry4.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(580, 150, window=entry4)


    def solve_method():
        x1 = entry1.get()
        x2 = entry2.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        global g
        f = sympify(x1)
        g = sympify(x2)
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        newton_method(xi)

    button1 = Button(newton_window,text='solve', command=solve_method, bg=color, fg=blue_color, font=(font, 15), borderwidth=border)
    canvas1.create_window(400, 200, window=button1)
    # table
    my_table = ttk.Treeview(newton_window)
    style = ttk.Style(newton_window)
    style.configure("Custom.Treeview", fieldbackground=blue_color)

    my_table = ttk.Treeview(newton_window, style="Custom.Treeview")
    my_table['columns'] = ('i', 'xi', 'f(xi)', "f'(xi)", 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi", anchor=CENTER, width=110)
    my_table.column("f(xi)", anchor=CENTER, width=125)
    my_table.column("f'(xi)", anchor=CENTER, width=122)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi", text="Xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(Xi)", anchor=CENTER)
    my_table.heading("f'(xi)", text="f'(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 350, window=my_table)

    def newton_method(xi):
        step = 0
        condition = True
        while condition:
            xiplus1 = xi-(f.subs(x, xi)/g.subs(x, xi))
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, f.subs(x, xi), g.subs(x, xi), "-"))
                error = abs((xiplus1 - xi) / xiplus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, f.subs(x, xi), g.subs(x, xi), error))
                print(f.subs(x, xi))
            condition = error > eps
            error = abs((xiplus1 - xi) / xiplus1) * 100
            if error < eps:
                rootlabel = Label(newton_window, text="Root=", fg = blue_color, bg = color)  # shows as text in the window
                rootlabel.config(font=(font, 12))
                canvas1.create_window(540, 200, window=rootlabel)
                root = Label(newton_window, text=xi)  # shows as text in the window
                root.config(font=(font, 12), fg = red_color, bg = color)
                canvas1.create_window(620, 200, window=root)
            step = step + 1
            xi = xiplus1
    newton_window.mainloop()
def secant():
    # create window
    secant_window = Tk()
    secant_window.title('Secant Method')
    canvas1 = Canvas(secant_window, width=800, height=400, bg = color, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(secant_window, text='Enter function (f(x))', fg = blue_color)
    label1.config(font=(font_default, 12), bg = color)
    canvas1.create_window(300, 50, window=label1)
    entry1 = Entry(secant_window, width=40)
    entry1.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(300, 80, window=entry1)

    # Xu
    label2 = Label(secant_window, text='Xi-1', fg = blue_color)
    label2.config(font=(font_default, 12), bg = color)
    canvas1.create_window(140, 120, window=label2)
    entry2 = Entry(secant_window)
    entry2.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(140, 150, window=entry2)

    # Xl
    label3 = Label(secant_window, text='Xi', fg = blue_color)
    label3.config(font=(font_default, 12), bg = color)
    canvas1.create_window(340, 120, window=label3)
    entry3 = Entry(secant_window)
    entry3.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(340, 150, window=entry3)

    # Error
    label4 = Label(secant_window, text='Error', fg = blue_color)
    label4.config(font=(font_default, 12), bg = color)
    canvas1.create_window(540, 120, window=label4)
    entry4 = Entry(secant_window)
    entry4.configure(bg=color2, borderwidth=border, fg=red_color)
    canvas1.create_window(540, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        ximin1 = float(entry2.get())
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        secant_method(ximin1, xi)

    button1 = Button(secant_window, text='solve', command=solve_method, bg = color2, fg=blue_color,
                     borderwidth=border, font=(font, 15))
    canvas1.create_window(400, 230, window=button1)

    # Table
    my_table = ttk.Treeview(secant_window)
    style = ttk.Style(secant_window)
    style.configure("Custom.Treeview", fieldbackground=blue_color)

    my_table = ttk.Treeview(secant_window, style="Custom.Treeview")
    my_table['columns'] = ('i', 'xi-1', 'f(xi-1)', 'xi', 'f(xi)', 'Error')

    # Column configurations
    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi-1", anchor=CENTER, width=100)
    my_table.column("f(xi-1)", anchor=CENTER, width=120)
    my_table.column("xi", anchor=CENTER, width=100)
    my_table.column("f(xi)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    # Heading configurations
    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi-1", text="Xi-1", anchor=CENTER)
    my_table.heading("f(xi-1)", text="f(xi-1)", anchor=CENTER)
    my_table.heading("xi", text="xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)

    canvas1.create_window(410, 400, window=my_table)

    def secant_method(ximin1, xi):
        step = 0
        condition=True
        while condition:
            xiPlus1 = xi - (f.subs(x, xi)* (ximin1 - xi)) / (f.subs(x, ximin1)- f.subs(x, xi))
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, ximin1, f.subs(x, ximin1), xi, f.subs(x, xi), "-"))
                error = abs((xiPlus1 - xi) / xiPlus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, ximin1, f.subs(x, ximin1), xi, f.subs(x, xi), error))
            step = step + 1
            condition=error>eps
            error = abs((xiPlus1 - xi) / xiPlus1) * 100
            if error<eps:
                # print the root
                rootlabel = Label(secant_window, text="Root=", bg = color ,fg = blue_color)  # shows as text in the window
                rootlabel.config(font=(font, 12))
                canvas1.create_window(540, 230, window=rootlabel)
                root = Label(secant_window, text=xi)
                root.config(font=(font, 12), fg=red_color ,bg=color)
                canvas1.create_window(620, 230, window=root)
            ximin1 = xi
            xi = xiPlus1

    secant_window.mainloop()


def matrices():
    newWindow = Toplevel(ws, bg=color)
    newWindow.geometry("1000x700")

    container = Frame(newWindow, bg=color)
    container.pack(expand=True, anchor='center')

    button = Button(
        container,
        text='Gaussian elimination',
        relief=RAISED,
        font=(font, 20),
        bg=color2, fg=blue_color, activebackground=color2, activeforeground=color2, borderwidth=border, command=gaus
    )
    button.pack(pady = 12)

    # button = Button(
    #     container,
    #     text='Cramers rule',
    #     relief=RAISED,
    #     font=(font, 20),
    #     bg=color2, fg=blue_color, activebackground=color2, activeforeground=color2, borderwidth=border, command=cramers
    # )
    button.pack(pady = 12)

    button = Button(
        container,
        text='LU decomposition',
        relief=RAISED,
        font=(font, 20),
        bg=color2, fg=blue_color, activebackground=color2, activeforeground=color2, borderwidth=border, command=ludec
    )
    button.pack(pady = 12)

def ludec():
    # create window
    LU_window = Tk()
    LU_window.title('LU Method')
    canvas1 = Canvas(LU_window, width=800, height=400, relief='raised', bg=color)
    canvas1.pack()
    # create frane for user input
    matrixFrame = Frame(LU_window)
    canvas1.create_window(400, 130, window=matrixFrame)
    all_entries = []
    rows = 3
    cols = 4

    label1 = Label(LU_window, text='x1', fg = blue_color, bg = color)
    label1.config(font=(font_default, 12))
    canvas1.create_window(275, 75, window=label1)
    label2 = Label(LU_window, text='x2', fg = blue_color, bg = color)
    label2.config(font=(font_default, 12))
    canvas1.create_window(360, 75, window=label2)
    label3 = Label(LU_window, text='x3', fg = blue_color, bg = color)
    label3.config(font=(font_default, 12), fg = blue_color, bg = color)
    canvas1.create_window(440, 75, window=label3)
    label4 = Label(LU_window, text='b')
    label4.config(font=(font_default, 12), fg = blue_color, bg = color)
    canvas1.create_window(525, 75, window=label4)
    global lmax
    lmax = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # creates grid view for matrix
    for r in range(rows):
        entries_row = []
        for c in range(cols):
            e = Entry(matrixFrame, width=8, bg = blue_color,fg=color)  # 5 chars
            e.insert('end', 0)
            e.grid(row=r, column=c)
            entries_row.append(e)
        all_entries.append(entries_row)

    # gets input for user and insert it into matrix
    def enter():
        # fill matrix with 0
        matrix = np.zeros((rows, cols))
        # insert values in matrix
        for r, row in enumerate(all_entries):
            for c, entry in enumerate(row):
                text = entry.get()
                matrix[r, c] = float(text)
        b = []
        b = [matrix[0, 3], matrix[1, 3], matrix[2, 3]]
        # make the upper triangle = 0 and fill l matrix
        umax = matrix
        for i in range(rows):
            if umax[i][i] == 0.0:
                print("no")
            for j in range(rows):
                if i != j and i < j:
                    ratio = umax[j][i] / umax[i][i]
                    lmax[j][i] = umax[j][i] / umax[i][i]
                    for k in range(cols):
                        umax[j][k] = umax[j][k] - ratio * umax[i][k]

        # sub for lc =b  and print C result on screen
        c1 = b[0]
        c2 = (b[1] - (lmax[1][0] * c1)) / lmax[1][1]
        c3 = (b[2] - (lmax[2][0] * c1 + lmax[2][1] * c2)) / lmax[2][2]
        Cresult = " "
        Cresult = ('  C1= %0.3f' % (c1)) + Cresult
        Cresult = ('  C2= %0.3f' % (c2)) + Cresult
        Cresult = ('  C3= %0.3f' % (c3)) + Cresult
        label2 = Label(LU_window, text='LC = b', bg=color, fg = red_color)
        label2.config(font=(font, 13))
        canvas1.create_window(280, 270, window=label2)
        label1 = Label(LU_window, text=Cresult, bg=color, fg=blue_color)
        label1.config(font=(font_default, 13))
        canvas1.create_window(320, 300, window=label1)
        # back sub and print X result on screen
        x3 = c3 / umax[2][2]
        x2 = (c2 - (umax[1][2] * x3)) / umax[1][1]
        x1 = (c1 - ((umax[0][1] * x2) + (umax[0][2] * x3))) / umax[0][0]
        Xresult = " "
        Xresult = ('  X1= %0.2f  ' % (x1)) + Xresult
        Xresult = ('  X2= %0.2f  ' % (x2)) + Xresult
        Xresult = ('  X3= %0.2f  ' % (x3)) + Xresult
        label2 = Label(LU_window, text='UX=C', bg = color, fg = red_color)
        label2.config(font=(font, 13))
        canvas1.create_window(280, 340, window=label2)
        label1 = Label(LU_window, text=Xresult, bg = color, fg =blue_color)
        label1.config(font=(font_default, 13))
        canvas1.create_window(320, 370, window=label1)

    enterbtn = Button(LU_window, text='Enter Matrix', command=enter, bg = color, fg = blue_color, font=(font, 15), borderwidth=border)
    canvas1.create_window(390, 200, window=enterbtn)

    LU_window.mainloop()
# def cramers():
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(ws)

#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("Cramers Rule")

#     # sets the geometry of toplevel
#     newWindow.geometry("700x450")

#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text="Cramers Rule").pack()
def gaus():
    # create window
    gauss_window = Tk()
    gauss_window.title('Gauss-Jordan Elimination Method')
    canvas1 = Canvas(gauss_window, width=800, height=400, relief='raised', bg=color)
    canvas1.pack()
    # create frane for user input
    matrixFrame = Frame(gauss_window)
    canvas1.create_window(400, 130, window=matrixFrame)
    # labels for entry
    label1 = Label(gauss_window, text='x1', fg=blue_color, bg = color)
    label1.config(font=(font_default, 12))
    canvas1.create_window(275, 75, window=label1)
    label2 = Label(gauss_window, text='x2', fg=blue_color, bg = color)
    label2.config(font=(font_default, 12))
    canvas1.create_window(360, 75, window=label2)
    label3 = Label(gauss_window, text='x3', fg=blue_color, bg = color)
    label3.config(font=(font_default, 12))
    canvas1.create_window(440, 75, window=label3)
    label4 = Label(gauss_window, text='b', fg=blue_color, bg = color)
    label4.config(font=(font_default, 12))
    canvas1.create_window(525, 75, window=label4)
    all_entries = []
    rows = 3
    cols = 4

    # creates grid view for matrix
    for r in range(rows):
        entries_row = []
        for c in range(cols):
            e = Entry(matrixFrame, width=8, bg=blue_color, fg=color,)  # 5 chars
            e.insert('end', 0)
            e.grid(row=r, column=c)
            entries_row.append(e)
        all_entries.append(entries_row)

    # gets input for user and insert it into matrix
    def enter():
        # fill matrix with 0
        matrix = np.zeros((rows, cols))
        # insert values in matrix
        for r, row in enumerate(all_entries):
            for c, entry in enumerate(row):
                text = entry.get()
                matrix[r, c] = float(text)
        # make the upper triangle = 0
        gmax = matrix
        for i in range(rows):
            if gmax[i, i] == 0.0:
                print("no")
            for j in range(rows):
                if i != j and i < j:
                    ratio = gmax[j, i] / gmax[i, i]
                    for k in range(cols):
                        gmax[j, k] = gmax[j, k] - ratio * gmax[i, k]
        # back sub and print result on screen
        x3 = gmax[2, 3] / gmax[2, 2]
        x2 = (gmax[1, 3] - (gmax[1, 2] * x3)) / gmax[1][1]
        x1 = (gmax[0, 3] - ((gmax[0, 1] * x2) + (gmax[0, 2] * x3))) / gmax[0, 0]
        result = " "
        result = ('  X1= %0.2f' % x1) + result + '\n'
        result = ('  X2= %0.2f' % x2) + result + '\n'
        result = ('  X3= %0.2f' % x3) + result
        label2 = Label(gauss_window, text='Answer', fg = red_color, bg = color)
        label2.config(font=(font, 13))
        canvas1.create_window(280, 270, window=label2)
        label1 = Label(gauss_window, text=result, bg=color, fg=blue_color)
        label1.config(font=(font, 10))
        canvas1.create_window(320, 300, window=label1)

    enterbtn = Button(gauss_window, text='Enter Matrix', command=enter, font=(font, 15), fg=blue_color, borderwidth=border, bg = color2)
    canvas1.create_window(390, 200, window=enterbtn)

    gauss_window.mainloop()

# Create container frame
container = Frame(ws)
container.place(relx=0.5, rely=0.5, anchor='center')
container.configure(background=color)

# Create label above the button
label_title = Label(container, text='Numerical Analysis Project', background=color, fg = red_color, font=(font, 35))
label_title.pack(padx=10, pady=90)

# Create "Let's Start" button
start_button = Button(
    container, text="Let's Start", relief=RAISED, font=(font, 22),
    background=color2, fg=blue_color, borderwidth=border, command=start
)
start_button.pack(padx=10, pady=10)

ws.mainloop()