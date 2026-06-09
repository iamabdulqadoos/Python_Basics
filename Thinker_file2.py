import tkinter as tk
from tkinter import messagebox

# ================= MAIN WINDOW =================
window = tk.Tk()
window.title("Python Dashboard App")
window.geometry("420x360")
window.resizable(False, False)

# ================= CALCULATOR =================
def calculator():
    calc = tk.Toplevel(window)
    calc.title("Calculator")
    calc.geometry("300x250")

    tk.Label(calc, text="Simple Calculator", font=("Arial", 14)).pack(pady=10)

    e1 = tk.Entry(calc)
    e1.pack(pady=5)

    e2 = tk.Entry(calc)
    e2.pack(pady=5)

    result = tk.Label(calc, text="")
    result.pack(pady=10)

    def add():
        try:
            a = float(e1.get())
            b = float(e2.get())
            result.config(text=f"Result: {a + b}")
        except:
            result.config(text="Invalid Input")

    tk.Button(calc, text="Add", command=add).pack(pady=5)


# ================= LIST FUNCTIONS =================
def list_functions():
    win = tk.Toplevel(window)
    win.title("List Functions")
    win.geometry("300x250")

    numbers = [10, 20, 30]

    label = tk.Label(win, text=f"List: {numbers}")
    label.pack(pady=10)

    def add_item():
        numbers.append(40)
        label.config(text=f"List: {numbers}")

    def remove_item():
        if numbers:
            numbers.pop()
        label.config(text=f"List: {numbers}")

    tk.Button(win, text="Add Item", command=add_item).pack(pady=5)
    tk.Button(win, text="Remove Item", command=remove_item).pack(pady=5)


# ================= FILE CREATOR =================
def file_creator():
    win = tk.Toplevel(window)
    win.title("File Creator")
    win.geometry("350x300")

    tk.Label(win, text="File Name").pack(pady=5)
    file_name = tk.Entry(win)
    file_name.pack()

    tk.Label(win, text="Enter Content").pack(pady=5)
    text_box = tk.Text(win, height=6, width=30)
    text_box.pack()

    def create_file():
        name = file_name.get().strip()
        content = text_box.get("1.0", tk.END)

        if name == "":
            messagebox.showerror("Error", "File name cannot be empty!")
            return

        with open(name + ".txt", "w") as f:
            f.write(content)

        messagebox.showinfo("Success", "File Created Successfully!")

    tk.Button(win, text="Create File", command=create_file).pack(pady=10)


# ================= EXIT APP =================
def exit_app():
    window.destroy()


# ================= DASHBOARD UI =================
tk.Label(window, text="Python Dashboard App", font=("Arial", 18)).pack(pady=20)

tk.Button(window, text="Run Calculator", width=30, command=calculator).pack(pady=5)

tk.Button(window, text="Run List Functions", width=30, command=list_functions).pack(pady=5)

tk.Button(window, text="Run File Creator", width=30, command=file_creator).pack(pady=5)

tk.Button(window, text="Exit App", width=30, command=exit_app).pack(pady=10)


# ================= RUN APP =================
window.mainloop()