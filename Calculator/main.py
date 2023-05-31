from tkinter import Tk, Label, Button
import re

class ConstColors:
    # Define some constant colors
    GREY = '#4c4c4c'
    ORANGE = '#ec9649'
    OFFWHITE = '#d5d5d5'
    BLACK = 'Black'
    WHITE = 'White'

class CalcButton:
    def __init__(self, value: str, row: int, column: int, bg_color: str, fg_color: str, func, rowspan: int = 1, columnspan: int = 1) -> None:
        # Initialize a button with given parameters
        Button(text=value,
               command=lambda: func(value),
               padx=5, pady=5,
               font=('Arial', 20),
               borderwidth=1,
               relief='raised',
               bg=bg_color,
               fg=fg_color,
               ).grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")

class MainProgram():
    def calculator(self, val):
        try:
            if val == '=':
                # Replace 'X' with '*' and handle numbers followed by 'π'
                self.outputText = self.outputText.replace('x', '*')
                self.outputText = self.outputText.replace('÷', '/')
                self.outputText = re.sub(
                    r'(\d+)(π)', r'\1*\2', self.outputText) # Handle numbers followed by 'π'
                self.outputText = re.sub(
                    r'(π)(\d+)', r'\1*\2', self.outputText) # Handle 'π' followed by numbers
                self.outputText = self.outputText.replace('π', '3.14')
                if self.outputText == '':
                    self.outputText = '0.0'
                output_res = eval(self.outputText)
                self.outputText = '{:.2f}'.format(output_res)
                self.output.config(text=self.outputText)
            elif val == 'C':
                # Clear the output text and set the output label to '0.0'
                self.outputText = ''
                self.output.config(text=0.0)
            elif val == 'CE':
                # Remove the last character from the output text and update the output label
                self.outputText = self.outputText[:-1]
                if self.outputText == '':
                    self.output.config(text='0.0')
                else:
                    self.output.config(text=self.outputText)
            else:
                # Append the value to the output text and update the output label
                self.outputText += val
                self.output.config(text=self.outputText)
        except Exception as e:
            # If there is an exception, set the output label to 'Error 404' and clear the output text
            print(e)
            self.output.config(text='Error404')
            self.outputText = ''

    def __init__(self) -> None:
        # Initialize the main program
        screen = Tk()
        screen.title('Calculator')
        screen.config(bg=ConstColors.GREY)

        # Initialize the output label and text
        self.output = Label(text='0.0', font=('Arial', 20),  pady=10,
                            width=16, bg=ConstColors.GREY, fg=ConstColors.WHITE, anchor='e', wraplength=250, justify='right')
        self.output.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.outputText = ""

        # Define the buttons and their properties
        BUTTONS_SYMBOLS = [
            ["C", "CE", "π", "÷"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "", ".", "="],
        ]
        BUTTONS_COLORS_BG = [ConstColors.OFFWHITE, ConstColors.OFFWHITE,
                             ConstColors.OFFWHITE, ConstColors.ORANGE]
        BUTTONS_COLORS_FG = [ConstColors.BLACK, ConstColors.BLACK,
                             ConstColors.BLACK, ConstColors.WHITE, ]

        # Add the buttons to the screen
        for i in range(1, 6):
            for j in range(4):
                # Skip empty buttons
                if(not BUTTONS_SYMBOLS[i-1][j]):
                    continue

                # Create a CalcButton object and add it to the screen
                CalcButton(value=BUTTONS_SYMBOLS[i-1][j], row=i, column=j,
                           columnspan=2 if (i == 5 and j == 0) else 1,
                           bg_color=BUTTONS_COLORS_BG[j], fg_color=BUTTONS_COLORS_FG[j],
                           func=self.calculator)

        # Configure the grid layout to resize properly
        for i in range(6):
            screen.grid_rowconfigure(i, weight=1)
            for j in range(4):
                screen.grid_columnconfigure(j, weight=1)

        # Start the main event loop
        screen.mainloop()

if __name__ == "__main__":
    MainProgram()