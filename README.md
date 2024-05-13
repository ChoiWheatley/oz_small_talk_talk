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
python3 sample.py --names "a b c d e" --count 3 --markdown

| 그룹번호 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | a | c | d |
| 1 | b | e |  |
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

