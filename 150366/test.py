#!/usr/bin/python3

class Cell:
    def __init__(self):
        self.value = ''
        self.prev = -1
        self.next = -1
    
def idx(r, c):
    return 50 * (r-1) + (c-1)

def initialIdx(cells, idx):
    if cells[idx].prev == -1:
        return idx
    else:
        return initialIdx(cells, cells[idx].prev)

def finalIdx(cells, idx):
    if cells[idx].next == -1:
        return idx
    else:
        return finalIdx(cells, cells[idx].next)

def isMerged(cells, idx1, idx2):
    idx = idx1
    while idx != -1:
        if idx == idx2:
            return True
        idx = cells[idx].prev
    idx = idx1
    while idx != -1:
        if idx == idx2:
            return True
        idx = cells[idx].next
    return False

def solution(commands):
    answer = []

    cells = []
    for i in range(50 * 50):
        cells.append(Cell())

    for command in commands:
        argList = command.split()
        if argList[0] == 'UPDATE' and len(argList) == 4:
            r, c = int(argList[1]), int(argList[2])
            value = argList[3]
            cells[finalIdx(cells, idx(r,c))].value = value
        elif argList[0] == 'UPDATE' and len(argList) == 3:
            value1, value2 = argList[1], argList[2]
            for i in range(50 * 50):
                if cells[i].value == value1:
                    cells[i].value = value2
        elif argList[0] == 'MERGE':
            r1, c1 = int(argList[1]), int(argList[2])
            r2, c2 = int(argList[3]), int(argList[4])
            if isMerged(cells, idx(r1,c1), idx(r2,c2)):
                continue
            f1 = finalIdx(cells, idx(r1,c1))
            f2 = finalIdx(cells, idx(r2,c2))
            if cells[f1].value == '':
                i2 = initialIdx(cells, idx(r2,c2))
                cells[f1].next = i2
                cells[f1].value = ''
                cells[i2].prev = f1
            else:
                i1 = initialIdx(cells, idx(r1,c1))
                cells[f2].next = i1
                cells[f2].value = ''
                cells[i1].prev = f2
        elif argList[0] == 'UNMERGE':
            r, c = int(argList[1]), int(argList[2])
            cells[idx(r,c)].value = cells[finalIdx(cells, idx(r,c))].value
            i = cells[idx(r,c)].prev
            while i != -1:
                tmp = cells[i].prev
                cells[i] = Cell()
                i = tmp
            cells[idx(r,c)].prev = -1
            i = cells[idx(r,c)].next
            while i != -1:
                tmp = cells[i].next
                cells[i] = Cell()
                i = tmp
            cells[idx(r,c)].next = -1
        elif argList[0] == 'PRINT':
            r, c = int(argList[1]), int(argList[2])
            result = cells[finalIdx(cells, idx(r,c))].value
            if result == '':
                answer.append('EMPTY')
            else:
                answer.append(result)
        
    return answer
    
def parseInput(token: str):
    token = token.strip()

    if token[0] == '[':
        assert(token[-1] == ']')

        resList = []
        start, end, pNum = 1, 1, 0

        while end < len(token) - 1:
            if token[end] == '[':
                pNum += 1
            elif token[end] == ']':
                pNum -= 1
            elif token[end] == ',' and pNum == 0:
                resList.append(parseInput(token[start:end]))
                start = end + 1
            end += 1

        assert(pNum == 0)
        resList.append(parseInput(token[start:end]))

        return resList
    else:
        if token.replace('-', '', 1).isdigit():
            return int(token)
        elif token.replace('-', '', 1).replace('.', '', 1).isdigit():
            return float(token)
        elif token[0] == '"' or token[0] == "'":
            return token[1:-1]
        else:
            return token
    
if __name__ == '__main__':
    commands = parseInput(input())
    print(solution(commands))