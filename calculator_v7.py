import tkinter as tk

def on_button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + char)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x)
    if button == "=":
        action = calculate
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear).grid(row=row_val, column=col_val)

root.mainloop()
