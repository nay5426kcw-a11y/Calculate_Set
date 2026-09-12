from tkinter import *

root = Tk()
root.title("เครื่องคิดเลขจำนวนสมาชิกเซต")
root.geometry("500x700")
root.configure(bg="#2c3e50")
root.resizable(False, False)

num_vars = {
    1: StringVar(value=""),
    2: StringVar(value=""),
    3: StringVar(value=""),
    4: StringVar(value=""),
    5: StringVar(value=""),
    6: StringVar(value=""),
    7: StringVar(value=""),
    8: StringVar(value=""),
}

set_display = 1
result = ""
num_input = StringVar(value="n(A) = ")

na = nb = nc = nab = nac = nbc = nabc = naUbUc = 0

def show_display():
    global set_display
    labels = {
        1: "n(A)",
        2: "n(B)",
        3: "n(C)",
        4: "n(A∩B)",
        5: "n(A∩C)",
        6: "n(B∩C)",
        7: "n(A∩B∩C)",
        8: "n(AUBUC)",
        9: "กด '=' เพื่อคำนวณ"
    }
    
    if set_display == 9:
        num_input.set(labels[9])
    else:
        label = labels.get(set_display, "")#ถ้าไม่มีค่าที่เหมือนset_display ให้คือค่าเป็น""(ค่าว่าง)
        value = num_vars[set_display].get()
        if value == "":
            num_input.set(f"{label} = ")
        else:
            num_input.set(f"{label} = {value}")

def get_num():
    global set_display
    global na, nb, nc, nab, nac, nbc, nabc, naUbUc

    input_value = num_input.get()
    
    if input_value.startswith("n"):
        return
    
    if set_display in num_vars:
        num_vars[set_display].set(input_value)

        if input_value != "x":
            try:
                value = int(input_value)
                if set_display == 1: na = value
                elif set_display == 2: nb = value
                elif set_display == 3: nc = value
                elif set_display == 4: nab = value
                elif set_display == 5: nac = value
                elif set_display == 6: nbc = value
                elif set_display == 7: nabc = value
                elif set_display == 8: naUbUc = value
            except ValueError:
                pass 

def opt_display(operater):
    global set_display

    if num_input.get().startswith("Error"):
        return
    
    if operater == ">" and 9 > set_display >= 1:
        get_num()
        set_display += 1
        show_display()
    elif operater == "<" and 9 >= set_display > 1:
        get_num()
        set_display -= 1
        show_display()

def show_num(num):
    global result
    
    if num_input.get().startswith("Error"):
        return 
    
    if num_input.get().startswith("n") or num_input.get().startswith("E"):
        result = ""
    elif num == "x" and num_input.get() != "":
        result = "Error"
        num = ""
    elif num != "x" and num_input.get().startswith("x"):
        result = "Error"
        num = ""
    
    result += str(num)
    num_input.set(result)

def clear():
    global set_display

    if set_display in num_vars:
        num_vars[set_display].set("")

    num_input.set("")
    show_display()

def calculate():
    global result
    result = ""
    
    unknown_index = None
    unknown_count = 0
    
    for idx in range(1, 9):
        if num_vars[idx].get() == "x":
            unknown_count += 1
            unknown_index = idx
    
    if unknown_count == 0 or unknown_count > 1:
        result = "Error"
    elif unknown_index == 8:  
        result = na + nb + nc - nab - nac - nbc + nabc
    elif unknown_index == 7:  
        result = naUbUc - na - nb - nc + nab + nac + nbc
    elif unknown_index == 1:  
        result = naUbUc - nb - nc + nab + nac + nbc - nabc
    elif unknown_index == 2:  
        result = naUbUc - na - nc + nab + nac + nbc - nabc
    elif unknown_index == 3:  
        result = naUbUc - nb - na + nab + nac + nbc - nabc
    elif unknown_index == 4:  
        result = na + nb + nc - naUbUc - nac - nbc + nabc
    elif unknown_index == 5:  
        result = na + nb + nc - nab - naUbUc - nbc + nabc
    elif unknown_index == 6:  
        result = na + nb + nc - nab - nac - naUbUc + nabc
    
    num_input.set(result)
    
    

# bg
bg_area = Frame(
    root,
    bg="#ecf0f1",
    width=490,
    height=350
)
bg_area.place(x=5, y=350)

