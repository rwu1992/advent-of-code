from collections import Counter
from typing import List, Tuple


def read_input() -> Tuple[List[int], List[int]]:
    location_ids1 = []
    location_ids2 = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            ids = [
                location_id
                for location_id in line.split(" ")
                if len(location_id) > 0
            ]
            location_ids1.append(int(ids[0]))
            location_ids2.append(int(ids[1]))
    return location_ids1, location_ids2


def compute_sum_distance(location_ids1: List[int], location_ids2: List[int]) -> int:
    sorted_location_ids1 = sorted(location_ids1)
    sorted_location_ids2 = sorted(location_ids2)
    sum_distances = sum([
        abs(id1 - id2)
        for id1, id2 in zip(sorted_location_ids1, sorted_location_ids2)
    ])
    return sum_distances


def compute_similarity_score(location_ids1: List[int], location_ids2: List[int]) -> int:
    location_ids2_count = Counter(location_ids2)
    return sum([id1 * location_ids2_count[id1] for id1 in location_ids1])


def main():
    location_ids1, location_ids2 = read_input()
    print("Sum of distances = {}".format(compute_sum_distance(location_ids1, location_ids2)))
    print("Similarity score = {}".format(compute_similarity_score(location_ids1, location_ids2)))


if __name__ == "__main__":
    main()
