import numpy as np
import matplotlib.pyplot as plt


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


def CreateDictionary():
    Characters = dict()
    text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in text:
        Characters[char] = Characters.get(char, 0)
    return Characters


def Create_CharacterConverter_Dictionary():
    CharacterConverter = dict()
    text = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
            'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'L', 'l',
            'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
            's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
            'y', 'Y', 'z', 'Z']
    i = 0
    for char in text:
        CharacterConverter[char] = CharacterConverter.get(char, 10) + i
        i = i + 1
    return CharacterConverter


def Count(FileHandel, CharactersDic):
    words = FileHandel.split()
    for word in words:
        for char in word:
            CharactersDic[char] = CharactersDic.get(char, 0) + 1
    return CharactersDic
    '''For debugging purpose'''


def SortRepetedChar(CharactersDic):
    lst = list()
    for key, value in CharactersDic.items():
        newTuple = (value, key)
        lst.append(newTuple)

    lst = sorted(lst, reverse=True)
    return lst
    "print(sorted( [(value,key) for key,value in CharactersDic.items()] , reverse = True) [:NoMostReperted])"



def PlotMostRepetedChar(NoMostReperted, SortedCharList):
    for value, key in SortedCharList[:NoMostReperted]:
        plt.bar(key, value)
    plt.xlabel("Charcters")
    plt.ylabel("No. Repeted")
    plt.show()


def PlotAllChar(SortedCharList):
    for value, key in SortedCharList:
        plt.bar(key, value)
    plt.xlabel("Charcters")
    plt.ylabel("No. Repeted")
    plt.show()


def ConvertCharToNum(CharactersDic, CharacterConverter):
    data = []
    for value, key in CharactersDic:
        print(value, key)
        if (key in CharacterConverter):
            data.append((value * CharacterConverter[key]))
    return data
