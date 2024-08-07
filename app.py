import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import datetime
import random
import string
import re
from PIL import Image, ImageTk


class BankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TechVault")
        self.master.geometry("450x520")
        self.master.configure(bg='teal')
        self.create_registration_gui()
        self.master.resizable(False, False)
        
    def clear_gui(self):
        for widget in self.master.winfo_children():
            widget.destroy()    

    def create_registration_gui(self):
        self.clear_gui()
        self.master.geometry("450x520")
        self.master.resizable(False, False)

        container_frame = tk.Frame(self.master, bg='#D9D9D9', bd=2, relief='solid')
        container_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=500)

        image = Image.open("images/logo.png")
        self.logo_image = ImageTk.PhotoImage(image)

        self.logo_placeholder = tk.Label(self.master, image=self.logo_image, bg='#D9D9D9')
        self.logo_placeholder.grid(row=0, column=0, columnspan=3, pady=(40, 0), sticky='n')

        heading = tk.Label(self.master, text="Welcome to TechVault\nYour #1 banking app", bg='#D9D9D9', fg='teal',
                           font=("Arial", 12, "bold"))
        heading.grid(row=1, column=0, columnspan=3, pady=(5, 10), sticky='n')

        self.label_username = tk.Label(self.master, text="Username:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_username.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=2, column=1, sticky='w')

        self.label_age = tk.Label(self.master, text="Age:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_age.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.entry_age = tk.Entry(self.master)
        self.entry_age.grid(row=3, column=1, sticky='w')

        self.label_gender = tk.Label(self.master, text="Gender:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_gender.grid(row=4, column=0, padx=10, pady=10, sticky='e')


        gender_frame = tk.Frame(self.master, bg='#D9D9D9')
        gender_frame.grid(row=4, column=1, columnspan=2, sticky='w')

        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.radio_male = tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male", bg='#D9D9D9',
                                         fg='teal')
        self.radio_male.pack(side='left')
        self.radio_female = tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female",
                                           bg='#D9D9D9', fg='teal')
        self.radio_female.pack(side='left', padx=(10, 0))

        self.label_email = tk.Label(self.master, text="Email:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_email.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=5, column=1, sticky='w')
        
        self.label_account_type = tk.Label(self.master, text="Account Type:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_account_type.grid(row=6, column=0, padx=10, pady=10, sticky='e')

        self.account_type_var = tk.StringVar()
        self.account_type_var.set("Savings")
        self.account_type_menu = ttk.Combobox(self.master, textvariable=self.account_type_var, values=["Savings", "Checking", "Business"])
        self.account_type_menu.grid(row=6, column=1, sticky='w')


        button_frame = tk.Frame(self.master, bg='#D9D9D9')
        button_frame.grid(row=7, column=0, columnspan=3, pady=10)

        self.register_button = tk.Button(button_frame, text="Register", command=self.register_user)
        self.register_button.pack(side='left', padx=10)

        self.login_button = tk.Button(button_frame, text="Login", command=self.show_login_gui)
        self.login_button.pack(side='left', padx=10)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def show_login_gui(self):
        self.create_login_gui()
        self.master.resizable(False, False)

    def create_login_gui(self):
        self.clear_gui()
        self.master.resizable(False, False)

        self.master.configure(bg='teal')

        image = Image.open("images/logo.png")
        self.logo_image = ImageTk.PhotoImage(image)
        self.logo_placeholder = tk.Label(self.master, image=self.logo_image, bg='#D9D9D9')
        self.logo_placeholder.grid(row=0, column=0, columnspan=3, pady=(40, 0), sticky='n')

        heading = tk.Label(self.master, text="Login to TechVault", bg='#D9D9D9', fg='teal',
                           font=("Arial", 16, "bold"))
        heading.grid(row=1, column=0, columnspan=2, padx=110, pady=10)

        self.label_username_login = tk.Label(self.master, text="Username:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_username_login.grid(row=2, column=0, padx=(10, 2), pady=10, sticky='e')
        self.entry_username_login = tk.Entry(self.master)
        self.entry_username_login.grid(row=2, column=1, padx=(2, 50))

        self.label_password_login = tk.Label(self.master, text="Password:", bg='#D9D9D9', fg='teal', font=("Arial", 12))
        self.label_password_login.grid(row=3, column=0, padx=(10, 2), pady=10, sticky='e')
        self.entry_password_login = tk.Entry(self.master, show="*")
        self.entry_password_login.grid(row=3, column=1, padx=(2, 50))

        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self.master, text="Show Password", variable=self.show_password_var,
                                                     command=self.toggle_password_visibility)
        self.show_password_checkbox.grid(row=4, column=0, columnspan=2, pady=5)

        button_frame = tk.Frame(self.master, bg='#D9D9D9')
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        self.login_button = tk.Button(button_frame, text="Login", command=self.login_user)
        self.login_button.pack(side='left', padx=10)

        self.back_button = tk.Button(button_frame, text="Back", command=self.create_registration_gui)
        self.back_button.pack(side='left', padx=10)


        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def toggle_password_visibility(self):
        show_password = self.show_password_var.get()
        self.entry_password_login.config(show="" if show_password else "*")

    def register_user(self):
        username = self.entry_username.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        email = self.entry_email.get()
        account_type = self.account_type_var.get()
        

        if not (username and age and gender and email and account_type):
            messagebox.showerror("Error", "Please enter all the fields.")
            return

        if not age.isdigit():
            messagebox.showerror("Invalid Input", "Age must be a number.")
            return

        if int(age) < 18:
            messagebox.showerror("Invalid Input", "You must be 18 or older to register.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Input", "Invalid email format.")
            return

        account_number = ''.join(random.choices(string.digits, k=8))
        special_characters = '#!@$%^&*()'
        password = ''.join(random.choices(string.ascii_letters + string.digits + special_characters, k=12))

        with open("BankData.txt", "a") as file:
            file.write(
                f"Username: {username}, Age: {age}, Gender: {gender}, Email: {email}, Account Number: {account_number}, Password: {password}, Balance: R0.00\n")

        alert_msg = f"Registration Successful!\n\nUsername: {username}\nAge: {age}\nGender: {gender}\nEmail: {email}\nAccount Number: {account_number}\nPassword: {password}"
        messagebox.showinfo("Registration Successful", alert_msg)

        self.entry_username.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        self.create_login_gui()

        with open(f"{username}_TransactionLog.txt", "w") as transaction_file:
            pass

    def login_user(self):
        username = self.entry_username_login.get()
        password = self.entry_password_login.get()
        self.master.resizable(False, False)

        with open("BankData.txt", "r") as file:
            for line in file:
                if f"Username: {username}, " in line and f"Password: {password}, " in line:
                    self.username = username
                    self.balance = float(line.split(", Balance: R")[1])
                    self.prompt_transaction_choice()
                    return
        messagebox.showerror("Login Failed", "Invalid username or password.")

    def prompt_transaction_choice(self):
        self.transaction_choice_window = tk.Toplevel(self.master)
        self.transaction_choice_window.title("Transaction Choice")
        self.transaction_choice_window.configure(bg='teal')
        self.master.resizable(False, False)

        label = tk.Label(self.transaction_choice_window, text="Would you like to make a transaction?", bg='teal',
                         fg='white', font=("Arial", 12))
        label.pack(pady=10)

        yes_button = tk.Button(self.transaction_choice_window, text="1. Yes", command=self.create_transaction_gui)
        yes_button.pack(pady=5)

        no_button = tk.Button(self.transaction_choice_window, text="2. No", command=self.show_personal_details_gui)
        no_button.pack(pady=5)

        self.back_button = tk.Button(self.master, text="Back", command=self.create_registration_gui)
        self.back_button.grid(row=6, column=0, columnspan=2, pady=10)

    def create_transaction_gui(self):
        self.clear_gui()
        self.master.resizable(False, False)
        self.transaction_choice_window.destroy()
        for widget in self.master.winfo_children():
            widget.grid_forget()

        self.master.configure(bg='teal')

        image = Image.open("images/banklogo5.png")
        self.logo_image = ImageTk.PhotoImage(image)
        self.logo_placeholder = tk.Label(self.master, image=self.logo_image, bg='teal')
        self.logo_placeholder.grid(row=0, column=0, columnspan=3, padx=(90, 90), pady=(10, 10))

        self.label_balance = tk.Label(self.master, text=f"Balance: R{self.balance:.2f}", bg='teal', fg='white',
                                      font=("Arial", 12))
        self.label_balance.grid(row=1, column=0, padx=100, pady=10)

        button_width = 20  # Set a fixed width for the buttons
        
       
        self.transaction_button = tk.Button(self.master, text="Make a Transaction", command=self.prompt_transaction,
                                            width=button_width)
        self.transaction_button.grid(row=3, column=0, columnspan=2, padx=100, pady=10)

        self.bank_statement_button = tk.Button(self.master, text="Bank Statement", command=self.show_bank_statement,
                                               width=button_width)
        self.bank_statement_button.grid(row=4, column=0, columnspan=2, padx=100, pady=10)
        
        self.personal_details_button = tk.Button(self.master, text="Personal Details", command=self.show_personal_details_gui,
                                                  width=button_width)
        self.personal_details_button.grid(row=5, column=0, columnspan=2, padx=100, pady=10)

        self.back_button = tk.Button(self.master, text="Back", command=self.create_registration_gui)
        self.back_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        

    def show_personal_details_gui(self):
        self.clear_gui()
        self.transaction_choice_window.destroy()
        for widget in self.master.winfo_children():
            widget.grid_forget()

        self.master.configure(bg='teal')
        self.master.geometry("300x300")
        self.master.resizable(False, False)

        image = Image.open("images/banklogo5.png")
        self.logo_image = ImageTk.PhotoImage(image)
        self.logo_placeholder = tk.Label(self.master, image=self.logo_image, bg='teal')
        self.logo_placeholder.grid(row=0, column=0, columnspan=3, padx=(90, 90), pady=(10, 10))

        self.show_details_button = tk.Button(self.master, text="Show Personal Details",
                                             command=self.show_personal_details)
        self.show_details_button.grid(row=1, column=0, columnspan=2, padx=90, pady=10)
        
        self.edit_details_button = tk.Button(self.master, text="Edit Personal Details", command=self.edit_personal_details_gui)
        self.edit_details_button.grid(row=2, column=0, columnspan=2, padx=90, pady=10)

        self.back_button = tk.Button(self.master, text="Back", command=self.create_registration_gui)
        self.back_button.grid(row=6, column=0, columnspan=2, pady=10)

    '''def show_personal_details(self):
        with open("BankData.txt", "r") as file:
            for line in file:
                if f"Username: {self.username}, " in line:
                    data = line.strip().split(", ")
                    details = {
                        "Username": data[0].split(": ")[1],
                        "Age": data[1].split(": ")[1],
                        "Gender": data[2].split(": ")[1],
                        "Email": data[3].split(": ")[1],
                        "Account Number": data[4].split(": ")[1],
                        "Account Type": data[5].split(": ")[1]
                    }

        details_window = tk.Toplevel(self.master)
        details_window.title("Personal Details")
        details_window.configure(bg='teal')

        tree = ttk.Treeview(details_window, columns=("Field", "Value"), show="headings")
        tree.heading("Field", text="Field")
        tree.heading("Value", text="Value")
        for key, value in details.items():
            tree.insert("", "end", values=(key, value))
        tree.pack(expand=True, fill="both")
        
    def edit_personal_details_gui(self):
        self.clear_gui()
        for widget in self.master.winfo_children():
            widget.grid_forget()

        self.master.configure(bg='teal')
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        with open("BankData.txt", "r") as file:
            for line in file:
                if f"Username: {self.username}, " in line:
                    data = line.strip().split(", ")
                    details = {
                        "Username": data[0].split(": ")[1],
                        "Age": data[1].split(": ")[1],
                        "Gender": data[2].split(": ")[1],
                        "Email": data[3].split(": ")[1],
                        "Account Number": data[4].split(": ")[1],
                        "Account Type": data[5].split(": ")[1]
                    }

        self.username_entry = tk.Entry(self.master)
        self.username_entry.insert(0, details["Username"])
        self.username_entry.grid(row=0, column=1)

        self.age_entry = tk.Entry(self.master)
        self.age_entry.insert(0, details["Age"])
        self.age_entry.grid(row=1, column=1)

        self.email_entry = tk.Entry(self.master)
        self.email_entry.insert(0, details["Email"])
        self.email_entry.grid(row=2, column=1)

        self.gender_var = tk.StringVar(value=details["Gender"])
        self.gender_menu = ttk.Combobox(self.master, textvariable=self.gender_var, values=["Male", "Female"])
        self.gender_menu.grid(row=3, column=1)

        self.account_type_var = tk.StringVar(value=details["Account Type"])
        self.account_type_menu = ttk.Combobox(self.master, textvariable=self.account_type_var, values=["Savings", "Checking", "Business"])
        self.account_type_menu.grid(row=4, column=1)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_personal_details)
        self.save_button.grid(row=5, column=0, columnspan=2)

        self.back_button = tk.Button(self.master, text="Back", command=self.show_personal_details_gui)
        self.back_button.grid(row=6, column=0, columnspan=2)

def save_personal_details(self):
    new_username = self.username_entry.get()
    new_age = self.age_entry.get()
    new_email = self.email_entry.get()
    new_gender = self.gender_var.get()
    new_account_type = self.account_type_var.get()

    if not (new_username and new_age and new_email and new_gender and new_account_type):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    if not new_age.isdigit() or int(new_age) < 18:
        messagebox.showerror("Error", "Invalid age.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
        messagebox.showerror("Error", "Invalid email format.")
        return

    new_lines = []
    with open("BankData.txt", "r") as file:
        for line in file:
            if f"Username: {self.username}, " in line:
                data = line.strip().split(", ")
                account_number = data[4].split(": ")[1]
                password = data[6].split(": ")[1]
                balance = data[7].split(": ")[1]
                new_line = f"Username: {new_username}, Age: {new_age}, Gender: {new_gender}, Email: {new_email}, Account Type: {new_account_type}, Account Number: {account_number}, Password: {password}, Balance: {balance}\n"
                new_lines.append(new_line)
            else:
                new_lines.append(line)

    with open("BankData.txt", "w") as file:
        for line in new_lines:
            file.write(line)

    self.username = new_username
    messagebox.showinfo("Success", "Details updated successfully.")
    self.show_personal_details_gui()
'''

    def prompt_transaction(self):
        self.transaction_window = tk.Toplevel(self.master)
        self.transaction_window.title("Transaction")
        self.transaction_window.configure(bg='teal')
        self.master.resizable(False, False)

        label = tk.Label(self.transaction_window, text="Choose transaction type:", bg='teal', fg='white',
                         font=("Arial", 12))
        label.pack(pady=10)

        deposit_button = tk.Button(self.transaction_window, text="Deposit", command=self.deposit_gui)
        deposit_button.pack(pady=5)

        withdraw_button = tk.Button(self.transaction_window, text="Withdraw", command=self.withdraw_gui)
        withdraw_button.pack(pady=5)

    def deposit_gui(self):
        self.transaction_window.destroy()
        self.master.resizable(False, False)
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
        self.master.resizable(False, False)
        self.withdraw_window = tk.Toplevel(self.master)
        self.withdraw_window.title("Withdraw")
        self.withdraw_window.configure(bg='teal')

        label = tk.Label(self.withdraw_window, text="Enter withdrawal amount:", bg='teal', fg='white',
                         font=("Arial", 12))
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
                raise ValueError("Enter valid amount.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.update_balance(-amount)
            self.log_transaction(amount, "Withdrawal")
            self.withdraw_window.destroy()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def update_balance(self, amount):
        self.master.resizable(False, False)
        with open("BankData.txt", "r+") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if f"Username: {self.username}, " in line:
                    data = line.strip().split(", ")
                    balance = float(data[6].split(": ")[1].replace("R", ""))
                    new_balance = balance + amount
                    self.balance = new_balance
                    lines[
                        i] = f"Username: {data[0].split(': ')[1]}, Age: {data[1].split(': ')[1]}, Gender: {data[2].split(': ')[1]}, Email: {data[3].split(': ')[1]}, Account Number: {data[4].split(': ')[1]}, Password: {data[5].split(': ')[1]}, Balance: R{new_balance:.2f}\n"
                    self.label_balance.config(text=f"Balance: R{new_balance:.2f}")
                    file.seek(0)
                    file.writelines(lines)
                    return

    def log_transaction(self, amount, transaction_type):
        now = datetime.datetime.now()
        transaction_entry = f"{now}: {transaction_type} of R{amount:.2f}\n"

        # Append the transaction to the user's transaction log file
        with open(f"{self.username}_TransactionLog.txt", "a") as user_file:
            user_file.write(transaction_entry)

        # Append the transaction to the global TransactionLog.txt file
        with open("TransactionLog.txt", "a") as global_file:
            global_file.write(f"Username: {self.username}, {transaction_entry}")

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

                download_button = tk.Button(statement_window, text="Download Transaction History", font=('Calibri', 12),
                                        command=lambda: self.download_transactions(statement))
                download_button.pack(pady=10)

            else:
                messagebox.showerror("Error", "No transactions found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No transactions found.")

    def download_transactions(self, transactions):
        download_location = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if download_location:
            with open(download_location, "w") as file:
                file.writelines(transactions)
            messagebox.showinfo("Success", "Transaction history downloaded successfully.")


    def clear_gui(self):
        for widget in self.master.winfo_children():
            widget.destroy()


root = tk.Tk()
banking_app = BankingApp(root)
root.mainloop()
