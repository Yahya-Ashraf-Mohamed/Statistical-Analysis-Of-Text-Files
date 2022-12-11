import Functions
from tkinter import *
from PIL import ImageTk, Image

"""import PySimpleGUI as GUI
import os.path"""


def GetInputFile():
    # Browse for input file then print its name in the text box
    Output_Label = Label(root, text=input_TextBox.get())
    Output_Label.grid(row=2, column=0)


def AnalyseInputFile():
    print("")


def Execute(New_Plot_Type):
    myLable = Label(root, text=New_Plot_Type)
    myLable.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Statistical Analysis Of Text Files")
    root.iconbitmap('D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Project/Icone.ico')

# Frame 1
    Frame_1 = LabelFrame(root, padx=20, pady=5)

    # Create a Textbox widget
    input_TextBox = Entry(Frame_1, width=50, borderwidth=5, bg="White", fg="Black")
    input_TextBox.insert(0, "Choose the file you want to analysis")

    # Create Buttons
    button_Choose_File = Button(Frame_1, text="Browse File", state=ACTIVE, padx=15, pady=2, fg="blue",
                                command=GetInputFile)
    button_Analysis_File = Button(Frame_1, text="Analyse", state=ACTIVE, padx=15, pady=2, bg="Green",
                                  command=AnalyseInputFile)

# Shoving Frame 1 into the screen
    Frame_1.pack(padx=0, pady=0)
    input_TextBox.grid(row=0, column=0)
    button_Choose_File.grid(row=0, column=4)
    button_Analysis_File.grid(row=1, column=0)

# Frame 2
    Frame_2 = LabelFrame(root, padx=10, pady=50)

    # Create Radio buttons
    MODES = [
        ("PMF", "PMF"),
        ("CDF", "CDF"),
        ("Mean", "Mean"),
        ("Variance", "Variance"),
        ("skewness", "skewness"),
        ("kurtosis", "kurtosis"),
    ]

    PlotType = StringVar()
    PlotType.set("PMF")

    row = column = count = 0
    for text, mode in MODES:
        Radiobutton(Frame_2, text=text, variable=PlotType, value=mode).pack(anchor=W)  # .grid(row=row, column=column)
        if row == 2:
            row = 0
        if count == 2:
            column = 2
        else:
            count = count + 1
        row = row + 1

    # Create Exit buttons
    button_Execute = Button(Frame_2, text="Execute", state=ACTIVE, padx=5, pady=2, bg="Red", command=Execute(PlotType.get()))

# Shoving Frame 2 into the screen
    Frame_2.pack(padx=1, pady=0)

    button_Execute.pack(anchor=W)    # .grid(row=4, column=1)

    # Generate main loop
    root.mainloop()

"""    # Frame 2
    Frame_2 = LabelFrame(root, padx=10, pady=10)
    Frame_2.pack(padx=20, pady=20)
    button_Exit = Button(Frame_2, text="Exit Program", state=ACTIVE, padx=5, pady=2, bg="Red", command=root.quit)

    # Frame 2
    Frame_3 = LabelFrame(root, padx=50, pady=50)
    Frame_3.pack(padx=30, pady=30)
    button_PMF = Button(Frame_3, text="PMF", state=DISABLED, padx=10, pady=5, fg="Green")
    button_CDF = Button(Frame_3, text="CDF", state=DISABLED, padx=10, pady=5, fg="#AA336A")  # dark pink
    button_Mean = Button(Frame_3, text="Mean", state=DISABLED, padx=10, pady=5, fg="orange")
    button_Variance = Button(Frame_3, text="Variance", state=DISABLED, padx=10, pady=5, fg="#8B8000")  # dark yellow
    button_Skewness = Button(Frame_3, text="Skewness", state=DISABLED, padx=10, pady=5, fg="purple")
    button_kurtosis = Button(Frame_3, text="kurtosis", state=DISABLED, padx=10, pady=5, fg="Black")

    # Shoving it into the screen
    input_TextBox.grid(row=0, column=0)
    # Output_Label.grid(row=2, column=0)

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
"""

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
