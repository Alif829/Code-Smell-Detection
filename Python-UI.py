from tkinter import Tk, Label, Entry, Button, Listbox, END

from python_smell_detector import detect_code_smells


def detect_smells_and_display(code):
    # Analyze code and retrieve smells
    smells = detect_code_smells(code)

    # Clear listbox
    smells_listbox.delete(0, END)

    # Add each smell to the listbox
    for smell, description in smells:
        smells_listbox.insert(END, f"{description}: {smell}")


# Initialize Tkinter window
window = Tk()
window.title("Code Smell Detector")

# Label for code input
code_label = Label(window, text="Enter Python code:")
code_label.grid(row=0, column=0, sticky="E")

# Entry for code input
code_entry = Entry(window, width=50)
code_entry.grid(row=0, column=1, columnspan=2)

# Button to trigger smell detection
detect_button = Button(window, text="Detect Smells", command=lambda: detect_smells_and_display(code_entry.get()))
detect_button.grid(row=1, column=1)

# Listbox to display detected smells
smells_listbox = Listbox(window, width=50, height=10)
smells_listbox.grid(row=2, column=0, columnspan=3)

# Start the main event loop
window.mainloop()
