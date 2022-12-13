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

def Generate_Analysis_File(CheckBox_state, SortedCharList, CharactersDic):
    Generated_text = "#Character | No. of Repetition | Probability of Occurrence\n"
    if CheckBox_state == 0:
        for value, key in SortedCharList[1:NoMostReperted]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value/CharactersDic["Total no. of words"])) + "\n"
    else:
        for value, key in SortedCharList[1:]:
            Generated_text = Generated_text + "    [" + str(key) + "]    |" + "        " + str(value) + "        " + \
                             "| " + str((value / CharactersDic["Total no. of words"])) + "\n"
    return Generated_text
def Save_Output_File(FileName, Updated_text):
    try:
        FileHandel = open(FileName, 'w')
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
    TotalNumberOfWords = 0
    CharactersDic["Total no. of words"] = TotalNumberOfWords
    for word in words:
        for char in word:
            CharactersDic[char] = CharactersDic.get(char, 0) + 1
            TotalNumberOfWords = TotalNumberOfWords + 1
    CharactersDic["Total no. of words"] = TotalNumberOfWords
    return CharactersDic

def SortRepetedChar(CharactersDic):
    lst = list()
    for key, value in CharactersDic.items():
        newTuple = (value, key)
        lst.append(newTuple)

    lst = sorted(lst, reverse=True)
    return lst
    "print(sorted( [(value,key) for key,value in CharactersDic.items()] , reverse = True) [:NoMostReperted])"



def PlotMostRepetedChar(NoMostReperted, SortedCharList, TotalNumberOfWords):
    for value, key in SortedCharList[1:NoMostReperted]:
        plt.bar(key, value/TotalNumberOfWords)
    plt.xlabel("Characters")
    plt.ylabel("Probability")
    plt.show()


def PlotAllChar(SortedCharList, TotalNumberOfWords):
    for value, key in SortedCharList[1:]:
        plt.bar(key, value/TotalNumberOfWords)
    plt.xlabel("Characters")
    plt.ylabel("No. Repeated")
    plt.show()


def Generate_X_fx(CharactersDic, CharacterConverter):
    data = dict()
    for key, value in CharacterConverter.items():
        temp = int(CharactersDic[key])/int(CharactersDic['Total no. of words'])
        data[value] = data.get(value, temp)
    return data


def Calculate_Mean(X_fx):
    Mean = 0
    for key, value in X_fx.items():
        Mean = Mean + (value*key)
    return Mean