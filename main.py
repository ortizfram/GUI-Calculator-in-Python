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
        calculation = str(eval(calculation))
        calculation = ""
        textResult.delete(1.0,"end")
        textResult.insert(1.0,calculation)
    except:
        clearField()
        textResult.insert(1.0,"Error")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


# Graphical user interface
root = tk.Tk()
root.geometry("300x275")

textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=5)

# lambda refers to a function that does this if called
btn_1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Arial",14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Arial",14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Arial",14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Arial",14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Arial",14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Arial",14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Arial",14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Arial",14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Arial",14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Arial",14))
btn_0.grid(row=5, column=2)
root.mainloop()