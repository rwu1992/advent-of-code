from typing import List, Tuple

def read_input() -> List[str]:
    return open("input.txt", "r").read().split("\n")


def count_xmas_word(lines: List[str]) -> int:
    count = 0
    num_lines = len(lines)
    num_chars = len(lines[0])

    for x in range(num_lines):
        for y in range(num_chars):
            for direction in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                for pos, target_char in enumerate("XMAS"):
                    search_x = x + (pos * direction[0])
                    search_y = y + (pos * direction[1])
                    if not 0 <= search_x < num_lines:
                        break
                    if not 0 <= search_y < num_chars:
                        break
                    if lines[x + (pos*direction[0])][y + (pos*direction[1])] != target_char:
                        break
                else:
                    count += 1
    return count


def count_x_mas_word(lines: List[str]) -> int:
    count = 0
    num_lines = len(lines)
    num_chars = len(lines[0])

    for x in range(num_lines):
        for y in range(num_chars):
            if lines[x][y] != "A":
                continue

            for direction in [(-1, 1), (1, 1)]:
                start_x, start_y = x + direction[0], y + direction[1]
                end_x, end_y = x - direction[0], y - direction[1]
                if not 0 <= start_x < num_lines:
                    break
                if not 0 <= end_x < num_lines:
                    break
                if not 0 <= start_y < num_chars:
                    break
                if not 0 <= end_y < num_chars:
                    break
                if (lines[start_x][start_y] != "M" or lines[end_x][end_y] != "S") and (lines[start_x][start_y] != "S" or lines[end_x][end_y] != "M"):
                    break
            else:
                count += 1
    return count


if __name__ == "__main__":
    input_lines = read_input()
    print("Num of XMAS = {}".format(count_xmas_word(input_lines)))
    print("Num of X-MAS = {}".format(count_x_mas_word(input_lines)))
