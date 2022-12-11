import Functions
from tkinter import *

"""import PySimpleGUI as GUI
import os.path"""

def GetInputFile():
    # Browse for input file then print its name in the text box
    Output_Label = Label(root, text=input_TextBox.get())
    Output_Label.grid(row=2, column=0)

if __name__ == "__main__":

    root = Tk()

    # Create a Label widget
    input_TextBox = Entry(root, width=50, borderwidth=5, bg="White", fg="Black")
    input_TextBox.insert(0, "Choose the file you want to analysis")
    #Output_Label = Label(root, text="Label box will be here!")

    # Create Buttons
    button_Choose_File = Button(root, text="Browse File", state=ACTIVE, padx=15, pady=2, fg="blue", command=GetInputFile)
    button_Exit = Button(root, text="Exit Program", state=ACTIVE, padx=5, pady=2, command=root.quit)
    button_PMF = Button(root, text="PMF", state=DISABLED, padx=10, pady=5, fg="Green")
    button_CDF = Button(root, text="CDF", state=DISABLED, padx=10, pady=5, fg="#AA336A")  # dark pink
    button_Mean = Button(root, text="Mean", state=DISABLED, padx=10, pady=5, fg="orange")
    button_Variance = Button(root, text="Variance", state=DISABLED, padx=10, pady=5, fg="#8B8000")  # dark yellow
    button_Skewness = Button(root, text="Skewness", state=DISABLED, padx=10, pady=5, fg="purple")
    button_kurtosis = Button(root, text="kurtosis", state=DISABLED, padx=10, pady=5, fg="Black")

    # Shoving it into the screen
    input_TextBox.grid(row=0, column=0)
    #Output_Label.grid(row=2, column=0)

    C = 20
    for i in range(1, C):
        Label(root, text=" ").grid(row=0, column=C)

    button_Choose_File.grid(row=0, column=4)
    button_Exit.grid(row=0, column=6)

    button_PMF.grid(row=3, column=6)
    Label(root, text=" ").grid(row=4, column=6)

    button_CDF.grid(row=8, column=6)
    Label(root, text=" ").grid(row=9, column=6)

    button_Mean.grid(row=13, column=6)
    Label(root, text=" ").grid(row=14, column=6)

    button_Variance.grid(row=18, column=6)
    Label(root, text=" ").grid(row=19, column=6)

    button_Skewness.grid(row=23, column=6)
    Label(root, text=" ").grid(row=24, column=6)

    button_kurtosis.grid(row=28, column=6)
    Label(root, text=" ").grid(row=29, column=6)

    # Generate main loop
    root.mainloop()

"""
    file_Data_Column = \
        [
            [
                GUI.Text("Import File"),
                GUI.In(size=(25, 1), enable_events=True, key="-FILE-"),
                GUI.FileBrowse(),
            ],
            [
                GUI.Listbox
                (
                    values=[], enable_events=True, size=(40,20),
                    key="-INPUT FILE-"
                )
            ],
        ]

    # Analytical data shown in the box
    Buttons_column = \
        [
            [


            ],
        ]
    # ---- full layout ----
    layout = \
        [
            [
                GUI.Column(file_Data_Column),
                GUI.VSeperator(),
                GUI.Column(Buttons_column),
            ]
        ]

    # Create the Window
    Window = GUI.Window("STATISTICAL ANALYSIS OF TEXT FILES", layout)

    # Create an event loop
    while True:
        event, value = Window.read()
        # End program if user closes window or
        # presses the Exit button
        if event == "Exit" or event == GUI.WIN_CLOSED:
            break

        # File was chosen
        if event == "-FILE-":
            try:
                file = value["-FILE-"]
            except:
                file = []

    Window.close()
"""

"""
    "1) Open file"
    FileName = input("Enter Your File Name: ")
    FileName = "ST.txt"
    Text = Functions.OpenFile(FileName)

    "2) Create Dictionary"
    CharactersDic = Functions.CreateDictionary()
    CharacterConverter = Functions.Create_CharacterConverter_Dictionary()

    "3) Count Characters"
    print("Counting...")
    Functions.Count(Text, CharactersDic)

    "4) User Enter Number of letters most repeted"
    NoMostReperted = int( input("Enter the number of most repeted letters you want: "))
    SortedCharList = Functions.SortRepetedChar(CharactersDic)
    Functions.PrintMostRepetedChar(NoMostReperted, SortedCharList)

    "5) Plot most repeted letters"
    Functions.PlotMostRepetedChar(NoMostReperted, SortedCharList)
    Functions.PlotAllChar(SortedCharList)

    "6) Change letters to equivalent number for calculations and create array"
    data = Functions.ConvertCharToNum(SortedCharList, CharacterConverter)
    "print(data)" '''For debugging purpose'''
"""
