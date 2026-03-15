import tkinter as tk
from tkinter import messagebox
def calculate_interest():
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate / 100) ** time - 1)
        result = f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        messagebox.showinfo("Interest Calculation", result)

root = tk.Tk()
root.title("Interest Calculator")
label_principal = tk.Label(root, text="Principal Amount:")
label_principal.grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)
label_time = tk.Label(root, text="Time Period (years):")
label_time.grid(row=1, column=0, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=0, padx=10, pady=10)
label_rate = tk.Label(root, text="Rate of Interest (% per year):")
label_rate.grid(row=2, column=0, padx=10, pady=10)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=2, padx=20, pady=20)
button_calculate = tk.Button(root, text="Calculate",command=calculate_interest)
button_calculate.grid(row=2, column=0, columnspan=2, pady=20)
root.mainloop()