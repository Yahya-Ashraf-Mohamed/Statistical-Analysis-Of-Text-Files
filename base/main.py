import Functions
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image


def Click_Show_TextBox(key):
     # Open analysis button
     button_Analyse_File.configure(state=ACTIVE, bg="Green")

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
    Updated_text = Show_TextBox.get(1.0, END)
    Functions.EditFile(FileName, Updated_text)


def AnalyseInputFile():
    "1) Create Dictionary"
    CharactersDic = Functions.CreateDictionary()
    CharacterConverter = Functions.Create_CharacterConverter_Dictionary()

    "2) Count Characters"
    test = Functions.Count(Show_TextBox.get(1.0, END), CharactersDic)

    "3) User Enter Number of letters most repeted"
    try:
        NoMostReperted = int(Input_TextBox.get())
    except:
        messagebox.showerror("ERROR", "Enter number of letters you want!\n")
    SortedCharList = Functions.SortRepetedChar(CharactersDic)
    text = ""
    counter = 1
    for value, key in SortedCharList[:NoMostReperted]:
        text = text + " [" + str(key) + "] " + str(value) + "   "
        if counter == 4:
            text = text + "\n"
            counter = 0
        counter = counter + 1
    Analysis_Label.configure(text=text)



def Execute():
    button_Save_Analysis_File.configure(state=ACTIVE)


if __name__ == "__main__":
    root = Tk()
    root.geometry("700x550")
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

# Shoving Frame 1 into the screen
    Frame_1.grid(row=0, column=0)
    Input_TextBox.grid(row=0, column=0)
    button_Choose_File.grid(row=0, column=1)
    button_Analyse_File.grid(row=2, column=0)
    button_Save_Edit_File.grid(row=2, column=1)

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
        ("skewness", "skewness"),
        ("kurtosis", "kurtosis"),
    ]

    PlotType = StringVar()

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
    button_Execute = Button(Frame_2, text="Execute", state=DISABLED, padx=5, pady=2, command=Execute)
    button_Save_Analysis_File = Button(Frame_2, text="Save Analysis", state=DISABLED, padx=15, pady=2, fg="Black",
                                       command=Save_Analysis_File)

# Shoving Frame 2 into the screen
    Frame_2.grid(row=0, column=1)
    button_Execute.grid(row=4, column=0)
    button_Save_Analysis_File.grid(row=4, column=2)


# Frame 4
    Frame_4 = LabelFrame(root, padx=0, pady=0)

    # Create a Textbox widget
    Analysis_Label = Label(Frame_4, text='', width=29, height=24, borderwidth=2, bg="White", fg="Black",
                           font=('Helvetica', 10), justify="left", wraplength=240)

# Shoving Frame 4 into the screen
    Frame_4.grid(row=1, column=1)
    Analysis_Label.grid(row=0, column=0)
    Analysis_Label.pack_propagate(0)


    Show_TextBox.bind("<Key>", Click_Show_TextBox)

# Generate main loop
    root.mainloop()


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
