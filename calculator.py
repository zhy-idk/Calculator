import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x410")
        self.frames()
        self.display()
        self.keypad()
        self.value1 = ""
        self.value2 = ""
        self.operation="none"

        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

    def frames(self):
        self.entry_frame = ctk.CTkFrame(self, width=300)
        self.entry_frame.grid(row=0, column=0)
        self.button_frame = ctk.CTkFrame(self, width=300)
        self.button_frame.grid(row=1, column=0, pady=1, sticky="n")

    def display(self):
        self.textbox = ctk.CTkTextbox(
            master=self.entry_frame,
            corner_radius=10,
            border_width=3,
            width=300,
            height=100,
            font=("Cascadia Code SemiBold", 25)
        )
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.reset()
        self.textbox.configure(state="disabled")
        self.textbox.see("end")

    def keypad(self):
        clear = ctk.CTkButton(
            master=self.button_frame, text="C", width=72, height=60, command=self.clear
        )
        
        clear_last = ctk.CTkButton(
            master=self.button_frame,
            text="←",
            width=72,
            height=60,
            command=self.clear_last,
        )

        divide = ctk.CTkButton(master=self.button_frame, text="/", width=72, height=60, command=lambda: self.operator("/"))
        multiply = ctk.CTkButton(
            master=self.button_frame, text="*", width=72, height=60, command=lambda: self.operator("*")
        )
        minus = ctk.CTkButton(master=self.button_frame, text="-", width=72, height=60, command=lambda: self.operator("-"))
        plus = ctk.CTkButton(master=self.button_frame, text="+", width=72, height=60, command=lambda: self.operator("+"))
        enter = ctk.CTkButton(
            master=self.button_frame, text="Enter", width=72, height=121, command = self.enter
        )

        btn_seven = ctk.CTkButton(
            master=self.button_frame,
            text="7",
            width=72,
            height=60,
            command=lambda: self.click(7),
        )

        btn_eight = ctk.CTkButton(
            master=self.button_frame,
            text="8",
            width=72,
            height=60,
            command=lambda: self.click(8),
        )

        btn_nine = ctk.CTkButton(
            master=self.button_frame,
            text="9",
            width=72,
            height=60,
            command=lambda: self.click(9),
        )

        btn_four = ctk.CTkButton(
            master=self.button_frame,
            text="4",
            width=72,
            height=60,
            command=lambda: self.click(4),
        )
        
        btn_five = ctk.CTkButton(
            master=self.button_frame,
            text="5",
            width=72,
            height=60,
            command=lambda: self.click(5),
        )

        btn_six = ctk.CTkButton(
            master=self.button_frame,
            text="6",
            width=72,
            height=60,
            command=lambda: self.click(6),
        )

        btn_one = ctk.CTkButton(
            master=self.button_frame,
            text="1",
            width=72,
            height=60,
            command=lambda: self.click(1),
        )

        btn_two = ctk.CTkButton(
            master=self.button_frame,
            text="2",
            width=72,
            height=60,
            command=lambda: self.click(2),
        )

        btn_three = ctk.CTkButton(
            master=self.button_frame,
            text="3",
            width=72,
            height=60,
            command=lambda: self.click(3),
        )

        btn_zero = ctk.CTkButton(
            master=self.button_frame,
            text="0",
            width=144,
            height=60,
            command=lambda: self.click(0),
        )

        decimal = ctk.CTkButton(master=self.button_frame, text=".", width=72, height=60, command=self.decimal)

        clear.grid(row=0, column=0, padx=1, pady=1)
        clear_last.grid(row=0, column=1, padx=1, pady=1)
        divide.grid(row=0, column=2, padx=1, pady=1)
        multiply.grid(row=0, column=3, padx=1, pady=1)
        minus.grid(row=1, column=3, padx=1, pady=1)
        plus.grid(row=2, column=3, padx=1, pady=1)
        enter.grid(row=3, column=3, rowspan=2, padx=1, pady=1)

        btn_seven.grid(row=1, column=0, padx=1, pady=1)
        btn_eight.grid(row=1, column=1, padx=1, pady=1)
        btn_nine.grid(row=1, column=2, padx=1, pady=1)

        btn_four.grid(row=2, column=0, padx=1, pady=1)
        btn_five.grid(row=2, column=1, padx=1, pady=1)
        btn_six.grid(row=2, column=2, padx=1, pady=1)

        btn_one.grid(row=3, column=0, padx=1, pady=1)
        btn_two.grid(row=3, column=1, padx=1, pady=1)
        btn_three.grid(row=3, column=2, padx=1, pady=1)

        btn_zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        decimal.grid(row=4, column=2, padx=1, pady=1)
    
    def reset(self):
        self.textbox.insert("end-1c", "0")

    def decimal(self):
        self.textbox.configure(state="normal")

        if self.operation == "none":
            if "." not in self.value1:
                self.value1 += "."
                self.textbox.insert("end-1c", ".")
        else:
            if "." not in self.value2:
                if self.value2 == "":
                    self.reset()
                    self.value2 += "."
                    self.textbox.insert("end-1c", ".")

        self.textbox.configure(state="disabled")

    def click(self, number):
        self.textbox.configure(state="normal")

        if self.operation == "none":
            if self.value1 == "":
                if number != 0:
                    self.textbox.delete("end-2c")

                self.value1 += str(number)
                self.textbox.insert("end-1c", str(number))

        else:
            if self.value2 == "":
                if number == 0:
                    self.textbox.delete("end-2c")

                self.value2 += str(number)
                self.textbox.insert("end-1c", str(number))

        
        self.textbox.configure(state="disabled")

    def clear_last(self):
        self.textbox.configure(state="normal")
        last_content = self.textbox.get("end-2c", "end-1c")
        content = self.textbox.get("1.0", tk.END)
        if last_content == " ":
            self.textbox.delete("end-2c")
            self.textbox.delete("end-2c")
            self.textbox.delete("end-2c")
            self.operation = "none"
            self.value2 = ""
        else:
            self.textbox.delete("end-2c")
            if content == " ":
                self.value1 = ""
                self.reset()
        self.textbox.configure(state="disabled")

    def clear(self):
        self.operation = "none"
        self.value1 = ""
        self.value2 = ""
        self.textbox.configure(state="normal")
        self.textbox.delete(0.0, "end-1c")
        self.reset()
        self.textbox.configure(state="disabled")

    def operator(self, operator):
        content = self.textbox.get("1.0", tk.END)
        found_operator = ""
        find_array = ["+","-","*","/"]
        self.textbox.configure(state="normal")

        for i in find_array:
            if content.find(i) > -1 and content.find(i) != 0:
                found_operator += i

        if self.value2 == "":
            if found_operator != "":
                self.textbox.delete("end-2c")
                self.textbox.delete("end-2c")
                self.textbox.delete("end-2c")
        else:
            self.enter()
            self.textbox.configure(state="normal")

        self.textbox.insert("end-1c", " ")
        self.textbox.insert("end-1c", str(operator))
        self.textbox.insert("end-1c", " ")
        
        self.textbox.configure(state="disabled")
        self.operation = operator
        
    def enter(self):
        self.test()
        if self.value1.isdecimal() == False:
            self.value1 = float(self.value1)
        else:
            self.value1 = int(self.value1)

        if self.value2.isdecimal() == False:
            self.value2 = float(self.value2)
        else:
            self.value2 = int(self.value2)

        x = self.value1
        y = self.value2
        z = 0

        self.textbox.configure(state="normal")
        self.textbox.delete(0.0, "end-1c")

        if self.operation == "+":
            z = x + y
            z = 0 if z == 0 else z
            self.textbox.insert("end-1c", z)
        elif self.operation == "-":
            z = x - y
            z = 0 if z == 0 else z
            self.textbox.insert("end-1c", z)
        elif self.operation == "*":
            z = x * y
            z = 0 if z == 0 else z
            self.textbox.insert("end-1c", z)
        elif self.operation == "/":
            z = x / y
            z = 0 if z == 0 else z
            self.textbox.insert("end-1c", z)

        self.value1 = str(z)
        self.value2 = ""
        self.operation = "none"

        self.textbox.configure(state="disabled")
        
    def test(self):
        print(self.value1)
        print(self.value2)

if __name__ == "__main__":
    Calculator().mainloop()