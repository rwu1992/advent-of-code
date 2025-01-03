from typing import List


def read_input() -> List[List[int]]:
    reports = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            reports.append([int(level) for level in line.split(" ")])
    return reports


def get_number_safe_reports(reports: List[List[int]]) -> int:
    return sum([int(is_report_safe(report)) for report in reports])


def get_number_safe_reports_with_problem_dampener(reports: List[List[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
            continue
        for level_to_omit in range(len(report)):
            if is_report_safe(report[:level_to_omit] + report[level_to_omit+1:]):
                safe_reports += 1
                break
    return safe_reports


def is_report_safe(report: List[int]) -> bool:
    is_prev_increasing = None
    for curr_level, next_level in zip(report, report[1:]):
        if curr_level == next_level:
            return False
        elif is_prev_increasing is None:
            is_prev_increasing = curr_level < next_level

        if is_prev_increasing != (curr_level < next_level):
            return False
        if abs(curr_level - next_level) > 3:
            return False
    return True


if __name__ == '__main__':
    input_reports = read_input()
    print("Safe reports = {}".format(get_number_safe_reports(input_reports)))
    print("Safe reports with problem dampener = {}".format(
        get_number_safe_reports_with_problem_dampener(input_reports))
    )