display = Entry(
    textvariable=num_input,
    font=("Arial", 40, "bold"),  
    justify="right",
    bg="#ecf0f1",  
    fg="#2c3e50",  
    relief="sunken",  
    borderwidth=3,
    state="readonly"  
    )
display.grid(
    row=0,
    column=0,
    padx=10,
    pady=15,
    columnspan=6,
    sticky="nsew"
    )

def create_display(textvariable, row, column):

    _ = Entry(
        textvariable=textvariable,
        font=('Arial', 18, 'bold'),
        justify="center",
        bg="#ffffff",
        fg="#2c3e50",
        relief="solid",
        borderwidth=2,
        state="readonly"  
    )
    _.grid(
        row=row,
        column=column,
        padx=8,
        pady=10,
        sticky="nsew"
    )

def create_lb(text, row, column):

    lb = Label(
        text=text,
        font=("Arial", 14, "bold"),
        bg="#34495e", 
        fg="#ecf0f1",  
        relief="flat"
    )
    lb.grid(
        row=row,
        column=column,
        columnspan=2,
        padx=8,
        pady=10,
        sticky="nsew"
    )
    
def create_btn(text, row, column, command, columnspan=1, rowspan=1, color="red"):

    color_map = {
        "red": ("#e74c3c", "#c0392b"),      
        "blue": ("#3498db", "#2980b9"),    
        "green": ("#27ae60", "#229954"),   
    }
    
    bg_color, active_color = color_map.get(color, ("#e74c3c", "#c0392b"))
    
    btn = Button(
        root,
        text=text,
        font=("Arial", 22, "bold"),
        command=command,
        bg=bg_color,
        fg="white",
        relief="raised",
        borderwidth=3,
        activebackground=active_color,
        activeforeground="white",
        cursor="hand2"  
    )
    btn.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        rowspan=rowspan,
        padx=6,
        pady=8,
        sticky="nsew"
    )

for colum in range(6):
    root.grid_columnconfigure(colum, weight=1, uniform="calculator")

for row in range(1, 9):
    root.grid_rowconfigure(row, weight=1)

#colum0-1
create_lb("n(A)", 1, 0)
create_lb("n(B)", 2, 0)
create_lb("n(C)", 3, 0)
create_lb("n(A∩B)", 4, 0)

#colum2
create_display(num_vars[1], 1, 2)
create_display(num_vars[2], 2, 2)
create_display(num_vars[3], 3, 2)
create_display(num_vars[4], 4, 2)

#colum3-4
create_lb("n(A∩C)", 1, 3)
create_lb("n(B∩C)", 2, 3)
create_lb("n(A∩B∩C)", 3, 3)
create_lb("n(AUBUC)", 4, 3)

#colum5
create_display(num_vars[5], 1, 5)
create_display(num_vars[6], 2, 5)
create_display(num_vars[7], 3, 5)
create_display(num_vars[8], 4, 5)
btn_equal = create_btn("=", 7, 4, lambda: calculate(), 1, 2, color="red")

#row5
btn7 = create_btn("7", 5, 1, lambda: show_num(7), color="green")
btn8 = create_btn("8", 5, 2, lambda: show_num(8), color="green")
btn9 = create_btn("9", 5, 3, lambda: show_num(9), color="green")
btn_c = create_btn("C", 5, 4, lambda: clear(), color="red")

#row6
btn4 = create_btn("4", 6, 1, lambda: show_num(4), color="green")
btn5 = create_btn("5", 6, 2, lambda: show_num(5), color="green")
btn6 = create_btn("6", 6, 3, lambda: show_num(6), color="green")
btn_x = create_btn("x", 6, 4, lambda: show_num("x"), color="red")

#row7
btn1 = create_btn("1", 7, 1, lambda: show_num(1), color="green")
btn2 = create_btn("2", 7, 2, lambda: show_num(2), color="green")
btn3 = create_btn("3", 7, 3, lambda: show_num(3), color="green")

#row8
btn_back = create_btn("◀", 8, 1, lambda: opt_display("<"), color="blue")
btn_0 = create_btn("0", 8, 2, lambda: show_num(0), color="green")
btn_next = create_btn("▶", 8, 3, lambda: opt_display(">"), color="blue")

root.mainloop()