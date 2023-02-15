#!/usr/bin/python3

def solution():
    return 0
    
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
    print(solution())