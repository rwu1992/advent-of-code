import itertools
from typing import Dict, List, Set, Tuple


def parse_map(antenna_map: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    output: Dict[str, List[Tuple[int, int]]] = {}
    for row, line in enumerate(antenna_map):
        for column, char in enumerate(line):
            if char == ".":
                continue
            if char not in output:
                output[char] = [(row, column)]
            else:
                output[char].append((row, column))
    return output


def get_all_antinodes_v1(antenna_map: List[str]) -> Set[Tuple[int, int]]:
    output = set()
    num_rows, num_columns = len(antenna_map), len(antenna_map[0])
    antennas = parse_map(antenna_map)
    for freq_pos in antennas.values():
        for first_pos, second_pos in itertools.combinations(freq_pos, 2):
            diff_rows = first_pos[0] - second_pos[0]
            diff_columns = first_pos[1] - second_pos[1]

            first_antinode = (first_pos[0]+diff_rows, first_pos[1]+diff_columns)
            second_antinode = (second_pos[0]-diff_rows, second_pos[1]-diff_columns)
            if validate_within_bounds(num_rows, num_columns, first_antinode):
                output.add(first_antinode)
            if validate_within_bounds(num_rows, num_columns, second_antinode):
                output.add(second_antinode)
    return output


def get_all_antinodes_v2(antenna_map: List[str]) -> Set[Tuple[int, int]]:
    output = set()
    num_rows, num_columns = len(antenna_map), len(antenna_map[0])
    antennas = parse_map(antenna_map)
    for freq_pos in antennas.values():
        for first_pos, second_pos in itertools.combinations(freq_pos, 2):
            diff_rows = first_pos[0] - second_pos[0]
            diff_columns = first_pos[1] - second_pos[1]

            output.add(first_pos)
            output.add(second_pos)

            antinode_candidate = (first_pos[0] + diff_rows, first_pos[1] + diff_columns)
            while validate_within_bounds(num_rows, num_columns, antinode_candidate):
                output.add(antinode_candidate)
                antinode_candidate = (antinode_candidate[0] + diff_rows, antinode_candidate[1] + diff_columns)

            antinode_candidate = (second_pos[0] - diff_rows, second_pos[1] - diff_columns)
            while validate_within_bounds(num_rows, num_columns, antinode_candidate):
                output.add(antinode_candidate)
                antinode_candidate = (antinode_candidate[0] - diff_rows, antinode_candidate[1] - diff_columns)
    return output


def validate_within_bounds(num_rows: int, num_columns: int, pos: Tuple[int, int]) -> bool:
    return (0 <= pos[0] < num_rows) and (0 <= pos[1] < num_columns)


def main():
    antenna_map = [l.strip() for l in open("input.txt", "r")]
    print("Number of unique antinodes, part 1 = {}".format(len(get_all_antinodes_v1(antenna_map))))
    print("Number of unique antinodes, part 2 = {}".format(len(get_all_antinodes_v2(antenna_map))))


if __name__ == "__main__":
    main()
