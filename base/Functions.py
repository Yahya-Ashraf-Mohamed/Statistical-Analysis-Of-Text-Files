import numpy as np
import matplotlib.pyplot as plt

Sample_Space = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
                'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
                'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
                's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
                'y', 'Y', 'z', 'Z']

def OpenFile(FileName):
    try:
        FileHandel = open(FileName, 'r')
        text = FileHandel.read()
        FileHandel.close()
        return text
    except:
        return False


def EditFile(FileName, Updated_text):
    try:
        FileHandel = open(FileName, 'w')
        FileHandel.write(Updated_text)
        FileHandel.close()
        return True
    except:
        return False

def Generate_Analysis_File(CheckBox_state, SortedCharList, TotalNumberOfWords):
    Generated_text = "#Character | No. of Repetition | Probability of Occurrence\n" \
                     "============================================================\n"
    if CheckBox_state == 0:
        for value, key in SortedCharList[0:NoMostRepeated]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value/TotalNumberOfWords)) + "\n"
    else:
        for value, key in SortedCharList[0:]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value / TotalNumberOfWords)) + "\n"
    return Generated_text

def Save_Output_File(FileName, CheckBox_state, SortedCharList, TotalNumberOfWords, Mean, Variance, Skewness, Kurtosis):
    try:
        FileHandel = open(FileName, 'w')
        Updated_text =                "        Mean:           " + Mean + " \n"
        Updated_text = Updated_text + "      Variance:         " + Variance + "\n"
        Updated_text = Updated_text + "      Skewness:         " + Skewness + "\n"
        Updated_text = Updated_text + "      Kurtosis:         " + Kurtosis + "\n"
        Updated_text = Updated_text + "Total Number Of Words:  " + str(TotalNumberOfWords) + "\n"
        Updated_text = Updated_text + "============================================================\n"
        Updated_text = Updated_text + Generate_Analysis_File(CheckBox_state, SortedCharList, TotalNumberOfWords)
        FileHandel.write(Updated_text)
        FileHandel.close()
        return True
    except:
        return False

def CreateDictionary():
    Characters = dict()
    for char in Sample_Space:
        Characters[char] = Characters.get(char, 0)
    return Characters


def Create_CharacterConverter_Dictionary():
    CharacterConverter = dict()
    i = 0
    for char in Sample_Space:
        CharacterConverter[char] = CharacterConverter.get(char, 0) + i
        i = i + 1
    return CharacterConverter


def Count_Each_Char(FileHandel, CharactersDic):
    words = FileHandel.split()
    Total_Number_Of_Words = 0
    Total_Distinct_Of_Words = 0
    CharactersDic["Total no. of words"] = Total_Number_Of_Words
    CharactersDic["Total Distinct no. of words"] = Total_Distinct_Of_Words
    for word in words:
        for char in word:
            try:
                if CharactersDic[char] == 0:
                    Total_Distinct_Of_Words = Total_Distinct_Of_Words + 1
                CharactersDic[char] = CharactersDic.get(char, 0) + 1
                Total_Number_Of_Words = Total_Number_Of_Words + 1
            except:
                continue
    CharactersDic["Total no. of words"] = Total_Number_Of_Words
    CharactersDic["Total Distinct no. of words"] = Total_Distinct_Of_Words
    return CharactersDic

def SortRepetedChar(CharactersDic):
    lst = list()
    for key, value in CharactersDic.items():
        newTuple = (value, key)
        lst.append(newTuple)

    lst = sorted(lst, reverse=True)
    return lst
    "print(sorted( [(value,key) for key,value in CharactersDic.items()] , reverse = True) [:NoMostRepeated])"


def Output_Data(SortedCharList, NoMostRepeated):
    text = ""
    counter = 1
    for value, key in SortedCharList[0:NoMostRepeated]:
        if value == 0:
            continue
        text = text + " [" + str(key) + "] " + str(value) + "  "
        if counter == 4:
            text = text + "\n"
            counter = 0
        counter = counter + 1
    return text


