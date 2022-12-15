import numpy as np
import matplotlib.pyplot as plt
import statistics

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
    Generated_text = "#Character | No. of Repetition | Probability of Occurrence\n"
    if CheckBox_state == 0:
        for value, key in SortedCharList[2:NoMostRepeated]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value/TotalNumberOfWords)) + "\n"
    else:
        for value, key in SortedCharList[2:]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value / TotalNumberOfWords)) + "\n"
    return Generated_text

def Save_Output_File(FileName, CheckBox_state, SortedCharList, TotalNumberOfWords, X_fx):
    Updated_text = str(Functions.Calculate_Mean(X_fx))
    try:
        FileHandel = open(FileName, 'w')
        Updated_text = "Mean: " + str(Functions.Calculate_Mean(X_fx)) + " \n"
        Updated_text = Updated_text + "Variance: " + str(Calculate_Variance(X_fx)) + "\n"
        Updated_text = Updated_text + "skewness: " + str(Calculate_skewness(X_fx)) + "\n"
        Updated_text = Updated_text + "kurtosis: " + str(Calculate_kurtosis(X_fx)) + "\n"
        Updated_text = Updated_text + "============================================================================\n"
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
            if CharactersDic[char] == 0:
                Total_Distinct_Of_Words = Total_Distinct_Of_Words + 1
            CharactersDic[char] = CharactersDic.get(char, 0) + 1
            Total_Number_Of_Words = Total_Number_Of_Words + 1
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


def Calculate_skewness(X_fx):
    "Skew = 3 * (Mean – Median) / Standard Deviation"
    Var = Calculate_Variance(X_fx)
    Standerd_Deviation = np.sqrt(Var)
    Mean = Calculate_Mean(X_fx)
    Sorted_X = []
    for X, Fx in X_fx.items():
        if Fx == 0:
            continue
        Sorted_X.append(int(X))
    Median = statistics.median(Sorted_X)

    Skew = 3*(Mean-Median)/Standerd_Deviation
    return Skew

def Calculate_kurtosis(X_fx):
    "Kurtosis  = Σ(xi - x̅)4/(n-1)(SD4)"
    """x̅ = Mean (average of all data points)
       xi = Value of each data point
       n = Sample size
       SD = Standard Deviation
"""
    Mean = Calculate_Mean(X_fx)
    Sample_size = 0
    ΣXi_X = 0
    for X, Fx in X_fx.items():
        if Fx == 0:
            continue
        Sample_size = Sample_size + 1
        ΣXi_X = ΣXi_X + (X-Mean)**4
    Var = Calculate_Variance(X_fx)
    Standerd_Deviation = np.sqrt(Var)

    kurtosis = (ΣXi_X)/((Sample_size - 1)*(Standerd_Deviation**4))
    return kurtosis
