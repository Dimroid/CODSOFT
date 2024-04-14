from tkinter import *
sumup = ''
result = ''
def btnEqualsInput():
    global coperator
    global sumup
    sumup = str(eval(coperator))
    coperator = sumup
    text_input.set(sumup)


def btnClick(numbers):
    global coperator
    text_input.set(result)
    coperator += str(numbers)
    #coperator = coperator
    text_input.set(coperator)


def btnClearDisplay():
    global coperator
    coperator = ''
    text_input.set("")

    
cal = Tk()
cal.title("Dimroid -- Calculator")

coperator = ''
text_input = StringVar()
#cal.resizable(False, False)

txtDisplay = Entry(cal, font = ('arial', 20, 'bold'),
                   textvariable = text_input, bd =20,
                   bg="powder blue", justify = "right").grid(columnspan = 4)


btn7 = Button(cal, padx=16, bd=8, fg = "black", pady = 16, bg = "powder blue",
              font = ('arial', 20, 'bold'), text = "7",
              command = lambda:btnClick(7)).grid(row = 1, column = 0)

btn8 = Button(cal, padx=16, bd=8, fg = "black", pady = 16, bg = "powder blue",
              font = ('arial', 20, 'bold'), text = "8",
              command = lambda:btnClick(8)).grid(row = 1, column = 1)

btn9 = Button(cal, padx=16, bd=8, fg = "black", pady = 16, bg = "powder blue",
              font = ('arial', 20, 'bold'), text = "9",
              command = lambda:btnClick(9)).grid(row = 1, column = 2)

addition = Button(cal, padx = 16, bd = 8, pady = 16, fg = "black",text = "+",
                  command = lambda:btnClick('+'),
                  font = ('arial', 19, 'bold'), bg = "powder blue",).grid(row = 1, column = 3)

#================================================================================

btn4 = Button(cal, padx=16, bd=8, fg = "black", pady = 16,
              justify = "center", bg = "powder blue",
              command = lambda:btnClick(4),
              font = ('arial', 20, 'bold'), text = "4").grid(row = 2, column = 0)


btn5 = Button(cal, padx=16, bd=8, fg = "black", pady = 16,
              justify = "center", bg = "powder blue",
              command = lambda:btnClick(5),
              font = ('arial', 20, 'bold'), text = "5").grid(row = 2, column = 1)

btn6 = Button(cal, padx=16, bd=8, fg = "black", pady = 16,
              justify = "center", bg = "powder blue",
              command = lambda:btnClick(6),
              font = ('arial', 20, 'bold'), text = "6").grid(row = 2, column = 2)

subtraction = Button(cal, padx = 16, bd = 8, pady = 16,
                     fg = "black",text = "-", bg = "powder blue",
                     command = lambda:btnClick('-'),
                     font = ('arial', 20, 'bold')).grid(row = 2, column = 3)


#================================================================================
btn3 =  Button(cal, padx=16, bd=8, fg = "black", pady = 16,
               justify = "center", bg = "powder blue",
               command = lambda:btnClick(3),
              font = ('arial', 20, 'bold'), text = "3").grid(row = 3, column = 0)


btn2 = Button(cal, padx=16, bd=8, fg = "black", pady = 16,
              justify = "center", bg = "powder blue",
              command = lambda:btnClick(2),
              font = ('arial', 20, 'bold'), text = "2").grid(row = 3, column = 1)

btn1 = Button(cal, padx=16, bd=8, fg = "black",pady = 16,
              justify = "center",bg = "powder blue",
              command = lambda:btnClick(1),
              font = ('arial', 20, 'bold'), text = "1").grid(row = 3, column = 2)

multiplication = Button(cal, padx = 16, bd = 8, pady = 16,
                    fg = "black",text = "*", bg = "powder blue",
                        command = lambda:btnClick('*'),
                  font = ('arial', 20, 'bold')).grid(row = 3, column = 3)


#================================================================================
btn0 =  Button(cal, padx=16, bd=8, fg = "black", pady = 16,
               justify = "center", bg = "powder blue",
               command = lambda:btnClick(0),
              font = ('arial', 20, 'bold'), text = "0").grid(row = 4, column = 0)


btnClear = Button(cal, padx=16, bd=8, pady = 16, fg = "black",
                  justify = "center", bg = "powder blue",
                  command = btnClearDisplay,
              font = ('arial', 19, 'bold'), text = "C").grid(row = 4, column = 1)

btnEquals = Button(cal, padx=16, bd=8, pady = 16, fg = "black",
                   justify = "center",bg = "powder blue",
                   command = btnEqualsInput,
              font = ('arial', 20, 'bold'), text = "=").grid(row = 4, column = 2)

Division = Button(cal, padx = 16, pady = 16, bd = 8,
                  fg = "black",text = "/", bg = "powder blue",
                  command = lambda:btnClick('/'),
                  font = ('arial', 20, 'bold')).grid(row = 4, column = 3)


#================================================================================



cal.mainloop()
