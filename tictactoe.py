from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

clicked = True
count = 0

# Reset function
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count

    clicked = True
    count = 0

    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for b in buttons:
        b.config(text=" ", state=NORMAL, bg="SystemButtonFace")

# Disable all buttons
def disable_all():
    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for b in buttons:
        b.config(state=DISABLED)

# Check winner
def checkwinner():
    global winner
    winner = False

    # Winning combinations
    wins = [
        (b1,b2,b3),(b4,b5,b6),(b7,b8,b9),  # rows
        (b1,b4,b7),(b2,b5,b8),(b3,b6,b9),  # columns
        (b1,b5,b9),(b3,b5,b7)              # diagonals
    ]

    for combo in wins:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != " ":
            for b in combo:
                b.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"{combo[0]['text']} Wins!")
            disable_all()
            return

    global count
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")

# Button click
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        checkwinner()

    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwinner()

    else:
        messagebox.showerror("Error", "Already Selected!")

# Buttons
b1 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, command=lambda: b_click(b9))

# Grid
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

# Menu
menu = Menu(root)
root.config(menu=menu)

options = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=reset)

root.mainloop()