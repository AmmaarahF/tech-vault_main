import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import random
import string
import re

class BankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TechVault")
        self.master.geometry("500x400")
        self.master.configure(bg='teal')
        self.create_registration_gui()

    def create_registration_gui(self):
        heading = tk.Label(self.master, text="Welcome to TechVault\nYour #1 banking app", bg='teal', fg='white', font=("Arial", 16, "underline"))
        heading.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        self.label_username = tk.Label(self.master, text="Username:", bg='teal', fg='white', font=("Arial", 12))
        self.label_username.grid(row=1, column=0, padx=80, pady=10)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1)

        self.label_age = tk.Label(self.master, text="Age:", bg='teal', fg='white', font=("Arial", 12))
        self.label_age.grid(row=2, column=0, padx=10, pady=10)
        self.entry_age = tk.Entry(self.master)
        self.entry_age.grid(row=2, column=1)

        self.label_gender = tk.Label(self.master, text="Gender:", bg='teal', fg='white', font=("Arial", 12))
        self.label_gender.grid(row=3, column=0, padx=10, pady=10)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.radio_male = tk.Radiobutton(self.master, text="Male", variable=self.gender_var, value="Male", bg='teal',
                                         fg='black')
        self.radio_male.grid(row=3, column=1)
        self.radio_female = tk.Radiobutton(self.master, text="Female", variable=self.gender_var, value="Female",
                                           bg='teal', fg='black')
        self.radio_female.grid(row=3, column=2)

        self.label_email = tk.Label(self.master, text="Email:", bg='teal', fg='white', font=("Arial", 12))
        self.label_email.grid(row=4, column=0, padx=10, pady=10)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=4, column=1)

        self.register_button = tk.Button(self.master, text="Register", command=self.register_user)
        self.register_button.grid(row=5, column=0, columnspan=3, pady=10)

        self.login_button = tk.Button(self.master, text="Login", command=self.show_login_gui)
        self.login_button.grid(row=6, column=0, columnspan=3, pady=5)

    def show_login_gui(self):
        self.create_login_gui()

    def create_login_gui(self):
        for widget in self.master.winfo_children():
            widget.grid_forget()

        self.master.configure(bg='teal')

        heading = tk.Label(self.master, text="Login to TechVault", bg='teal', fg='white', font=("Arial", 16, "underline"))
        heading.grid(row=0, column=0, columnspan=2, padx=110, pady=10)

        self.label_username_login = tk.Label(self.master, text="Username:", bg='teal', fg='white', font=("Arial", 12))
        self.label_username_login.grid(row=1, column=0, padx=80, pady=10)
        self.entry_username_login = tk.Entry(self.master)
        self.entry_username_login.grid(row=1, column=1)

        self.label_password_login = tk.Label(self.master, text="Password:", bg='teal', fg='white', font=("Arial", 12))
        self.label_password_login.grid(row=2, column=0, padx=10, pady=10)
        self.entry_password_login = tk.Entry(self.master, show="*")
        self.entry_password_login.grid(row=2, column=1)

        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self.master, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.grid(row=3, columnspan=2, pady=5)

        self.login_button = tk.Button(self.master, text="Login", command=self.login_user)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=10)

    def toggle_password_visibility(self):
        show_password = self.show_password_var.get()
        self.entry_password_login.config(show="" if show_password else "*")    

    def register_user(self):
        username = self.entry_username.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        email = self.entry_email.get()

        if not (username and age and gender and email):
            messagebox.showerror("Error", "Please enter all the fields.")
            return

        if not age.isdigit():
            messagebox.showerror("Invalid Input", "Age must be a number.")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Input", "Invalid email format.")
            return

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        account_number = ''.join(random.choices(string.digits, k=8))


        with open("BankData.txt", "a") as file:
            file.write(f"Username: {username}, Age: {age}, Gender: {gender}, Email: {email}, Password: {password}, Account Number: {account_number}, Balance: R0.00\n")

        alert_msg = f"Registration Successful!\n\nUsername: {username}\nAge: {age}\nGender: {gender}\nEmail: {email}\nPassword: {password}\nAccount Number: {account_number}"
        messagebox.showinfo("Registration Successful", alert_msg)

        self.entry_username.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        self.create_login_gui()

        with open(f"{username}_TransactionLog.txt", "w") as transaction_file:
            pass  # Just to create an empty file if it doesn't exist

    def login_user(self):
        username = self.entry_username_login.get()
        password = self.entry_password_login.get()

        if self.show_password_var.get(): #check if the password should be shown
            messagebox.showinfo("Password", f"Your password is: {password}")
            return

        with open("BankData.txt", "r") as file:
            for line in file:
                if f"Username: {username}, " in line and f"Password: {password}, " in line:
                    self.username = username
                    self.balance = float(line.split(", Balance: R")[1])
                    self.create_transaction_gui()
                    return
        messagebox.showerror("Login Failed", "Invalid username or password.")

    def create_transaction_gui(self):
        for widget in self.master.winfo_children():
            widget.grid_forget()

        self.master.configure(bg='teal')

        self.label_balance = tk.Label(self.master, text=f"Balance: R{self.balance:.2f}", bg='teal', fg='white', font=("Arial", 12))
        self.label_balance.grid(row=0, column=0, padx=100, pady=10)

        self.transaction_button = tk.Button(self.master, text="Make a Transaction", command=self.prompt_transaction)
        self.transaction_button.grid(row=1, column=0, columnspan=2, padx=100, pady=10)

        self.bank_statement_button = tk.Button(self.master, text="Bank Statement", command=self.show_bank_statement)
        self.bank_statement_button.grid(row=2, column=0, columnspan=2, padx=100, pady=10)

    def prompt_transaction(self):
        self.transaction_window = tk.Toplevel(self.master)
        self.transaction_window.title("Transaction")
        self.transaction_window.configure(bg='teal')

        label = tk.Label(self.transaction_window, text="Choose transaction type:", bg='teal', fg='white', font=("Arial", 12))
        label.pack(pady=10)

        deposit_button = tk.Button(self.transaction_window, text="Deposit", command=self.deposit_gui)
        deposit_button.pack(pady=5)

        withdraw_button = tk.Button(self.transaction_window, text="Withdraw", command=self.withdraw_gui)
        withdraw_button.pack(pady=5)

    def deposit_gui(self):
        self.transaction_window.destroy()

        self.deposit_window = tk.Toplevel(self.master)
        self.deposit_window.title("Deposit")
        self.deposit_window.configure(bg='teal')

        label = tk.Label(self.deposit_window, text="Enter deposit amount:", bg='teal', fg='white', font=("Arial", 12))
        label.pack(pady=10)

        self.entry_deposit = tk.Entry(self.deposit_window)
        self.entry_deposit.pack(pady=5)

        deposit_button = tk.Button(self.deposit_window, text="Deposit", command=self.deposit)
        deposit_button.pack(pady=10)

    def withdraw_gui(self):
        self.transaction_window.destroy()

        self.withdraw_window = tk.Toplevel(self.master)
        self.withdraw_window.title("Withdraw")
        self.withdraw_window.configure(bg='teal')

        label = tk.Label(self.withdraw_window, text="Enter withdrawal amount:", bg='teal', fg='white', font=("Arial", 12))
        label.pack(pady=10)

        self.entry_withdraw = tk.Entry(self.withdraw_window)
        self.entry_withdraw.pack(pady=5)

        withdraw_button = tk.Button(self.withdraw_window, text="Withdraw", command=self.withdraw)
        withdraw_button.pack(pady=10)

    def deposit(self):
        try:
            amount = float(self.entry_deposit.get())
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.update_balance(amount)
            self.log_transaction(amount, "Deposit")
            self.deposit_window.destroy()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def withdraw(self):
        try:
            amount = float(self.entry_withdraw.get())
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.update_balance(-amount)
            self.log_transaction(amount, "Withdrawal")
            self.withdraw_window.destroy()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def update_balance(self, amount):
        with open("BankData.txt", "r+") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if f"Username: {self.username}, " in line:
                    data = line.strip().split(", ")
                    balance = float(data[5].split(": ")[1].replace("R", "").replace("$", ""))
                    new_balance = balance + amount
                    self.balance = new_balance
                    lines[i] = f"Username: {data[0].split(': ')[1]}, Age: {data[1].split(': ')[1]}, Gender: {data[2].split(': ')[1]}, Email: {data[3].split(': ')[1]}, Password: {data[4].split(': ')[1]}, Balance: R{new_balance:.2f}\n"
                    self.label_balance.config(text=f"Balance: R{new_balance:.2f}")
                    file.seek(0)
                    file.writelines(lines)
                    return

    def log_transaction(self, amount, transaction_type):
        now = datetime.datetime.now()
        # Append the transaction to the user's transaction log file
        with open(f"{self.username}_TransactionLog.txt", "a") as file:
            file.write(f"{now}: {transaction_type} of R{amount:.2f}\n")

    def show_bank_statement(self):
        try:
            # Read transactions from the logged-in user's transaction log file
            with open(f"{self.username}_TransactionLog.txt", "r") as file:
                statement = file.readlines()
            if statement:
                # Display the bank statement
                statement_window = tk.Toplevel(self.master)
                statement_window.title("Bank Statement")
                statement_window.configure(bg='teal')
                tree = ttk.Treeview(statement_window, columns=("Date", "Transaction Type", "Amount"), show="headings")
                tree.heading("Date", text="Date")
                tree.heading("Transaction Type", text="Transaction Type")
                tree.heading("Amount", text="Amount")
                for transaction in statement:
                    date, _, amount = transaction.partition(":")
                    tree.insert("", "end", values=(
                        date.strip(), "Deposit" if "Deposit" in transaction else "Withdrawal", amount.strip()))
                tree.pack(expand=True, fill="both")
            else:
                messagebox.showerror("Error", "No transactions found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No transactions found.")

root = tk.Tk()
banking_app = BankingApp(root)
root.mainloop()
