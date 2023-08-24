import tkinter as tk

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")

        self.balance = 1000  # Initial balance

        self.balance_var = tk.StringVar()
        self.balance_var.set(f"Balance: ${self.balance:.2f}")

        self.create_widgets()

    def create_widgets(self):
        balance_label = tk.Label(self.root, textvariable=self.balance_var)
        balance_label.pack()

        deposit_label = tk.Label(self.root, text="Deposit Amount:")
        deposit_label.pack()

        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack()

        deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        deposit_button.pack()

        withdraw_label = tk.Label(self.root, text="Withdraw Amount:")
        withdraw_label.pack()

        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack()

        withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        withdraw_button.pack()

    def deposit(self):
        try:
            deposit_amount = float(self.deposit_entry.get())
            if deposit_amount > 0:
                self.balance += deposit_amount
                self.balance_var.set(f"Balance: ${self.balance:.2f}")
                self.deposit_entry.delete(0, tk.END)
        except ValueError:
            pass

    def withdraw(self):
        try:
            withdraw_amount = float(self.withdraw_entry.get())
            if 0 < withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                self.balance_var.set(f"Balance: ${self.balance:.2f}")
                self.withdraw_entry.delete(0, tk.END)
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
