from tkinter import Button


class CalcButton:
    def __init__(self, value: str, row: int, column: int, bg_color: str, fg_color: str, func, rowspan: int = 1, columnspan: int = 1) -> None:
        Button(text=value,
               command=func,
               padx=5, pady=5,
               width=3 if columnspan < 2 else 7, height=1*rowspan,
               font=('Arial', 20),
               borderwidth=1,
               relief='raised',
               bg=bg_color,
               fg=fg_color,
               ).grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
