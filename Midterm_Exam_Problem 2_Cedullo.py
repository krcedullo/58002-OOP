import tkinter as tk

def show_full_name():
    given_name = entry_given_name.get()
    middle_name = entry_middle_name.get()
    last_name = entry_last_name.get()
    full_name = f"{last_name}, {given_name} {middle_name}"
    entry_full_name.delete(0, tk.END)
    entry_full_name.insert(0, full_name)

def clear_all():
    entry_given_name.delete(0, tk.END)
    entry_middle_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_full_name.delete(0, tk.END)

# main window
root = tk.Tk()
root.title("My Full Name")
root.configure(bg="white")

# default font and foreground color for labels and text
label_font = ("Verdana", 12)
label_fg = "red"
text_font = ("Verdana", 12)
text_fg = "red"

# title label
label_title = tk.Label(root, text="My Full Name", font=("Verdana", 24), fg="red", bg="white")
label_title.grid(row=0, column=0, columnspan=2, padx=5, pady=20)

#  labels for input fields
label_given_name = tk.Label(root, text="Enter Given Name:", font=label_font, fg=label_fg, bg="white")
label_given_name.grid(row=1, column=0, sticky="e", padx=70, pady=10)

label_middle_name = tk.Label(root, text="Enter Middle Name:", font=label_font, fg=label_fg, bg="white")
label_middle_name.grid(row=2, column=0, sticky="e", padx=70, pady=10)

label_last_name = tk.Label(root, text="Enter Last Name:", font=label_font, fg=label_fg, bg="white")
label_last_name.grid(row=3, column=0, sticky="e", padx=70, pady=10)

label_full_name = tk.Label(root, text="My Full Name is:", font=label_font, fg=label_fg, bg="white")
label_full_name.grid(row=4, column=0, sticky="e", padx=70, pady=10)

# Entry widgets for input fields
entry_given_name = tk.Entry(root, font=text_font)
entry_given_name.grid(row=1, column=1, padx=70, pady=10)

entry_middle_name = tk.Entry(root, font=text_font)
entry_middle_name.grid(row=2, column=1, padx=70, pady=10)

entry_last_name = tk.Entry(root, font=text_font)
entry_last_name.grid(row=3, column=1, padx=70, pady=10)

entry_full_name = tk.Entry(root, font=text_font, fg=text_fg)
entry_full_name.grid(row=4, column=1, padx=70, pady=10)

# Show Full Name button
button_show_full_name = tk.Button(root, text="Show Full Name", font=label_font, fg=label_fg, bg="white", command=show_full_name)
button_show_full_name.grid(row=5, column=0, columnspan=2, padx=200, pady=20, sticky="ew")

# Clear All button
button_clear_all = tk.Button(root, text="Clear All", font=label_font, fg=label_fg, bg="white", command=clear_all)
button_clear_all.grid(row=6, column=0, columnspan=4, padx=200, pady=10, sticky="ew")

root.mainloop()
