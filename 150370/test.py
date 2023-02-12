#!/usr/bin/python3

def solution(today, terms, privacies):
    answer = []

    today = today.split('.')
    tYear = int(today[0])
    tMonth = int(today[1])
    tDay = int(today[2])
    tDays = 28 * (12 * tYear + tMonth) + tDay

    periods = {}
    for term in terms:
        term = term.split(' ')
        periods[term[0]] = int(term[1])
    
    for i in range(len(privacies)):
        privacy = privacies[i].split(' ')
        xYear = int(privacy[0].split('.')[0])
        xMonth = int(privacy[0].split('.')[1])
        xDay = int(privacy[0].split('.')[2])
        period = periods[privacy[1]]

        xDays = 28 * (12 * xYear + xMonth) + xDay
        xDays += 28 * period

        if tDays >= xDays:
            answer.append(i+1)
            
    return answer

if __name__ == '__main__':
    today = input().strip().strip('"')
    terms = [elem.strip('"[] ') for elem in input().strip().split(',')]
    privacies = [elem.strip('"[] ') for elem in input().strip().split(',')]

    print(solution(today, terms, privacies))
