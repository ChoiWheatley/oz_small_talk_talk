# oz_small_talk_talk
스몰톡톡 인원 배치를 랜덤으로 하기 위한 스크립트

## sample.py

```
python3 sample.py --help
```

```
usage: human_placement [-h] --names NAMES --count COUNT [--markdown] [--csv]

이 프로그램은 스몰톡톡 세션을 진행하기 전에 인원들을 랜덤으로 배치하기 위해 만들어졌습니다.

options:
  -h, --help     show this help message and exit
  --names NAMES  whitespace-separated, surrounded by quotation mark
  --count COUNT  group size
  --markdown
  --csv

^___^b
```

> 예시

```
python sample.py \
  --names "다은 기은 길동 황동 과동 승현 재현 우현 재윤 다윤 가윤 라윤 마윤 으악 이름 정하 는게 너무 어려 워요" \
  --count 3 \
  --markdown
```

| 그룹 \ 멤버 | member 0 | member 1 | member 2 |
| --- | --- | --- | --- |
| group 0 | 황동 | 라윤 | 는게 |
| group 1 | 어려 | 재현 | 정하 |
| group 2 | 길동 | 워요 | 승현 |
| group 3 | 너무 | 이름 | 기은 |
| group 4 | 과동 | 마윤 | 다윤 |
| group 5 | 우현 | 으악 | 가윤 |
| group 6 | 재윤 | 다은 |  |

```
python sample.py \
  --names "다은 기은 길동 황동 과동 승현 재현 우현 재윤 다윤 가윤 라윤 마윤 으악 이름 정하 는게 너무 어려 워요" \
  --count 3 \
  --csv

그룹\멤버,member0,member1,member2
group0,너무,과동,으악
group1,정하,어려,기은
group2,마윤,재현,재윤
group3,는게,이름,가윤
group4,황동,우현,길동
group5,다윤,라윤,다은
group6,승현,워요,
```

## groups.py

```
usage: 두 그룹 간에 set 연산 [-h] --group1 GROUP1 --group2 GROUP2 [--operation OPERATION]

이 프로그램은 두 그룹 사이에 AND, OR, XOR 집합연산을 간단하게 지원하는 프로그램입니다.

options:
  -h, --help            show this help message and exit
  --group1 GROUP1       whitespace-separated surrounded by quotation mark
  --group2 GROUP2       whitespace-separated surrounded by quotation mark
  --operation OPERATION
                        [union | intersection | difference | symmetric_difference]

^_______^b
```

