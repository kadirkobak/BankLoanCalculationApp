import tkinter as tk
from tkinter import messagebox

def calculate_fixed_interest_loan(loan_amount, monthly_interest_rate, term_months):
    interest_amount = loan_amount * (monthly_interest_rate / 100) * term_months
    total_payment = loan_amount + interest_amount
    monthly_installment = total_payment / term_months
    return monthly_installment, total_payment

def calculate():
    try:
        loan_amount = float(entry_loan_amount.get())
        monthly_interest_rate = float(entry_interest_rate.get())
        term_months = int(entry_term.get())

        monthly_payment, total_payment = calculate_fixed_interest_loan(loan_amount, monthly_interest_rate, term_months)

        result_label.config(text=f"Monthly Payment: {monthly_payment:.2f} TL\nTotal Repayment: {total_payment:.2f} TL")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


root = tk.Tk()
root.title("Loan Calculator")
root.geometry("400x350") 


tk.Label(root, text="Loan Amount (TL):").pack(pady=(10, 0))
entry_loan_amount = tk.Entry(root)
entry_loan_amount.pack()

tk.Label(root, text="Monthly Interest Rate (%):").pack(pady=(10, 0))
entry_interest_rate = tk.Entry(root)
entry_interest_rate.pack()

tk.Label(root, text="Term (in months):").pack(pady=(10, 0))
entry_term = tk.Entry(root)
entry_term.pack()


tk.Button(root, text="Calculate", command=calculate).pack(pady=15)


result_label = tk.Label(root, text="Results will be shown here", font=("Arial", 12))
result_label.pack(pady=10)


root.mainloop()
