""" Day 1: Calorie Counting

Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""


import copy
import os

import numpy as np


PATH_DIR_INPUT = "res"
PATH_FILE_INPUT = os.path.join(
    PATH_DIR_INPUT, f"{__file__.split('/')[-1].split('_')[0]}_input.txt"
)


def main():
    problem = parse_input(path_file_input=PATH_FILE_INPUT)

    part1_max_elf(problem=copy.deepcopy(problem))
    part2_max_elves(problem=copy.deepcopy(problem))


def part1_max_elf(problem):
    # Flatten problem by summing each elf calories
    problem = np.array(list(map(lambda elf: sum(elf), problem)))

    max_calories, max_elf = topk_values(array=problem, k=1)
    print("Problem 1")
    print("  Max calories:", max_calories[0])
    print("  Max elf     :", max_elf[0] + 1)


def part2_max_elves(problem):
    # Flatten problem by summing each elf calories
    problem = np.array(list(map(lambda elf: sum(elf), problem)))

    max_calories, max_elves = topk_values(array=problem, k=3)
    print("Problem 2")
    print("  Max calories:", max_calories)
    print("  Sum calories:", sum(max_calories))
    print("  Max elves   :", max_elves + 1)


def parse_input(path_file_input: str):
    problem = []

    with open(path_file_input) as fp:
        elf = []
        for line in fp:
            line = line.strip()
            if len(line) == 0:
                problem.append(elf)
                elf = []
            else:
                elf.append(int(line))
        if len(elf) != 0:
            problem.append(elf)
    return problem


def topk_values(array: np.ndarray, k: int):
    top_idx = np.argpartition(array, -k)[-k:]
    top_idx = top_idx[np.argsort(array[top_idx])]
    top_values = array[top_idx]
    return top_values, top_idx


if __name__ == "__main__":
    main()
