import customtkinter as ctk
import tkinter as tk

root = ctk.CTk()
root.geometry("400x200")

# Create the first segment with a checkbox list
checkbox_list = ["Option 1", "Option 2", "Option 3"]
for i, option in enumerate(checkbox_list):
    checkbox = ctk.CTkCheckBox(root, text=option)
    checkbox.grid(row=i, column=0, padx=10, pady=10, sticky="w")

# Create the second segment with a round button
round_button_1 = tk.Button(root, text="Round Button 1", bg="red", fg="white", width=15, height=5, borderwidth=0, highlightthickness=0, bd=0, command=lambda: print("Round Button 1 clicked!"))
round_button_1.grid(row=0, column=1, padx=10, pady=10)

# Create the third segment with another round button
round_button_2 = tk.Button(root, text="Round Button 2", bg="blue", fg="white", width=15, height=5, borderwidth=0, highlightthickness=0, bd=0, command=lambda: print("Round Button 2 clicked!"))
round_button_2.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
