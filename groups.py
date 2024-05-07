import argparse


parser = argparse.ArgumentParser(
    prog="두 그룹 간에 set 연산",
    description="이 프로그램은 두 그룹 사이에 AND, OR, XOR 집합연산을 간단하게 지원하는 프로그램입니다.",
    epilog="^_______^b",
)

parser.add_argument(
    "--group1",
    type=str,
    help="whitespace-separated surrounded by quotation mark",
    required=True,
)
parser.add_argument(
    "--group2",
    type=str,
    help="whitespace-separated surrounded by quotation mark",
    required=True,
)
parser.add_argument(
    "--operation",
    type=str,
    help="[union | intersection | difference | symmetric_difference]",
    default="union",
)

args = parser.parse_args()

group1 = set(args.group1.strip().split())
group2 = set(args.group2.strip().split())
operation_str = args.operation.strip()

operation = lambda x, y: x | y

match operation_str:
    case "union":
        operation = lambda x, y: x | y
    case "intersection":
        operation = lambda x, y: x & y
    case "difference":
        operation = lambda x, y: x - y
    case "symmetric_difference":
        operation = lambda x, y: x ^ y

output = operation(group1, group2)
print("", ",".join(output))
print(f"total: {len(output)}")
