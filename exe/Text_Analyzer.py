import Functions
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image


"Sample for text = aab5 "
"""

||=====================================================================||
||  X  | 0 | 1 | 2 | ... |  5  | ... |  a  | A |  b  | B | c | C | ... ||
||-----|---|---|---|-----| --- |-----| --- |---| --- |---|---|---|-----||
||  Fx | 0 | 0 | 0 |  0  | 1/4 |  0  | 2/4 | 0 | 1/4 | 0 | 0 | 0 |  0  ||
||=====================================================================||

X_fx = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.25, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.5,
        11: 0.0, 12: 0.25, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0,
        21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0,
        31: 0.0, 32: 0.0, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 0.0, 38: 0.0, 39: 0.0, 40: 0.0,
        41: 0.0, 42: 0.0, 43: 0.0, 44: 0.0, 45: 0.0, 46: 0.0, 47: 0.0, 48: 0.0, 49: 0.0, 50: 0.0,
        51: 0.0, 52: 0.0, 53: 0.0, 54: 0.0, 55: 0.0, 56: 0.0, 57: 0.0, 58: 0.0, 59: 0.0, 60: 0.0,
        61: 0.0}

"""
"CharactersDic ={'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 1, '6': 0, '7': 0, '8': 0, '9': 0," \
                 "'a': 2, 'b': 1, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0," \
                 " 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0," \
                 " 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0," \
                 " 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0," \
                 " 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0," \
                 " 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Total no. of words': 4," \
                 "'Total Distinct no. of words': 4}"

"CharacterConverter = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9," \
                       "'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19," \
                       "'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29," \
                       "'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39," \
                       "'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49," \
                       "'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59," \
                       "'Y': 60, 'Z': 61}"
"SortedCharList = [(4, 'Total no. of words'), (3, 'Total Distinct no. of words'), (2, 'a'), (1, 'b'), (1, '5')," \
                  "(0, 'z'), (0, 'y'), (0, 'x'), (0, 'w'), (0, 'v'), (0, 'u'), (0, 't'), (0, 's'), (0, 'r'), (0, 'q'),"\
                  "(0, 'p'), (0, 'o'), (0, 'n'), (0, 'm'), (0, 'l'), (0, 'k'), (0, 'j'), (0, 'i'), (0, 'h'), (0, 'g'),"\
                  "(0, 'f'), (0, 'e'), (0, 'd'), (0, 'c'), (0, 'Z'), (0, 'Y'), (0, 'X'), (0, 'W'), (0, 'V'), (0, 'U'),"\
                  "(0, 'T'), (0, 'S'), (0, 'R'), (0, 'Q'), (0, 'P'), (0, 'O'), (0, 'N'), (0, 'M'), (0, 'L'), (0, 'K'),"\
                  "(0, 'J'), (0, 'I'), (0, 'H'), (0, 'G'), (0, 'F'), (0, 'E'), (0, 'D'), (0, 'C'), (0, 'B'), (0, 'A'),"\
                  "(0, '9'), (0, '8'), (0, '7'), (0, '6'), (0, '4'), (0, '3'), (0, '2'), (0, '1'), (0, '0')]"


def Click_Show_TextBox(key):
     # Open analysis button
     button_Analyse_File.configure(state=ACTIVE, bg="Green")
     button_Execute.configure(state=ACTIVE)

# Browse for input file then print its name in the text box
def GetInputFile():
    global FileName
    FileName = filedialog.askopenfilename(initialdir="Home", title="Open Text File",
                                          filetypes=(("Text Files", "*.txt"),))
    Text = Functions.OpenFile(FileName)
    if Text:
        Show_TextBox.delete(1.0, END)
        Show_TextBox.insert(END, Text)
        button_Analyse_File.configure(state=ACTIVE, bg="Green")
        button_Save_Edit_File.configure(state=ACTIVE)
        button_Execute.configure(state=ACTIVE, bg="Red")
        PlotType.set("Analysis")
    else:
        messagebox.showerror("ERROR", "Can't open file!\n")


def Save_Changes_inputFile():
    Updated_text = Show_TextBox.get(1.0, END)
    state = Functions.EditFile(FileName, Updated_text)
    if state == True:
        messagebox.showinfo("Save", "File Saved Successfully!")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + FileName)


def Save_Analysis_File():
    Save_FileName = filedialog.askopenfilename(initialdir="Home", title="Open Text File",
                                               filetypes=(("Text Files", "*.txt"),))
    state = Functions.Save_Output_File(Save_FileName, Check_Value.get(), SortedCharList, TotalNoOfWords, Mean,
                                       Var, Skewness, Kurtosis)
    if state == True:
        messagebox.showinfo("Save", "Analysis Saved Successfully!")
    else:
        messagebox.showerror("ERROR", "Error in Saving!\n" + Save_FileName)


