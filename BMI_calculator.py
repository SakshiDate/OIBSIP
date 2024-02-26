from tkinter import *
from tkinter import messagebox

def get_height():
    try:
        height = float(entry_height.get())
        return height
    except ValueError:
        messagebox.showinfo("Error", "Invalid height!")

def get_weight():
    try:
        weight = float(entry_weight.get())
        return weight
    except ValueError:
        messagebox.showinfo("Error", "Invalid weight!")

def calculate_bmi(a=""):
    try:
        height = get_height()
        weight = get_weight()
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Error", "Positive height required!")
    except ValueError:
        return

    bmi_categories = [
        (15.0, "Very severely underweight!!"),
        (16.0, "Severely underweight!"),
        (18.5, "Underweight!"),
        (25.0, "Normal."),
        (30.0, "Overweight."),
        (35.0, "Moderately obese!"),
        (40.0, "Severely obese!"),
        (float('inf'), "Super obese!!")
    ]

    for category, remark in bmi_categories:
        if bmi <= category:
            result_text = f"Your BMI is {bmi:.2f}\nRemarks: {remark}"
            messagebox.showinfo("Result", result_text)
            break

if __name__ == '__main__':
    root = Tk()
    root.bind("<Return>", calculate_bmi)
    root.geometry("500x300")
    root.configure(background="#F0F0F0")
    root.title("BMI Calculator")
    root.resizable(width=False, height=False)

    label_welcome = Label(root, bg="#F0F0F0", text="BMI Calculator", font=("Arial", 20, "bold"), pady=10, fg="#333333")
    label_welcome.place(x=160, y=10)

    label_weight = Label(root, bg="#F0F0F0", text="Enter Weight (in kg):", bd=6, font=("Arial", 12), pady=5, fg="#333333")
    label_weight.place(x=70, y=60)
    entry_weight = Entry(root, bd=8, width=10, font=("Arial", 12))
    entry_weight.place(x=250, y=60)

    label_height = Label(root, bg="#F0F0F0", text="Enter Height (in meters):", bd=6, font=("Arial", 12), pady=5, fg="#333333")
    label_height.place(x=70, y=120)
    entry_height = Entry(root, bd=8, width=10, font=("Arial", 12))
    entry_height.place(x=250, y=120)

    button_calculate = Button(root, bg="#2187e7", bd=12, text="Calculate BMI", padx=20, pady=10, command=calculate_bmi, font=("Arial", 14, "bold"), fg="#FFFFFF")
    button_calculate.grid(row=3, column=0, sticky=W)
    button_calculate.place(x=150, y=200)

    root.mainloop()
