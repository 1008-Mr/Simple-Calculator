import tkinter as tk
from tkinter import messagebox
from tkinter.constants import SUNKEN

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        # Create the main frame
        self.frame = tk.Frame(master=self.window, bg='lightgray', padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the entry widget for displaying the input and results
        self.entry = tk.Entry(master=self.frame, relief=SUNKEN, borderwidth=3, width=30, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

        # Define buttons and their positions
        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create and place buttons
        for (text, row, col) in self.buttons:
            button = tk.Button(
                master=self.frame, text=text, padx=15, pady=10, width=5,
                font=('Arial', 12), command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, pady=5, padx=5)

    def on_button_click(self, text):
        """Handles button clicks."""
        if text == '=':
            self.calculate_result()
        elif text == 'C':
            self.clear_entry()
        else:
            self.entry.insert(tk.END, text)

    def calculate_result(self):
        """Evaluates the expression in the entry widget."""
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")

    def clear_entry(self):
        """Clears the entry widget."""
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    calculator = Calculator(window)
    window.mainloop()
