import os
os.environ['TCL_LIBRARY'] = r'C:\Users\User1\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User1\AppData\Local\Programs\Python\Python313\tcl\tk8.6'


import FreeSimpleGUI as sg
from converter import meters

label = sg.Text("Enter Feet   ")

input1 = sg.Input()
label2 = sg.Text("Enter Inches")
input2 = sg.Input()
button = sg.Button("Convert")
button2 = sg.Button("Exit")
output_text = sg.Text(key="output",text_color= "green")

window = sg.Window("Converter",[[label, input1],[label2,input2],[button,button2,output_text]])

while True:

    event, data = window.read()
    print(event)
    print(data)
    match event:
        case "Convert":
            feet = float(data[0])
            inches = float(data[1])
            Meters=(meters(feet,inches))
            window["output"].update(value=f"{Meters}")

        case "Exit":
            break