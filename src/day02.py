def process_even_case(n1: str, n2: str) -> list[int]:
    """Assuming len(n1) == len(n2) (and len(n1) is even)"""
    invalid_ids = []
    length = len(n1)
    start = int(n1[0 : length // 2])
    end = int(n2[0 : length // 2])
    for half in range(start, end + 1):
        candidate = int(str(half) * 2)
        if (candidate >= int(n1)) & (candidate <= int(n2)):
            invalid_ids.append(candidate)
    return invalid_ids


if __name__ == "__main__":
    with open("./inputs/day02/input.txt") as f:
        ranges = f.read().rstrip("\n")

    res_part_1 = 0

    for r in ranges.split(","):
        #print(f"=== {r=}")
        n1, n2 = r.split("-")
        l1 = len(n1)
        l2 = len(n2)
        if l2 - l1 > 1:
            raise NotImplementedError(
                "I expect second number to have the same number of digits"
                " than the first one, or at most one extra digit"
            )
        if l1 != l2:
            if l1 % 2 == 0:
                new_n1 = n1
                new_n2 = str(10**l1 - 1)
            else:
                new_n1 = str(10**l1)
                new_n2 = n2
        else:
            if l1 % 2 == 0:
                new_n1 = n1
                new_n2 = n2
            else:
                continue
        #print(f"{new_n1=} {new_n2=}")
        res = process_even_case(new_n1, new_n2)
        #print(res)
        res_part_1 += sum(res)
    print(f"{res_part_1=}")
