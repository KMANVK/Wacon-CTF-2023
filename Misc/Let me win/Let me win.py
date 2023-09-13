import os
import requests
from Crypto.Util.number import *

team_n = 61

reqscore = open("reqscore", "r").read().split("\n")
assert len(reqscore) == team_n

db = {'Upper Guesser': [3, 4, 5, 7, 8, 9, 10, 11, 15, 16, 17, 18, 20, 22, 23, 25, 26, 28, 29, 30, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 49], ... 'squareimentary': [0, 2, 3, 5, 7, 11, 16, 17, 22, 23, 29, 30, 33, 37, 38, 41, 43, 44, 46]}

assert len(db) == team_n

tot = []

for k in db:
    tot += db[k]

solves = [0] * 50

for i in range(50):
    solves[i] = tot.count(i)

for team in db:
    res = []
    for k in db[team]:
        res.append(solves[k])
    res.sort()

    db[team] = res

# print(db)

from z3 import *

s = Solver()

arr = [Int('arr[%d]'%i) for i in range(61)]

for i in range(61):
    s.add(arr[i] > 0)

# print(arr)

sc = [0] * 62

sc[61] = arr[60]

for i in range(60, 0, -1):
    sc[i] = sc[i + 1] + arr[i - 1]

for i in range(60):
    higher_score = 0
    for k in db[reqscore[i]]:
        higher_score += sc[k]

    lower_score = 0
    for k in db[reqscore[i + 1]]:
        lower_score += sc[k]

    # print(higher_score)

    s.add(higher_score > lower_score)

print(s.check())

arr = s.model()

arr[0]
arr = [0] * 61

arr[11] = 26,
arr[22] = 53,
...
arr[47] = 1,
arr[59] = 15,

for i in range(61):
    arr[i] = arr[i][0]

# print(arr)

score = [0] * 62
score[61] = arr[60]

for i in range(60, 0, -1):
    score[i] = score[i + 1] + arr[i - 1]

print(score[1:])