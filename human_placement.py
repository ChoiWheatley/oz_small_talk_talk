#/usr/bin/python3
"""
argparse tutorial: https://docs.python.org/3/howto/argparse.html#argparse-tutorial

N개의 bin에 M명의 수강생을 골고루 담는 법

random.sample(names, M)
"""


import random
import math
import argparse


parser = argparse.ArgumentParser(
        prog="human_placement",
        description="이 프로그램은 스몰톡톡 세션을 진행하기 전에 인원들을 랜덤으로 배치하기 위해 만들어졌습니다.",
        epilog="^___^b")

parser.add_argument("--names", type=str, help="whitespace-separated, surrounded by quotation mark", default="")
parser.add_argument("--count", type=int, help="group size", default=3)

args = parser.parse_args()

names = args.names.strip().split(" ")
COUNT = args.count
NUMBER_OF_GROUP = math.ceil(len(names) / COUNT)

# 랜덤으로 인원을 섞습니다
names = random.sample(names, len(names))

# 선택된 이름들을 COUNT명씩 출력합니다
for i in range(NUMBER_OF_GROUP):
    for j in range(COUNT):
        idx = i * COUNT + j
        if idx >= len(names):
            break
        print(names[idx], end=" ")
    print()

