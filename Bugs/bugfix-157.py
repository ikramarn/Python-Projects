import os
os.environ['TCL_LIBRARY'] = r'C:\Users\User1\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User1\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File C.....",
                   layout=[[label],
                           [option1],
                            [option2],
                            [option3],
                            [option4],
                           ])

window.read()
window.close()