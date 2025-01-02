from operator import itemgetter
from typing import List, Dict, Set, Tuple


def parse_input() -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    rules: Dict[int, Set[int]] = {}
    updates: List[List[int]] = []
    with open("input.txt", "r") as f:
        for line in f:
            if "|" in line:
                predecessor, successor = [int(x) for x in line.split("|")]
                if predecessor in rules:
                    rules[predecessor].add(successor)
                else:
                    rules[predecessor] = {successor}
            elif "," in line:
                updates.append([int(x) for x in line.split(",")])

    return rules, updates


def get_middle_pages_from_correctly_ordered_updates(rules: Dict[int, Set[int]], updates: List[List[int]]) -> List[int]:
    middle_pages: List[int] = []
    for update in updates:
        if is_correctly_ordered_update(rules, update):
            middle_pages.append(update[len(update) // 2])
    return middle_pages


def get_middle_pages_from_incorrectly_ordered_updates(
    rules: Dict[int, Set[int]], updates: List[List[int]]
) -> List[int]:
    middle_pages: List[int] = []
    for update in updates:
        if is_correctly_ordered_update(rules, update):
            continue
        pages_and_num_rules = [
            (page, len(rules.get(page, set()).intersection(update)))
            for page in update
        ]
        fixed_update = [page for page, _ in sorted(pages_and_num_rules, key=itemgetter(1), reverse=True)]
        middle_pages.append(fixed_update[len(fixed_update) // 2])
    return middle_pages


def is_correctly_ordered_update(rules: Dict[int, Set[int]], update: List[int]) -> bool:
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] not in rules.get(update[i], set()):
                return False
    return True


def main():
    rules, updates = parse_input()
    print("Sum of middle pages from correctly-ordered updates = {}".format(
        sum(get_middle_pages_from_correctly_ordered_updates(rules, updates)))
    )
    print("Sum of middle pages from incorrectly-ordered updates = {}".format(
        sum(get_middle_pages_from_incorrectly_ordered_updates(rules, updates)))
    )


if __name__ == "__main__":
    main()
