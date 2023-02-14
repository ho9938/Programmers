#!/usr/bin/python3

def readNth2bits(bitArr, idx):
    return (bitArr >> (2 * idx)) & 0b11

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]

    pSums = []
    for bitArr in range(pow(4, len(emoticons))):
        pSum = [0, 0, 0, 0]
        for idx in range(len(emoticons)):
            pSum[readNth2bits(bitArr, idx)] += emoticons[idx]
        pSums.append(pSum)
    
    maxJoin, maxSale = 0, 0
    for pSum in pSums:
        join, sale = 0, 0
        for user in users:
            spend = 0
            for idx in range(len(discounts)):
                if discounts[idx] < user[0]:
                    continue
                spend += pSum[idx] * (100 - discounts[idx]) // 100
            if spend >= user[1]:
                join += 1
            else:
                sale += spend
        if (join > maxJoin) or (join == maxJoin and sale > maxSale):
            maxJoin, maxSale = join, sale
    
    return [maxJoin, maxSale]
    
    
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
    users = parseInput(input())
    emoticons = parseInput(input())
    print(solution(users, emoticons))