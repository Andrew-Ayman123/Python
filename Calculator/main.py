from calculator_button import CalcButton
from tkinter import Tk, Label, Button
import colors as Colors
screen = Tk()
screen.title('Calculator')
screen.config(bg=Colors.GREY)

output = Label(text='0.0', font=('Arial', 20),  pady=10,
               width=16, bg=Colors.GREY,fg=Colors.WHITE,anchor='e',wraplength=250,justify='right')
output.grid(row=0, column=0, columnspan=4)


output_value = ''

def calculator(val):
    global output_value
    try:
        if val == '=':
            output_value = output_value.replace('x', '*')
            output_value = output_value.replace('÷', '/')
            output_value = output_value.replace('π', '3.1416')
            if output_value=='':
                output_value='0.0'
            output_value = '{:e}'.format(eval(output_value))
            output.config(text=output_value)
            output_value = ''
        elif val=='c':
            output_value=''
            output.config(text=0.0)
        elif val =='ce':
            output_value=output_value[:-1] 
            if output_value =='':
                output.config(text='0.0')
            else:    
                output.config(text=output_value)
        else:    
            output_value += val
            output.config(text=output_value)
    except:
        output.config(text='Error 404')
        output_value = ''


BUTTONS: CalcButton = [

    CalcButton(value='0', row=5, column=0, columnspan=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('0')),

    CalcButton(value='.', row=5, column=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('.'),),

    CalcButton(value='=', row=5, column=3,
               bg_color=Colors.ORANGE, fg_color=Colors.WHITE,
               func=lambda: calculator('='),),

    CalcButton(value='1', row=4, column=0,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('1'),),

    CalcButton(value='2', row=4, column=1,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('2'),),

    CalcButton(value='3', row=4, column=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('3'),),

    CalcButton(value='+', row=4, column=3,
               bg_color=Colors.ORANGE, fg_color=Colors.WHITE,
               func=lambda: calculator('+'),),

    CalcButton(value='4', row=3, column=0,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('4'),),

    CalcButton(value='5', row=3, column=1,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('5'),),

    CalcButton(value='6', row=3, column=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('6'),),

    CalcButton(value='-', row=3, column=3,
               bg_color=Colors.ORANGE, fg_color=Colors.WHITE,
               func=lambda: calculator('-'),),

    CalcButton(value='7', row=2, column=0,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('7'),),

    CalcButton(value='8', row=2, column=1,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('8'),),

    CalcButton(value='9', row=2, column=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('9'),),

    CalcButton(value='X', row=2, column=3,
               bg_color=Colors.ORANGE, fg_color=Colors.WHITE,
               func=lambda: calculator('x'),),

    CalcButton(value='C', row=1, column=0,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('c'),),

    CalcButton(value='CE', row=1, column=1,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('ce'),),

    CalcButton(value='π', row=1, column=2,
               bg_color=Colors.OFFWHITE, fg_color=Colors.BLACK,
               func=lambda: calculator('π'),),

    CalcButton(value='÷', row=1, column=3,
               bg_color=Colors.ORANGE, fg_color=Colors.WHITE,
               func=lambda: calculator('÷'),),
 
]


screen.mainloop()