def PlotMostRepetedChar(NoMostRepeated, SortedCharList, TotalNumberOfWords):
    if NoMostRepeated > TotalNumberOfWords:
        NoMostRepeated = TotalNumberOfWords
    for value, key in SortedCharList[0:NoMostRepeated]:
        plt.bar(key, value)
    plt.xlabel("Characters")
    plt.ylabel("Probability")
    plt.show()


def PlotAllChar(SortedCharList, TotalNumberOfWords):
    for value, key in SortedCharList[0:TotalNumberOfWords]:
        plt.bar(key, value)
    plt.xlabel("Characters")
    plt.ylabel("No. Repeated")
    plt.show()


def Generate_X_fx(CharactersDic, CharacterConverter, TotalNoOfWords):
    data = dict()
    for key, value in CharacterConverter.items():
        temp = int(CharactersDic[key])/TotalNoOfWords
        data[value] = data.get(value, temp)
    return data


def Generate_PMF(X_fx):
    for value, key in X_fx.items():
        plt.bar(value, key)
    plt.title("PMF")
    plt.xlabel("X")
    plt.ylabel("F(x)")
    plt.show()

def Generate_CDF(X_fx):
    X = []
    PMF = []
    for value, key in X_fx.items():
        X.append(value)
        PMF.append(key)

    # using numpy np.cumsum to calculate the CDF
    CDF = np.cumsum(PMF)
    plt.plot(X[0:], CDF, color="red", label="CDF")
    plt.title("CDF")
    plt.xlabel("X")
    plt.ylabel("F(x)")
    plt.show()


def Calculate_Mean(X_fx):
    "X * Fx"
    Mean = 0
    for X, Fx in X_fx.items():
        Mean = Mean + (X*Fx)
    return Mean


def Calculate_Variance(X_fx):
    "Var = E(x^2) - Mean^2"
    Mean = Calculate_Mean(X_fx)
    E_x2 = []
    for X, Fx in X_fx.items():
        E_x2.append((X**2) * Fx)
    Variance = sum(E_x2) - (Mean**2)
    return Variance


def Calculate_Skewness(X_fx):
    """
        Skew = {Σ[(X**3) * f(x)] - [3 * Mean * Var] - (Mean**3)}
              ---------------------------------------------------
                        [Standard Deviation**3]
    """
    Var = Calculate_Variance(X_fx)
    Standard_Deviation = np.sqrt(Var)
    Mean = Calculate_Mean(X_fx)
    E_x3 = 0
    for X, Fx in X_fx.items():
        if Fx != 0:
            E_x3 = E_x3 + ((int(X)**3) * float(Fx))

    Skew = (E_x3 - (3 * Mean * Var) - (Mean ** 3)) / (Standard_Deviation ** 3)
    return Skew

def Calculate_Kurtosis(X_fx):
    """
        Kurtosis  = [Σ[(X**4) * f(x)] - (4 * Mean * Σ[(X**3) * f(x)]) + (6 * (Mean**2) * Var) + (3 * (Mean**4))]
                    ---------------------------------------------------------------------------------------------
                                        / [Standard Deviation**4]
    """
    Var = Calculate_Variance(X_fx)
    Standard_Deviation = np.sqrt(Var)
    Mean = Calculate_Mean(X_fx)
    E_x3 = 0
    for X, Fx in X_fx.items():
        if Fx != 0:
            E_x3 = E_x3 + ((int(X) ** 3) * float(Fx))

    E_x4 = 0
    for X, Fx in X_fx.items():
        if Fx != 0:
            E_x4 = E_x4 + ((int(X) ** 4) * float(Fx))

    kurtosis = ((E_x4 - (4 * Mean * E_x3) + (6 * (Mean**2) * Var)) + (3 * (Mean**4))) / (Standard_Deviation**4)
    return kurtosis
