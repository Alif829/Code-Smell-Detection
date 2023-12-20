import customtkinter as ctk
import tree_sitter
import tkinter as tk
from generate_ast import generate_ast
from customtkinter import *
from PIL import Image
from py2cfg import CFGBuilder
from generate_smell_tree import generate_ast_graph
from tkinter import filedialog, PhotoImage

from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.code_duplication import detect_duplicate_code
from Detectors.complex_method import detect_complex_method
from Detectors.complex_lambda_function import detect_complex_lambda


def display_ast_image(image_path):
    # Function to display the AST image in the GUI
    try:
        ast_img = PhotoImage(file=image_path)
        ast_label = ctk.CTkLabel(middle_frame, image=ast_img)
        ast_label.image = ast_img  # reference to avoid garbage collection
        ast_label.pack(pady=10)
    except Exception as e:
        ctk.messagebox.showerror("Error", str(e))


def detect_smells():
    code = code_input.get("1.0", tk.END)
    tree = generate_ast(code)
    root_node = tree.root_node

    try:
        param_thresh = int(parameter_threshold.get())
        return_thresh = int(return_threshold.get())
        max_nesting_level_val = int(max_nesting_level.get())
        max_statement_count_val = int(max_statement_count.get())
        lambda_complexity = int(complexity.get())
        child_thresh = int(child_threshold.get())

        smells = []
        smell_nodes=[]
        for node in root_node.children:
            if node.type == 'function_definition':
                duplicate_code_issues = detect_duplicate_code(node, code)
                for issue in duplicate_code_issues:
                    smells.append((issue, 'Duplicate Code'))

                long_parameter_list_issues = detect_long_parameter_list(node, param_thresh)
                for issue in long_parameter_list_issues:
                    smells.append((issue, 'Long Parameter List'))

                excessive_returns_issues = detect_excessive_returns(node, return_thresh)
                for issue in excessive_returns_issues:
                    smells.append((issue, 'Excessive Returns'))

                complex_method_issues = detect_complex_method(node, max_nesting_level_val, max_statement_count_val)
                for issue in complex_method_issues:
                    smells.append((issue, 'Complex Method'))

                complex_lambda_issues = detect_complex_lambda(node, lambda_complexity)
                for issue in complex_lambda_issues:
                    smells.append((issue, 'Complex Lambda'))

                large_method_issues = detect_long_method(node, code, child_thresh)
                for issue in large_method_issues:
                    smells.append((issue, 'Large Method'))
        
        
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.INSERT, smells)
        # generate_ast_graph and display the AST image
        ast_image_path = 'ast_graph.png'  # Path where the AST image will be saved
        language = tree_sitter.Language('E:/tree-sitter-python/tree-sitter-python.dll', 'python')
        graph = generate_ast_graph(code, language,smells)
        graph.render(ast_image_path, format='png', view=False)

        display_ast_image(ast_image_path)
    except Exception as e:
        ctk.messagebox.showerror("Error", str(e))


# main application window set up
ctk.set_appearance_mode("Dark")  # dark theme
root = ctk.CTk()
root.title("Code Smell Detector")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Frames
left_frame = ctk.CTkFrame(root)
middle_frame = ctk.CTkFrame(root)
right_frame = ctk.CTkFrame(root)

left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

left_frame.grid_columnconfigure(0, weight=1)
middle_frame.grid_rowconfigure(0, weight=1)
middle_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

# List of code smells
logo_img_data = Image.open("Icons/logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

CTkLabel(master=left_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")
CTkLabel(master=left_frame, text="Code Smells",fg_color="transparent", font=("Arial Bold", 18)).pack(pady=10,padx=10, anchor="center")

analytics_img_data = Image.open("Icons/duplicate.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)
CTkButton(master=left_frame,width=200 ,image=analytics_img, text="Code Duplication", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

package_img_data = Image.open("Icons/lambda.png")
package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
CTkButton(master=left_frame,width=200, image=package_img, text="Complex Lambda", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

list_img_data = Image.open("Icons/complex.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
CTkButton(master=left_frame,width=200, image=list_img, text="Complex Method", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

returns_img_data = Image.open("Icons/large.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
CTkButton(master=left_frame,width=200, image=returns_img, text="Large Method", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

settings_img_data = Image.open("Icons/returns_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=left_frame,width=200, image=settings_img, text="Excessive Returns", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

person_img_data = Image.open("Icons/parameter.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=left_frame,width=200, image=person_img, text="Long Parameter List", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))


# Code input and output
code_input = ctk.CTkTextbox(middle_frame, height=300,width=900,scrollbar_button_color="#FFCC70",corner_radius=16)
code_input.pack(pady=10)
result_output = ctk.CTkTextbox(middle_frame, height=200,width=900,scrollbar_button_color="#FFCC70",corner_radius=16)
result_output.pack(pady=10)

# Threshold inputs
parameter_threshold = ctk.CTkEntry(right_frame, width=200)
return_threshold = ctk.CTkEntry(right_frame, width=200)
max_nesting_level = ctk.CTkEntry(right_frame, width=200)
max_statement_count = ctk.CTkEntry(right_frame, width=200)
complexity = ctk.CTkEntry(right_frame, width=200)
child_threshold = ctk.CTkEntry(right_frame, width=200)

# threshold entries with labels
ctk.CTkLabel(right_frame, text="Parameter Threshold:").pack()
parameter_threshold.pack(pady=2)
ctk.CTkLabel(right_frame, text="Return Threshold:").pack()
return_threshold.pack(pady=2)
ctk.CTkLabel(right_frame, text="Max Nesting Level:").pack()
max_nesting_level.pack(pady=2)
ctk.CTkLabel(right_frame, text="Max Statement Count:").pack()
max_statement_count.pack(pady=2)
ctk.CTkLabel(right_frame, text="Lambda Complexity:").pack()
complexity.pack(pady=2)
ctk.CTkLabel(right_frame, text="Child Threshold:").pack()
child_threshold.pack(pady=2)

# Detect button
detect_button = ctk.CTkButton(middle_frame, text="Detect Smells", fg_color="#207244", command=detect_smells)
detect_button.pack(side="left", padx=90)  # Place it to the left


# handle file selection and input
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, 'r') as file:
            code_input.delete("1.0", tk.END)
            code_input.insert(tk.END, file.read())

# "Open File" button to trigger the file dialog
open_file_button = ctk.CTkButton(middle_frame, text="Open File", fg_color="#207244", command=open_file)
open_file_button.pack(side="right", padx=100)


root.mainloop()
