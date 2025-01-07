from enum import Enum
from typing import List, Set, Tuple


class Direction(Enum):
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, map_symbol: str, dx: int, dy: int):
        self.map_symbol = map_symbol
        self.dx = dx
        self.dy = dy

    UP = "^", 0, -1
    DOWN = "V", 0, 1
    LEFT = "<", -1, 0
    RIGHT = ">", 1, 0

    def turn_right(self) -> "Direction":
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
            case Direction.RIGHT:
                return Direction.DOWN

    @staticmethod
    def get_direction_from_starting_pos(area: List[str], cur_x: int, cur_y: int) -> "Direction":
        for direction in Direction:
            if area[cur_y][cur_x] == direction.map_symbol:
                return direction

    @staticmethod
    def get_direction_from_cur_and_next_pos(cur_pos: Tuple[int, int], next_pos: Tuple[int, int]) -> "Direction":
        dx = next_pos[0] - cur_pos[0]
        dy = next_pos[1] - cur_pos[1]
        for direction in Direction:
            if dx == direction.dx and dy == direction.dy:
                return direction


def get_starting_pos(area: List[str]) -> Tuple[int, int]:
    for x in range(len(area[0])):
        for y in range(len(area)):
            if area[y][x] in {direction.map_symbol for direction in Direction}:
                return x, y


def get_guard_path(area: List[str]) -> Set[Tuple[int, int]]:
    visited: Set[Tuple[int, int]] = set()
    cur_x, cur_y = get_starting_pos(area)
    cur_direction = Direction.get_direction_from_starting_pos(area, cur_x, cur_y)

    while 0 <= cur_x < len(area[0]) and 0 <= cur_y < len(area):
        visited.add((cur_x, cur_y))
        next_x, next_y = cur_x + cur_direction.dx, cur_y + cur_direction.dy
        while 0 <= next_x < len(area[0]) and 0 <= next_y < len(area) and area[next_y][next_x] == "#":
            cur_direction = cur_direction.turn_right()
            next_x, next_y = cur_x + cur_direction.dx, cur_y + cur_direction.dy
        cur_x, cur_y = next_x, next_y
    return visited


def get_obstacle_positions(area: List[str]) -> Set[Tuple[int, int]]:
    obstacle_positions: Set[Tuple[int, int]] = set()
    start_x, start_y = get_starting_pos(area)

    for obstacle_pos_x in range(len(area[0])):
        for obstacle_pos_y in range(len(area)):
            if obstacle_pos_x == start_x and obstacle_pos_y == start_y:
                continue

            original_row = area[obstacle_pos_y]
            area[obstacle_pos_y] = original_row[:obstacle_pos_x] + "#" + original_row[obstacle_pos_x+1:]
            if is_guard_stuck_in_loop(area):
                obstacle_positions.add((obstacle_pos_x, obstacle_pos_y))
            area[obstacle_pos_y] = original_row
    return obstacle_positions


def is_guard_stuck_in_loop(area: List[str]) -> bool:
    visited: Set[Tuple[int, int, Direction]] = set()
    cur_x, cur_y = get_starting_pos(area)
    cur_direction = Direction.get_direction_from_starting_pos(area, cur_x, cur_y)
    while 0 <= cur_x < len(area[0]) and 0 <= cur_y < len(area):
        if (cur_x, cur_y, cur_direction) in visited:
            return True

        visited.add((cur_x, cur_y, cur_direction))
        next_x, next_y = cur_x + cur_direction.dx, cur_y + cur_direction.dy
        while 0 <= next_x < len(area[0]) and 0 <= next_y < len(area) and area[next_y][next_x] == "#":
            cur_direction = cur_direction.turn_right()
            next_x, next_y = cur_x + cur_direction.dx, cur_y + cur_direction.dy
        cur_x, cur_y = next_x, next_y
    return False


def main():
    area = open("input.txt", "r").read().split("\n")
    print("Number of guard positions = {}".format(len(get_guard_path(area))))
    print("Number of obstacle positions = {}".format(len(get_obstacle_positions(area))))


if __name__ == "__main__":
    main()
