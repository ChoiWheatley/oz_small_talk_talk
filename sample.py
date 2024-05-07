# /usr/bin/python3
"""
argparse tutorial: https://docs.python.org/3/howto/argparse.html#argparse-tutorial

N개의 bin에 M명의 수강생을 골고루 담는 법

random.sample(names, M)
"""


import random
import math
import argparse


def make_markdown_table(array):
    """the same input as above"""

    nl = "\n"

    markdown = nl
    markdown += f"| {' | '.join(array[0])} |"

    markdown += nl
    markdown += f"| {' | '.join(['---']*len(array[0]))} |"

    markdown += nl
    for entry in array[1:]:
        markdown += f"| {' | '.join(entry)} |{nl}"

    return markdown


parser = argparse.ArgumentParser(
    prog="human_placement",
    description="이 프로그램은 스몰톡톡 세션을 진행하기 전에 인원들을 랜덤으로 배치하기 위해 만들어졌습니다.",
    epilog="^___^b",
)

parser.add_argument(
    "--names",
    type=str,
    help="whitespace-separated, surrounded by quotation mark",
    required=True,
)
parser.add_argument("--count", type=int, help="group size", required=True)
parser.add_argument("--markdown", action="store_true")
parser.add_argument("--csv", action="store_true")

args = parser.parse_args()
names = args.names.strip().split(" ")
is_markdown = args.markdown
is_csv = args.csv

COUNT = args.count
NUMBER_OF_GROUP = math.ceil(len(names) / COUNT)

# 랜덤으로 인원을 섞습니다
names = random.sample(names, len(names))

if is_markdown:

    names = [str(i) for i in range(1, COUNT + 1)] + names
    # 이차원 배열로 변환합니다
    names = [names[i : i + COUNT] for i in range(0, len(names), COUNT)]

    print(make_markdown_table(names))

elif is_csv:

    pass  # TODO - 2차원 리스트 csv 변환하기

else:

    # 선택된 이름들을 COUNT명씩 출력합니다
    for i in range(NUMBER_OF_GROUP):
        for j in range(COUNT):
            idx = i * COUNT + j
            if idx >= len(names):
                break
            print(names[idx], end=" ")
        print()