def AnalyseInputFile():
    "1) Create Dictionaries"
    global MVSK
    MVSK = dict()
    MVSK["Mean"] = False
    MVSK["Variance"] = False
    MVSK["Skewness"] = False
    MVSK["Kurtosis"] = False
    global CharactersDic
    global TotalNoOfWords
    TotalNoOfWords = 0
    global TotalDistinctOfWords
    TotalDistinctOfWords = 0
    CharactersDic = Functions.CreateDictionary()
    global CharacterConverter
    CharacterConverter = Functions.Create_CharacterConverter_Dictionary()

    "2) Count Characters"
    CharactersDic = Functions.Count_Each_Char(Show_TextBox.get(1.0, END), CharactersDic)
    TotalDistinctOfWords = CharactersDic["Total Distinct no. of words"]
    TotalNoOfWords = CharactersDic["Total no. of words"]
    del CharactersDic["Total Distinct no. of words"]
    del CharactersDic["Total no. of words"]

    "3) Create our Sample Space and f(x)"
    global X_fx
    X_fx = Functions.Generate_X_fx(CharactersDic, CharacterConverter,TotalNoOfWords)

    "4) Make our Calculations"
    global Mean
    global Var
    global Skewness
    global Kurtosis
    Mean = str(Functions.Calculate_Mean(X_fx))
    Var = str(Functions.Calculate_Variance(X_fx))
    Skewness = str(Functions.Calculate_Skewness(X_fx))
    Kurtosis = str(Functions.Calculate_Kurtosis(X_fx))

    "5) User Enter Number of letters most repeated"
    if Check_Value.get() == 0:
        global NoMostRepeated
        try:
            NoMostRepeated = int(Input_TextBox.get())
            if NoMostRepeated > TotalDistinctOfWords:
                messagebox.showwarning("Warning!",
                                       "The number of characters you want to show exceeds the total number of "
                                       "Characters entered!")
                NoMostRepeated = TotalDistinctOfWords

                Input_TextBox.delete(0, END)
                Input_TextBox.insert(END, str(NoMostRepeated))

        except:
            messagebox.showerror("ERROR", "Enter number of letters you want!\n")
            return
    else:
        NoMostRepeated = TotalDistinctOfWords
    button_Save_Analysis_File.config(state=ACTIVE)
    global SortedCharList
    SortedCharList = Functions.SortRepetedChar(CharactersDic)
    global Output_Text
    Output_Text = Functions.Output_Data(SortedCharList, NoMostRepeated)
    Analysis_Label.configure(text=Output_Text)

def Execute(PlotType):
    global Output_Text
    if Analysis_Label.cget("text") == "":
        AnalyseInputFile()
    match PlotType:
        case "Analysis":
            "Plot analysis for most repeated Characters"
            if Check_Value.get() == 0:
                Functions.PlotMostRepetedChar(NoMostRepeated, SortedCharList, TotalDistinctOfWords)
            else:
                "Plot analysis for All Characters"
                Functions.PlotAllChar(SortedCharList, TotalDistinctOfWords)
            return
        case "PMF":
            "Plot PMF for Characters"
            Functions.Generate_PMF(X_fx)
            return
        case "CDF":
            "Plot CDF for Characters"
            Functions.Generate_CDF(X_fx)
            return
        case "Mean":
            if MVSK["Mean"] == True:
                messagebox.showinfo("Mean", Mean)
                return
            messagebox.showinfo("Mean", Mean)
            Temp_Text = Output_Text
            Output_Text = "Mean = " + Mean + "\n"
            Output_Text = Output_Text + "==============================\n"
            Output_Text = Output_Text + Temp_Text
            Analysis_Label.configure(text=Output_Text)
            MVSK["Mean"] = True
            return
        case "Variance":
            if MVSK["Variance"] == True:
                messagebox.showinfo("Variance", Var)
                return
            messagebox.showinfo("Variance", Var)
            Temp_Text = Output_Text
            Output_Text = "Variance = " + Var + "\n"
            Output_Text = Output_Text + "==============================\n"
            Output_Text = Output_Text + Temp_Text
            Analysis_Label.configure(text=Output_Text)
            MVSK["Variance"] = True
            return
        case "Skewness":
            if MVSK["Skewness"] == True:
                messagebox.showinfo("Skewness", Skewness)
                return
            messagebox.showinfo("Skewness", Skewness)
            Temp_Text = Output_Text
            Output_Text = "Skewness = " + Skewness + "\n"
            Output_Text = Output_Text + "==============================\n"
            Output_Text = Output_Text + Temp_Text
            Analysis_Label.configure(text=Output_Text)
            MVSK["Skewness"] = True
            return
        case "Kurtosis":
            if MVSK["Kurtosis"] == True:
                messagebox.showinfo("Kurtosis", Kurtosis)
                return
            messagebox.showinfo("Kurtosis", Kurtosis)
            Temp_Text = Output_Text
            Output_Text = "Kurtosis = " + Kurtosis + "\n"
            Output_Text = Output_Text + "==============================\n"
            Output_Text = Output_Text + Temp_Text
            Analysis_Label.configure(text=Output_Text)
            MVSK["Kurtosis"] = True
            return
        case default:
            return


