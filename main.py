import tkinter as tk

calculation = ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete("1.0", "end")
    textResult.insert("1.0", calculation)

def evaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete("1.0", "end")
        textResult.insert("1.0", calculation)
    except:
        clearField()
        textResult.insert("1.0", "Error")

def clearField():
    global calculation
    calculation = ""
    textResult.delete("1.0", "end")

# Graphical user interface
root = tk.Tk()
root.geometry("300x430")
root.title("Calculator")

textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=5, pady=10)

button_config = {
    "height": 2,
    "width": 3,
    "font": ("Arial", 14),
    "bd": 0,
    "relief": "ridge",
}

# Button symbols and their grid positions
button_symbols = {
    "1": (2, 1),
    "2": (2, 2),
    "3": (2, 3),
    "4": (3, 1),
    "5": (3, 2),
    "6": (3, 3),
    "7": (4, 1),
    "8": (4, 2),
    "9": (4, 3),
    "0": (5, 2),
    "+": (2, 4),
    "-": (3, 4),
    "*": (4, 4),
    "/": (5, 4),
    "(": (5, 1),
    ")": (5, 3),
}

# Create and place the buttons
for symbol, (row, column) in button_symbols.items():
    btn = tk.Button(root, text=symbol, command=lambda symbol=symbol: addToCalculation(symbol), **button_config)
    btn.grid(row=row, column=column, padx=5, pady=5)

# Equal button
btn_equals = tk.Button(root, text="=", command=evaluateCalculation, **button_config)
btn_equals.grid(row=6, column=3, columnspan=2)

# Clear button
btn_clear = tk.Button(root, text="C", command=clearField, width=11, font=("Arial", 14), bd=0, relief="ridge")
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
