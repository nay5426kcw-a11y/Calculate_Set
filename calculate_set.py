from tkinter import *

root = Tk()
root.title("เครื่องคิดเลขจำนวนสมาชิกเซต")
root.geometry("400x600")
root.configure(bg="black")
root.resizable(False,False)

set_display = 1
result = ""
num_input = StringVar(value="n(A) = ")
num_na = StringVar(value="")
num_nb = StringVar(value="")
num_nc = StringVar(value="")
num_nab = StringVar(value="")
num_nac = StringVar(value="")
num_nbc = StringVar(value="")
num_nabc = StringVar(value="")
num_aUbUc = StringVar(value="")

def check_nset():
    global set_display
    match set_display:
        case 1:
            num_input.set("n(A) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 2:
            num_input.set("n(B) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 3:
            num_input.set("n(C) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 4:
            num_input.set("n(A∩B) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 5:
            num_input.set("n(A∩C) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 6:
            num_input.set("n(B∩C) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 7:
            num_input.set("n(A∩B∩C) = ")
            num_input.set(num_input.get())
            return num_input.get()
        case 8:
            num_input.set("n(AUBUC) = ")
            num_input.set(num_input.get())
            return num_input.get()

def get_num():
    global set_display
    if num_input.get().startswith("n"):
        return
    match set_display:
        case 1:
            num_na.set(num_input.get())
        case 2:
            num_nb.set(num_input.get())
        case 3:
            num_nc.set(num_input.get())
        case 4:
            num_nab.set(num_input.get())
        case 5:
            num_nac.set(num_input.get())
        case 6:
            num_nbc.set(num_input.get())
        case 7:
            num_nabc.set(num_input.get())
        case 8:
            num_aUbUc.set(num_input.get())

def show_display(operater):
    global set_display
    if operater == ">" and 8 > set_display >= 1:
        get_num()
        set_display += 1
        check_nset()
    elif operater == "<" and 8 >= set_display > 1:
        get_num()
        set_display -= 1
        check_nset()
    else:
        set_display == set_display

def show_num(num):
    global result
    result += str(num)
    num_input.set(result)

def clear():
    global result
    result = ""#น่าจะต้องทำเครียทีละอันเลย
    num_input.set(result)

# bg
bg_area = Frame(
    root,
    bg="gray",
    width=390,
    height=300
)
bg_area.place(x=5, y=310)

display = Entry(
    textvariable=num_input,
    font=("Arial", 30, "bold"),
    justify="right",
    bg="#ffffff"
    )
display.grid(
    row=0,
    column=0,
    padx=5,
    pady=10,
    columnspan=6,
    sticky="nsew"
    )

def create_display(textvariable, row, column):
    ax = Entry(
        textvariable=textvariable,
        font=('Arial',20)
        )
    ax.grid(
        row=row,
        column=column,
        padx=5,
        pady=10,
        sticky="nsew"
        )

def create_lb(text, row, column):
    lb = Label(
        text=text,
        font=("Arial", 15),
        bg="gray"
    )
    lb.grid(
        row=row,
        column=column,
        columnspan=2,
        padx=5,
        pady=10,
        sticky="nsew"
    )
    

def create_btn(text, row, column, command, columnspan=1, color="red"):
    btn = Button(
        root,
        text=text,
        font=("Arial",20),
        command=command,
        bg=color,
        fg="white"
    )
    btn.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        padx=5,
        pady=5,
        sticky="nsew"
    )

for colum in range(6):
    root.grid_columnconfigure(colum, weight=1, uniform="calculator")

for row in range(1,9):
    root.grid_rowconfigure(row,weight=1)

#colum0-1
lb_na = create_lb("n(A)",1,0)
lb_nb = create_lb("n(B)",2,0)
lb_nc = create_lb("n(C)",3,0)
lb_nab = create_lb("n(A∩B)",4,0)

#colum2
na = create_display(num_na,1,2)
nb = create_display(num_nb,2,2)
nc = create_display(num_nc,3,2)
nab = create_display(num_nab,4,2)

#colum3-4
lb_nac = create_lb("n(A∩C)",1,3)
lb_nbc = create_lb("n(B∩C)",2,3)
lb_nabc = create_lb("n(A∩B∩C)",3,3)
lb_naUbUc = create_lb("n(AUBUC)",4,3)

#colum5
nac = create_display(num_nac,1,5)
nbc = create_display(num_nbc,2,5)
nabc = create_display(num_nabc,3,5)
naUbUc = create_display(num_aUbUc,4,5)

#row5
btn7 = create_btn("7",5,1,lambda: show_num(7))
btn8 = create_btn("8",5,2,lambda: show_num(8))
btn9 = create_btn("9",5,3,lambda: show_num(9))
btn_c = create_btn("c",5,4,lambda: clear())

#row6
btn4 = create_btn("4",6,1,lambda: show_num(4))
btn5 = create_btn("5",6,2,lambda: show_num(5))
btn6 = create_btn("6",6,3,lambda: show_num(6))
btn_x = create_btn("x",6,4,lambda: show_num("x"))

#row7
btn1 = create_btn("1",7,1,lambda: show_num(1))
btn2 = create_btn("2",7,2,lambda: show_num(2))
btn3 = create_btn("3",7,3,lambda: show_num(3))
btn_next = create_btn(">",7,4,lambda: show_display(">"))

#row8
btn_equal = create_btn("=",8,1,lambda: show_num("="),3)
btn_back = create_btn("<",8,4,lambda: show_display("<"))

root.mainloop()