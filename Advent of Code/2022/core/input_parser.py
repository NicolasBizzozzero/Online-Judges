from core.map_funcs import identity

# TODO: Quelle interface ?
#  data = InputParser(from=..., ...)
#  from: sys.stdin, os.path.isfile(...), otherwise string
#  So automatic parsing or multiple calls to InputParser for files with multiple thing to parse.


class InputParser:
    def __init__(
        self,
        lines: int = 1,
        values_per_lines: int = 1,
        map_func: callable = identity,
        separator: str = " ",
    ):
        self.lines = lines
        self.values_per_lines = values_per_lines
        self.map_func = map_func
        self.separator = separator

    def parse(self, input_stream: str):
        if self.lines == 1:
            if self.values_per_lines == 1:
                return self.map_func(input())
            else:
                return list(map(self.map_func, input().split(self.separator)))
        else:
            if self.lines:
                return [self.map_func(input()) for _ in range(self.lines)]
            else:
                return [
                    list(map(self.map_func, input().split(self.separator)))
                    for _ in range(self.lines)
                ]
