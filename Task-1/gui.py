import tkinter as tk
from tkinter import messagebox
from Calculator import execute

# ---------------- Functions ---------------- #
def calculate(choice):
    a = first_num.get().strip()
    b = second_num.get().strip()

    if not a or not b:
        messagebox.showwarning("Missing Input", "Please enter both numbers.")
        return

    try:
        result = execute(a, b, choice)
        display.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Calculator")
root.geometry("400x520")
root.configure(bg="#121212")
root.resizable(False, False)

# ---------------- Display ---------------- #
display = tk.Label(
    root,
    text="0",
    bg="#1E1E1E",
    fg="white",
    font=("Arial", 24, "bold"),
    height=2,
    anchor="e",
    padx=15
)
display.pack(fill="x", padx=20, pady=20)

# ---------------- Input Area ---------------- #
input_frame = tk.Frame(root, bg="#121212")
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="First Number",
    bg="#121212",
    fg="white",
    font=("Arial", 11)
).pack(anchor="w")

first_num = tk.Entry(
    input_frame,
    font=("Arial", 16),
    width=22,
    justify="center"
)
first_num.pack(pady=5)

tk.Label(
    input_frame,
    text="Second Number",
    bg="#121212",
    fg="white",
    font=("Arial", 11)
).pack(anchor="w", pady=(10, 0))

second_num = tk.Entry(
    input_frame,
    font=("Arial", 16),
    width=22,
    justify="center"
)
second_num.pack(pady=5)

# ---------------- Buttons ---------------- #
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=30)

buttons = [
    ("+", "1", "#4CAF50"),
    ("−", "2", "#2196F3"),
    ("×", "3", "#FF9800"),
    ("÷", "4", "#F44336"),
]

for i, (symbol, value, color) in enumerate(buttons):
    tk.Button(
        btn_frame,
        text=symbol,
        font=("Arial", 20, "bold"),
        bg=color,
        fg="white",
        width=5,
        height=2,
        relief="flat",
        command=lambda v=value: calculate(v)
    ).grid(row=i // 2, column=i % 2, padx=12, pady=12)

# ---------------- Clear Button ---------------- #
def clear():
    first_num.delete(0, tk.END)
    second_num.delete(0, tk.END)
    display.config(text="0")

tk.Button(
    root,
    text="Clear",
    font=("Arial", 13, "bold"),
    bg="#616161",
    fg="white",
    relief="flat",
    command=clear
).pack(ipadx=20, ipady=8)

root.mainloop()