import numpy as np


def checkS(message, dictK:dict):
    a = message.replace(",", ".").split(" ")
    x = float(a[0]) / 1000
    h = float(a[1])
    y = float(a[2]) / 1000
    key = a[3]

    dictK.update({key:[x,y]})

    return dictK

def formList(dictK:dict):
    x = []
    y = []
    lst = list(dictK.values())
    for items in lst:
        x.append(items[0])
        y.append(items[1])

    return (x, y)




