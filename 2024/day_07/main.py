import itertools
import operator
from typing import Callable, List, Tuple


def read_input() -> List[Tuple[int, List[int]]]:
    output: List[Tuple[int, List[int]]] = []
    with open("input.txt", "r") as f:
        for line in f:
            target, rest = line.split(":")
            numbers = [int(number) for number in rest.strip().split(" ")]
            output.append((int(target), numbers))
    return output


def concat_operator(x: int, y: int) -> int:
    return int(str(x) + str(y))


def get_valid_total_calibrations(
    equations: List[Tuple[int, List[int]]], operators: List[Callable[[int, int], int]]
) -> int:
    output = 0
    for equation in equations:
        target, numbers = equation

        operator_combinations = itertools.product(operators, repeat=len(numbers) - 1)
        for operator_combination in operator_combinations:
            current_total = numbers[0]
            for number, op in zip(numbers[1:], operator_combination):
                current_total = op(current_total, number)

            if current_total == target:
                output += target
                break
    return output


def main():
    calibration_equations = read_input()
    print("Total of calibrations = {}".format(
        get_valid_total_calibrations(calibration_equations, [operator.add, operator.mul]))
    )
    print("Total of calibrations with concat op = {}".format(get_valid_total_calibrations(
        calibration_equations, [operator.add, operator.mul, concat_operator]
    )))


if __name__ == "__main__":
    main()
