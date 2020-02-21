import os
import collections
import random

import numpy as np

from core import Problem, Number, main


Input = collections.namedtuple("Input", ["nb_ampoules", "nb_interrupteurs", "ampoules"])
Solution = collections.namedtuple("Solution", ["interrupteurs"])

PATH_DIR_INPUTS = os.path.join("..", "inputs", "XXXX_illumination")
PATH_DIR_OUTPUTS = os.path.join("..", "outputs", "XXXX_illumination")


class ProblemIllumination(Problem):
    def parse_input(self, path_file_input: str) -> Input:
        with open(path_file_input, 'r') as fp:
            lines = fp.readlines()
        nb_ampoules, nb_interrupteurs = list(map(int, lines[0].strip().split(',')))
        ampoules = list(map(lambda l: list(map(int, l.strip().split(","))), lines[1:]))
        return Input(nb_ampoules=nb_ampoules, nb_interrupteurs=nb_interrupteurs, ampoules=ampoules)

    def score(self, inp: Input, solution: Solution) -> Number:
        ampoules_on = dict()
        for idx_interrupteur in solution.interrupteurs:
            for ampoule in inp.ampoules[idx_interrupteur]:
                try:
                    ampoules_on[ampoule] += 1
                except KeyError:
                    ampoules_on[ampoule] = 1
        return len(list(filter(lambda a: a % 2 == 1, ampoules_on.values())))

    def solve(self, inp: Input) -> Solution:
        return self._solve_bruteforce_random(inp, start=100_000, stop=150_000)

    def _solve_sort_then_greedy_bruteforce(self, inp: Input) -> Solution:
        """ Result: 569. """
        sorted_interrupteurs = sorted(enumerate(inp.ampoules), key=lambda e: len(e[1]), reverse=True)

        best_solution = Solution(interrupteurs=[sorted_interrupteurs[0][0]])
        best = self.score(inp, best_solution)

        for _ in range(len(sorted_interrupteurs) - 1):
            solution = Solution(interrupteurs=[sorted_interrupteurs[0][0]])
            score = self.score(inp, solution)
            if score > best:
                best = score
                best_solution = solution

            for interrupteur, ampoules in sorted_interrupteurs:
                solution = Solution(interrupteurs=solution.interrupteurs + [interrupteur])
                score = self.score(inp, solution)
                if score > best:
                    best = score
                    best_solution = solution
            sorted_interrupteurs = sorted_interrupteurs[1:]
        return best_solution

    def _solve_bruteforce_random_multithread(self, inp: Input) -> Solution:
        from multiprocessing import Pool 

        pool = Pool(processes=8)
        results = pool.map(self.score, lst)
        pool.close()
        pool.join()

        print(results)

    def _solve_bruteforce_random(self, inp: Input, start: int = 0, stop: int = 1000) -> Solution:
        """ Result: 573. """
        best = 0
        best_solution = None
        for seed in range(start, stop):
            np.random.seed(seed=seed)
            random.seed(a=seed)
            solution = self._solve_random(inp=inp)
            score = self.score(inp=inp, solution=solution)
            if score > best:
                best = score
                best_solution = solution
        return best_solution

    def _solve_random(self, inp: Input) -> Solution:
        interrupteurs = list(np.random.choice(a=list(range(inp.nb_interrupteurs)),
                                              size=random.randint(1, inp.nb_interrupteurs),
                                              replace=False))
        return Solution(interrupteurs=interrupteurs)


def func_convert(solution: Solution) -> str:
    return "\n".join(map(str, solution.interrupteurs))


if __name__ == "__main__":
    main(
        problem_class=ProblemIllumination,
        func_convert=func_convert,
        path_dir_inputs=PATH_DIR_INPUTS,
        path_dir_outputs=PATH_DIR_OUTPUTS,
        inputs_to_skip=["a"],
    )
