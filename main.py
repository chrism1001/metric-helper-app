import tkinter as tk
from tkinter import PhotoImage, StringVar, ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Metric Converter")
photo = PhotoImage(file = "metric-helper-app/images/ruler.png")
root.iconphoto(False, photo)

main = ttk.Frame(root)
main.grid()

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)

input_unit = StringVar()
output_unit = StringVar()

def input_selection(event):
    input_unit.set(input_selected.get())
def output_selection(event):
    output_unit.set(output_selected.get())
    
input = StringVar()
output = StringVar()

# Conversion function that uses a dictionary to find the specific input units and output units
# and returns the conversion of the value input.
def convert(input, input_unit, output_unit):
    metric_dict = {"base value": 1, "kilo": 1000, "hecto": 100, "deca": 10, "deci": .1, "centi": .01, "milli": .001}
    return input * metric_dict[input_unit] / metric_dict[output_unit]

# Converts and displays on the screen when the convert button is pressed.
def convert_press(*args):
    try:
        global input_unit; global output_unit
        global input; global output
        total = convert(float(input.get()), input_unit.get(), output_unit.get())
        output.set(total)
    except:
        output.set("Not a valid number.")

# Input field
input_field = ttk.Entry(root, textvariable = input)
input_field.grid(row = 0, column = 0, stick = "ew", padx = 20, pady = 10)
# Output field
output_field = ttk.Entry(root, textvariable = output)
output_field["state"] = "readonly"
output_field.grid(row = 0, column = 2, stick = "ew", padx = 20, pady = 10)

# Equals label between input and output fields.
equals_label = ttk.Label(root, text = "=")
equals_label.grid(row = 0, column = 1)

# Combobox for selecting units. Located to the left
input_selected = tk.StringVar()
input_dropdown = ttk.Combobox(root, textvariable = input_selected, justify = "center")
input_dropdown["values"] = ("base value", "kilo", "hecto", "deca", "deci","centi", "milli")
input_dropdown["state"] = "readonly"
input_dropdown.grid(row = 1, column = 0, padx = 20, pady = 10)

# Binding for first selected unit.
input_dropdown.bind("<<ComboboxSelected>>", input_selection)

# Combobox for selecting units. Located to the right.
output_selected = tk.StringVar()
output_dropdown = ttk.Combobox(root, textvariable = output_selected, justify = "center")
output_dropdown["values"] = ("base value", "kilo", "hecto", "deca", "deci","centi", "milli")
output_dropdown["state"] = "readonly"
output_dropdown.grid(row = 1, column = 2, padx = 20, pady = 10)

# Binding for second selected unit.
output_dropdown.bind("<<ComboboxSelected>>", output_selection)

# Text label that displays "to"
text_label = ttk.Label(root, text = "to")
text_label.grid(row = 1, column = 1)

# Calculate button
convert_button = ttk.Button(root, text = "Convert", command = convert_press)
convert_button.grid(row = 2, column = 0, columnspan = 3, padx = 20, pady = 10)

# Keybinding for enter key on keyboard
root.bind("<Return>", convert_press)
root.bind("<KP_Enter>", convert_press)

root.mainloop()
