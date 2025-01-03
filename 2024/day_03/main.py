from typing import List, Optional, Tuple


def get_sum_of_mul(mul_args: List[Tuple[int, int]]) -> int:
    return sum([x*y for x, y in mul_args])


class MulParser:
    DO_CALL = "do()"
    DONT_CALL = "don't()"
    MUL = "mul"
    MUL_ARG_MAX_DIGITS = 3

    _curr_idx = 0
    _process_mul_call = True
    _process_do_or_dont_call = True

    def __init__(self, process_do_or_dont_call: bool):
        self._process_do_or_dont_call = process_do_or_dont_call


    def parse_mul_instruction(self, line: str) -> List[Tuple[int, int]]:
        mul_args: List[Tuple[int, int]] = []
        while self._curr_idx < len(line):
            if self._process_do_or_dont_call and line[self._curr_idx: self._curr_idx + len(MulParser.DO_CALL)] == MulParser.DO_CALL:
                self._process_mul_call = True
                self._curr_idx += len(MulParser.DO_CALL)
                continue

            if self._process_do_or_dont_call and line[self._curr_idx: self._curr_idx + len(MulParser.DONT_CALL)] == MulParser.DONT_CALL:
                self._process_mul_call = False
                self._curr_idx += len(MulParser.DONT_CALL)
                continue

            if not self._process_mul_call:
                self._curr_idx += 1
                continue

            if line[self._curr_idx: self._curr_idx + len(MulParser.MUL)] != MulParser.MUL:
                self._curr_idx += 1
                continue

            self._curr_idx += len(MulParser.MUL)
            if line[self._curr_idx] != "(":
                continue

            self._curr_idx += 1
            first_arg = self._get_mul_arg(line)
            if first_arg is None:
                continue

            if line[self._curr_idx] != ",":
                continue

            self._curr_idx += 1
            second_arg = self._get_mul_arg(line)
            if second_arg is None:
                continue

            if line[self._curr_idx] != ")":
                continue

            self._curr_idx += 1
            mul_args.append((first_arg, second_arg))
        return mul_args


    def _get_mul_arg(self, line: str) -> Optional[int]:
        mul_arg = ""
        for i in range(MulParser.MUL_ARG_MAX_DIGITS):
            if not line[self._curr_idx].isdigit():
                return None if len(mul_arg) == 0 else int(mul_arg)
            mul_arg += line[self._curr_idx]
            self._curr_idx += 1
        return int(mul_arg)


if __name__ == "__main__":
    instructions = open("input.txt", "r").read()
    sum_of_mul_without_do_or_dont = get_sum_of_mul(MulParser(False).parse_mul_instruction(instructions))
    print("Sum of multiplications = {}".format(sum_of_mul_without_do_or_dont))
    sum_of_mul_with_do_or_dont = get_sum_of_mul(MulParser(True).parse_mul_instruction(instructions))
    print("Sum of multiplications = {}".format(sum_of_mul_with_do_or_dont))
