import tkinter as tk
from generate_ast import generate_ast
from tkinter import scrolledtext, Spinbox, Label
from tkinter import messagebox
from python_smell_detector import detect_code_smells

from Detectors.long_parameter_list import detect_long_parameter_list
from Detectors.large_method import detect_long_method
from Detectors.excessive_returns import detect_excessive_returns
from Detectors.code_duplication import detect_duplicate_code
from Detectors.complex_method import detect_complex_method
from Detectors.complex_lambda_function import detect_complex_lambda

def detect_smells():
    code = code_input.get("1.0", tk.END)

    # Tree-sitter ast
    tree = generate_ast(code)
    root_node = tree.root_node

    try:
        # Retrieving threshold values
        param_thresh = int(parameter_threshold.get())
        return_thresh = int(return_threshold.get())
        max_nesting_level_val = int(max_nesting_level.get())
        max_statement_count_val = int(max_statement_count.get())
        lambda_complexity = int(complexity.get())
        child_thresh = int(child_threshold.get())

        # Pass these values to the detection function
        smells = []

        for node in root_node.children:

            if node.type == 'function_definition':
                # Duplicated Code Smell
                duplicate_code_issues = detect_duplicate_code(node, code)
                for issue in duplicate_code_issues:
                    smells.append((issue, 'Duplicate Code'))
                    
                
                # Long Parameter List Smell
                if detect_long_parameter_list(node, param_thresh):
                    smells.extend([(smell_node, 'Long Parameter List') for smell_node in detect_long_parameter_list(node,parameter_threshold)])
                    
                
                # Excessive Return Smell
                excessive_returns = detect_excessive_returns(node, return_thresh)
                if excessive_returns:
                    for return_node in excessive_returns:
                        smells.append((return_node, 'Excessive Returns'))
                        

                # Complex Method Smell
                complex_method_issues = detect_complex_method(node, max_nesting_level_val, max_statement_count_val)
                for issue in complex_method_issues:
                    smells.append((issue, 'Complex Method'))
                    
                
                # Complex Lambda Functions
                complex_lambda_issues = detect_complex_lambda(node, lambda_complexity)
                for issue in complex_lambda_issues:
                    smells.append((issue, 'Complex Lambda'))
                    
                
                # Large method smell
                large_method_issues = detect_long_method(node,code, child_thresh)
                for issue in large_method_issues:
                    smells.append((issue, 'Large Method'))


        result_output.delete("1.0", tk.END)
        result_output.insert(tk.INSERT, smells)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main application window
root = tk.Tk()
root.title("Code Smell Detector")

# Code input area
code_input = scrolledtext.ScrolledText(root, height=15)
code_input.pack(pady=10)

# Threshold inputs
parameter_threshold = Spinbox(root, from_=1, to=10, width=5)
return_threshold = Spinbox(root, from_=1, to=10, width=5)
max_nesting_level = Spinbox(root, from_=1, to=10, width=5)
max_statement_count = Spinbox(root, from_=1, to=50, width=5)
complexity = Spinbox(root, from_=1, to=10, width=5)
child_threshold = Spinbox(root, from_=1, to=50, width=5)

# Labels for threshold inputs
Label(root, text="Parameter Threshold:").pack()
parameter_threshold.pack()
Label(root, text="Return Threshold:").pack()
return_threshold.pack()
Label(root, text="Max Nesting Level:").pack()
max_nesting_level.pack()
Label(root, text="Max Statement Count:").pack()
max_statement_count.pack()
Label(root, text="Lambda Complexity:").pack()
complexity.pack()
Label(root, text="Child Threshold:").pack()
child_threshold.pack()

# Detect button
detect_button = tk.Button(root, text="Detect Smells", command=detect_smells)
detect_button.pack()

# Result output area
result_output = scrolledtext.ScrolledText(root, height=15)
result_output.pack(pady=10)

root.mainloop()
