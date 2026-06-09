import tkinter as tk

window = tk.Tk()
window.title("Student App")
window.geometry("400x400")

def show_name():
    name = entry.get()
    result.config(text=f"Welcome, {name}!")

tk.Label(window, text="Enter Your Name:").pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

tk.Button(window, text="Submit", command=show_name).pack(pady=10)

result = tk.Label(window, text="")


result.pack(pady=10)

window.mainloop()