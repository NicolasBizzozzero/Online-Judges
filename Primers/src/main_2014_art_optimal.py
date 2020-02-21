import os
import collections

from core import Problem, Number, main


Input = collections.namedtuple("Input", ["largeur", "hauteur", "pixels"])
Solution = collections.namedtuple("Solution", ["operations"])

PATH_DIR_INPUTS = os.path.join("..", "inputs", "2014_art_optimal")
PATH_DIR_OUTPUTS = os.path.join("..", "outputs", "2014_art_optimal")


class ProblemArtOptimal(Problem):
    def parse_input(self, path_file_input: str) -> Input:
        with open(path_file_input, 'r') as fp:
            lines = fp.readlines()
        largeur, hauteur = list(map(int, lines[0].strip().split(',')))
        pixels = list(map(lambda l: l.strip(), lines[1:]))
        return Input(largeur=largeur, hauteur=hauteur, pixels=pixels)

    def score(self, inp: Input, solution: Solution) -> Number:
        return len(solution.operations)

    def solve(self, inp: Input) -> Solution:
        return self._solve_paint_one_by_one(inp)

    def write_output(self, solution: Solution, func_convert: callable, score: Number, id_problem: str,
                     path_dir_outputs: str = PATH_DIR_OUTPUTS):
        # Create outputs directory if it does not exists
        os.makedirs(path_dir_outputs, exist_ok=True)

        path_file_output = os.path.join(path_dir_outputs, id_problem + '_' + str(score)) + ".out"
        string = func_convert(solution)
        with open(path_file_output, 'w') as fp:
            fp.write(string)

    def _solve_paint_one_by_one(self, inp: Input) -> Solution:
        operations = []

        for y in range(inp.hauteur):
            for x in range(inp.largeur):
                if inp.pixels[y][x] == "#":
                    operations.append(op_fill(x=x, y=y, size=1))
        return Solution(operations=operations)


def op_fill(x, y, size):
    return ["FILL", x, y, size]


def op_erase(x, y):
    return ["ERASE", x, y]


def func_convert(solution: Solution) -> str:
    res = ''
    for operation in solution.operations:
        res += ",".join(map(str, operation)) + "\n"
    return res


if __name__ == "__main__":
    main(
        problem_class=ProblemArtOptimal,
        func_convert=func_convert,
        path_dir_inputs=PATH_DIR_INPUTS,
        path_dir_outputs=PATH_DIR_OUTPUTS,
    )
