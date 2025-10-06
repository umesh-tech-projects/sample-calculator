import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        # Bring window to front briefly to avoid appearing behind others
        self.root.attributes('-topmost', True)
        self.root.after(0, lambda: self.root.attributes('-topmost', False))
        
        # Variables
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.operator = ""
        self.result = False
        self.memory = 0
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()

        # Show any tkinter callback exceptions in a dialog instead of silently closing
        def _show_callback_exception(exc, val, tb):
            messagebox.showerror("Unexpected Error", f"{exc.__name__}: {val}")
        self.root.report_callback_exception = _show_callback_exception
        
        # Create display frame
        self.display_frame = tk.Frame(self.root, bg='#2c3e50', height=100)
        self.display_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Display label
        self.display = tk.Label(
            self.display_frame,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#2c3e50',
            fg='white',
            anchor='e',
            padx=20
        )
        self.display.pack(fill=tk.BOTH, expand=True)
        
        # Create button frame
        self.button_frame = tk.Frame(self.root, bg='#34495e')
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button configuration
        self.button_config = {
            'font': ('Arial', 16, 'bold'),
            'relief': 'raised',
            'bd': 2,
            'width': 6,
            'height': 2
        }
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', 'MC']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '=' and j == 2:  # The actual = button
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        command=lambda t=text: self.button_click(t),
                        bg='#e74c3c',
                        fg='white',
                        **self.button_config
                    )
                elif text == 'MC':  # Memory Clear button
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        command=lambda t=text: self.button_click(t),
                        bg='#9b59b6',
                        fg='white',
                        **self.button_config
                    )
                elif text in ['÷', '×', '−', '+']:
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        command=lambda t=text: self.button_click(t),
                        bg='#f39c12',
                        fg='white',
                        **self.button_config
                    )
                elif text in ['C', '±', '%']:
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        command=lambda t=text: self.button_click(t),
                        bg='#95a5a6',
                        fg='white',
                        **self.button_config
                    )
                else:
                    btn = tk.Button(
                        self.button_frame,
                        text=text,
                        command=lambda t=text: self.button_click(t),
                        bg='#ecf0f1',
                        fg='black',
                        **self.button_config
                    )
                
                btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, char):
        if char.isdigit():
            self.number_press(char)
        elif char == '.':
            self.decimal_press()
        elif char in ['÷', '×', '−', '+']:
            self.operator_press(char)
        elif char == '=':
            self.equals_press()
        elif char == 'C':
            self.clear()
        elif char == '±':
            self.plus_minus()
        elif char == '%':
            self.percentage()
        elif char == 'MC':
            self.memory_clear()
    
    def number_press(self, num):
        if self.result:
            self.current = "0"
            self.result = False
        
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        
        self.update_display()
    
    def decimal_press(self):
        if self.result:
            self.current = "0"
            self.result = False
        
        if "." not in self.current:
            self.current += "."
            self.update_display()
    
    def operator_press(self, op):
        if self.operator and not self.result:
            self.equals_press()
        
        self.total = float(self.current)
        self.operator = op
        self.current = "0"  # Reset current number for next input
        self.input_value = True
        self.result = False
    
    def equals_press(self):
        if self.operator and not self.result:
            try:
                if self.operator == '+':
                    self.total += float(self.current)
                elif self.operator == '−':
                    self.total -= float(self.current)
                elif self.operator == '×':
                    self.total *= float(self.current)
                elif self.operator == '÷':
                    if float(self.current) == 0:
                        self.current = "Error"
                        self.update_display()
                        return
                    self.total /= float(self.current)
                
                # Format result to remove unnecessary decimal places
                if self.total == int(self.total):
                    self.current = str(int(self.total))
                else:
                    self.current = str(self.total)
                self.operator = ""
                self.input_value = True
                self.result = True
                self.update_display()
            except:
                self.current = "Error"
                self.update_display()
    
    def clear(self):
        self.current = "0"
        self.total = 0
        self.operator = ""
        self.input_value = True
        self.result = False
        self.update_display()
    
    def plus_minus(self):
        if self.current != "0" and self.current != "Error":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
    
    def percentage(self):
        try:
            self.current = str(float(self.current) / 100)
            self.update_display()
        except:
            self.current = "Error"
            self.update_display()
    
    def update_display(self):
        # Format the display text
        display_text = self.current
        if len(display_text) > 12:
            display_text = display_text[:12]
        
        self.display.config(text=display_text)
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        
        if key.isdigit():
            self.number_press(key)
        elif key == '.':
            self.decimal_press()
        elif key in ['+', '-', '*', '/']:
            # Convert keyboard symbols to display symbols
            symbol_map = {'+': '+', '-': '−', '*': '×', '/': '÷'}
            self.operator_press(symbol_map[key])
        elif key == '=' or event.keysym == 'Return':
            self.equals_press()
        elif key.lower() == 'c':
            self.clear()
        elif key == '\r':  # Enter key
            self.equals_press()
        elif event.keysym == 'Escape':
            self.clear()
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.current = "0"
        self.update_display()

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
