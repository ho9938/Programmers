#!/usr/bin/python3

def validTree(bits):
    if len(bits) == 1:
        return True

    center = len(bits) // 2
    left = bits[:center]
    right = bits[center+1:]

    if bits[center] == '0' and \
        (left[len(left) // 2] == '1' or right[len(right) // 2] == '1'):
        return False
    else:
        return validTree(left) and validTree(right)
        
def solution(numbers):
    answer = []
    for number in numbers:
        bits = bin(number)[2:]
        compLen = 1
        while len(bits) > compLen:
            compLen = (compLen + 1) * 2 - 1
        for i in range(compLen - len(bits)):
            bits = '0' + bits
        answer.append(int(validTree(bits)))

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
    
if __name__ == '__main__':
    numbers = parseInput(input())
    print(solution(numbers))