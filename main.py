from tkinter import *

def button_clicked():
    if input.get() != "":
        kmratio = 1.60934
        kmvalue = float(kmratio) * float(input.get())
        lblKmValue["text"] = "%0.2f" % kmvalue


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
#window.minsize(width=300, height=200)

# Label
lblMileLbl = Label(text="Miles", padx=10, pady=10)
lblMileLbl.grid(column=2, row=0)

# Label
lblIsEqual = Label(text="is equal to", padx=10, pady=10)
lblIsEqual.grid(column=0, row=1)

# Label
lblKmValue = Label(text="0", padx=10, pady=10)
lblKmValue.grid(column=1, row=1)

# Label
lblKmLbl = Label(text="Km", padx=10, pady=10)
lblKmLbl.grid(column=2, row=1)

# Button
btnCalculate = Button(text="Calculate", command=button_clicked)
btnCalculate.grid(column=1, row=2)

#Entry
input = Entry()
input.grid(column=1, row=0)

window.mainloop()

