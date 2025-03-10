from typing import List, Optional, Tuple


def read_input() -> str:
    return open("input.txt", "r").read().strip()


def get_disk_layout(disk_map: str) -> List[Optional[int]]:
    disk_layout = []
    curr_file_id = 0
    for idx, file_block_or_free_space in enumerate(disk_map):
        if idx % 2 == 0:
            disk_layout += ([curr_file_id] * int(file_block_or_free_space))
            curr_file_id += 1
        else:
            disk_layout += ([None] * int(file_block_or_free_space))
    return disk_layout


def get_all_free_space_idx(disk_layout: List[Optional[int]]) -> List[int]:
    return [idx for idx, element in enumerate(disk_layout) if element is None]


def get_check_sum(disk_layout: List[Optional[int]]) -> int:
    return sum([idx * element for idx, element in enumerate(disk_layout) if element is not None])


def part_one(disk_map: str) -> int:
    disk_layout = get_disk_layout(disk_map)
    free_space_idx = get_all_free_space_idx(disk_layout)
    right_most_block_idx = len(disk_layout) - 1
    while free_space_idx[0] < right_most_block_idx:
        disk_layout[free_space_idx[0]], disk_layout[right_most_block_idx] = \
            disk_layout[right_most_block_idx], disk_layout[free_space_idx[0]]
        free_space_idx.pop(0)
        while disk_layout[right_most_block_idx] is None:
            right_most_block_idx -= 1

    return get_check_sum(disk_layout)


def get_free_space_idx_and_size(
    disk_map: str) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:

    file_block_idx_and_size = []
    free_space_idx_and_size = []
    curr_file_block_or_free_space_idx = 0
    for idx, file_block_or_free_space in enumerate(disk_map):
        if idx % 2 == 0:
            file_block_idx_and_size.append(
                (curr_file_block_or_free_space_idx, int(file_block_or_free_space))
            )
        else:
            free_space_idx_and_size.append(
                (curr_file_block_or_free_space_idx, int(file_block_or_free_space))
            )
        curr_file_block_or_free_space_idx+= int(file_block_or_free_space)
    return file_block_idx_and_size, free_space_idx_and_size


def part_two(disk_map: str) -> int:
    disk_layout = get_disk_layout(disk_map)
    file_block_idx_and_size, free_space_idx_and_size = get_free_space_idx_and_size(disk_map)
    for file_block_idx, file_block_size in reversed(file_block_idx_and_size):
        for i in range(len(free_space_idx_and_size)):
            free_space_idx, free_space_size = free_space_idx_and_size[i]
            if free_space_idx >= file_block_idx:
                break
            if free_space_size < file_block_size:
                continue
            file_block_to_move = disk_layout[file_block_idx: file_block_idx + file_block_size]
            disk_layout[free_space_idx: free_space_idx + file_block_size] = file_block_to_move
            disk_layout[file_block_idx: file_block_idx + file_block_size] = [None] * file_block_size
            free_space_idx_and_size[i] = (
                free_space_idx + file_block_size, free_space_size - file_block_size
            )
            break

    return get_check_sum(disk_layout)


def main():
    disk_map = read_input()
    check_sum_part_one = part_one(disk_map)
    print("Checksum for part one = {}".format(check_sum_part_one))
    check_sum_part_two = part_two(disk_map)
    print("Checksum for part two = {}".format(check_sum_part_two))


if __name__ == "__main__":
    main()
