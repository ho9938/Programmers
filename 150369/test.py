#!/usr/bin/python3
import sys
sys.setrecursionlimit(1000000)

def cost(cap, n, deliveries, pickups, remD, remP):
    if n < 0:
        return 0

    if deliveries[n] >= remD:
        deliveries[n] -= remD
        remD = 0
    else:
        remD -= deliveries[n]
        deliveries[n] = 0
    
    if pickups[n] >= remP:
        pickups[n] -= remP
        remP = 0
    else:
        remP -= pickups[n]
        pickups[n] = 0

    if deliveries[n] == 0 and pickups[n] == 0:
        return cost(cap, n-1, deliveries, pickups, remD, remP)
    else:
        visit = (max(deliveries[n], pickups[n]) - 1) // cap + 1
        addCost = 2 * visit * (n + 1)
        remD += visit * cap - deliveries[n]
        remP += visit * cap - pickups[n]
        deliveries[n], pickups[n] = 0, 0
        return addCost + cost(cap, n-1, deliveries, pickups, remD, remP)

def solution(cap, n, deliveries, pickups):
    return cost(cap, n-1, deliveries, pickups, 0, 0)

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
    cap = readInput()
    n = readInput()
    deliveries = readInput()
    pickups = readInput()
    
    print(solution(cap, n, deliveries, pickups))