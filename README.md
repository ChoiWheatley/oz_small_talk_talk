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
python sample.py --names "다은 기은 길동 황동 과동 승현 재현 우현 재윤 다윤 가윤 라윤 마윤 으악 이름 정하 는게 너무 어려 워요" --count 3 --markdown
```

| 그룹번호 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 는게 | 다윤 | 우현 |
| 1 | 라윤 | 으악 | 과동 |
| 2 | 정하 | 재현 | 황동 |
| 3 | 승현 | 워요 | 너무 |
| 4 | 어려 | 가윤 | 기은 |
| 5 | 마윤 | 길동 | 이름 |
| 6 | 다은 | 재윤 |  |

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

