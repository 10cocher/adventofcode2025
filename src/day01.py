def get_score(position: int, position_temp: int) -> int:
    if position_temp == 0:
        score = 1
    else:
        score = abs(position_temp) // 100 + (position * position_temp < 0)
    return score


if __name__ == "__main__":
    with open("./inputs/day01/input.txt") as f:
        lines = f.readlines()

    position = 50
    res_part_1 = 0
    res_part_2 = 0

    for i, line in enumerate(lines):
        line = line.rstrip("\n")
        sign = 1 if line[0] == "R" else -1
        offset = int(line[1:])
        position_temp = position + sign * offset
        score = get_score(position, position_temp)
        res_part_2 += score
        position = position_temp % 100
        if position == 0:
            res_part_1 += 1
    print(f"{res_part_1=}")
    print(f"{res_part_2=}")
