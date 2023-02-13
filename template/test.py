#!/usr/bin/python3

def solution():
    return 0
    
def readInput():
    inputList = [elem.strip('"[] ') for elem in input().strip().split(',')]

    # change type if int or float
    if inputList[0].replace('-', '', 1).isdigit():
        inputList = [int(elem) for elem in inputList]
    elif inputList[0].replace('-', '', 1).replace('.', '', 1).isdigit():
        inputList = [float(elem) for elem in inputList]

    # change type if not list
    if len(inputList) == 1:
        return inputList[0]
    else:
        return inputList
    
if __name__ == '__main__':
    print(solution())