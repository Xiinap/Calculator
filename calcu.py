'''
Please, check README.txt
'''

from tkinter import *
#tkinter importing
from decimal import *
#decimal importing

root = Tk()
root.title('Calculator')
#creating window

buttons = (('7', '8', '9', '/', '4'), #button names
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []

#Result Calculation

def calculate(): #make function 'calculate' for result calculation
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+': #action - plus
        result = operand1 + operand2 #performing an operation
    if operation == '-': #action - minus
        result = operand1 - operand2 #performing an operation
    if operation == '/': #action - division
        result = operand1 / operand2 #performing an operation
    if operation == '*': #action - multiplication
        result = operand1 * operand2 #performing an operation
    label.configure(text=str(result)) #text

#Click handling

def click(text):
    global activeStr
    global stack
    if text == 'CE': #if you press 'CE' button
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9': #if you press button 0 to 9
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.': #if you press '.' button
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else: # if you press '=' button
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

#Appearance

label = Label(root, text='0', width=35)
#The inscription has a width of 35, in order to draw up protocols under the record
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE',
                command=lambda text='CE': click(text)) #button
button.grid(row=1,
            column=3,
            sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
                #In order for the buttons to work correctly, we had to create our own function for each of the buttons using lambda
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop() #widow mainloop