if __name__ == "__main__":
    root = Tk()
    root.geometry("735x550")
    root.title("Statistical Analysis Of Text Files")
    root.iconbitmap(
        'D:/Self Development/Zewail collage material/Academic years/Year 3/Probability/Project/base/Icone.ico')



# Frame 1
    Frame_1 = LabelFrame(root, padx=10, pady=22)

    # Create a Textbox widget
    Input_TextBox = Entry(Frame_1, width=50, borderwidth=5, bg="White", fg="Black")
    Input_TextBox.insert(0, "Enter Number of letters you want to display")

    # Create Buttons
    button_Choose_File = Button(Frame_1, text="Browse File", state=ACTIVE, padx=22, pady=2, fg="blue",
                                command=lambda: GetInputFile())
    button_Analyse_File = Button(Frame_1, text="Analyse", state=DISABLED, padx=15, pady=2,
                                 command=lambda: AnalyseInputFile())

    button_Save_Edit_File = Button(Frame_1, text="Save Changes", state=DISABLED, padx=15, pady=2, fg="Black",
                                   command=lambda: Save_Changes_inputFile())

    # Create CheckBox
    Check_Value = IntVar()
    CheckBox_all_Char = Checkbutton(Frame_1, text="All Characters", variable=Check_Value)

# Shoving Frame 1 into the screen
    Frame_1.grid(row=0, column=0)
    Input_TextBox.grid(row=0, column=0)
    button_Choose_File.grid(row=0, column=1)
    button_Analyse_File.grid(row=2, column=0)
    button_Save_Edit_File.grid(row=2, column=1)
    CheckBox_all_Char.grid(row=1, column=0)

# Frame 3
    Frame_3 = LabelFrame(root, padx=0, pady=0)

    # Create a Textbox widget
    Show_TextBox = Text(Frame_3, width=55, borderwidth=2, bg="White", fg="Black")

    # Shoving Frame 3 into the screen
    Frame_3.grid(row=1, column=0)
    Show_TextBox.grid(row=0, column=0)

# Frame 2
    Frame_2 = LabelFrame(root, padx=0, pady=0)

    # Create Radio buttons
    MODES = [
        ("PMF", "PMF"),
        ("CDF", "CDF"),
        ("Mean", "Mean"),
        ("Analysis", "Analysis"),
        ("Variance", "Variance"),
        ("Skewness", "Skewness"),
        ("Kurtosis", "Kurtosis"),
    ]

    PlotType = StringVar()
    PlotType.set("Analysis")

    row = column = count = 0
    for text, mode in MODES:
        Radiobutton(Frame_2, text=text, variable=PlotType, value=mode).grid(row=row, column=column)
        if row == 1 & column == 1:
            row = 0
            column = 2
            continue
        row = row + 1
        if row == 3:
            row = 1
            column = 1

    # Create buttons
    button_Execute = Button(Frame_2, text="Execute", state=DISABLED, padx=5, pady=2, command=lambda: Execute(PlotType.get()))
    button_Save_Analysis_File = Button(Frame_2, text="Save Analysis", state=DISABLED, padx=15, pady=2, fg="Black",
                                       command=lambda: Save_Analysis_File())

# Shoving Frame 2 into the screen
    Frame_2.grid(row=0, column=1)
    button_Execute.grid(row=4, column=0)
    button_Save_Analysis_File.grid(row=4, column=2)


# Frame 4
    Frame_4 = LabelFrame(root, padx=0, pady=0)

    # Create a Textbox widget
    Analysis_Label = Label(Frame_4, text='', width=34, height=24, borderwidth=2, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left", wraplength=240)

# Shoving Frame 4 into the screen
    Frame_4.grid(row=1, column=1)
    Analysis_Label.grid(row=0, column=0)
    Analysis_Label.pack_propagate(0)


    Show_TextBox.bind("<Key>", Click_Show_TextBox)

# Generate main loop
    root.mainloop()
