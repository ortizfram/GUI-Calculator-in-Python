import tkinter as tk

calculation = ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def evaluateCalculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textResult.delete(1.0,"end")
        textResult.insert(1.0,"end")
    except:

def clearField():
    pass


# Graphical user interface
root = tk.Tk()
root.geometry("300x275")

textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=5)
root.mainloop()