def set_stdin_from_file(new_stdin: str, mode: str = "r") -> callable:
    """Temporary change stdin to the file value passed as argument."""

    def real_decorator(function: callable) -> callable:
        def wrapper(*args, **kwargs):
            import sys

            previous_stdin = sys.stdin
            sys.stdin = open(new_stdin, mode)
            result = function(*args, **kwargs)
            sys.stdin.close()
            sys.stdin = previous_stdin
            return result

        return wrapper

    return real_decorator


def set_stdin_from_str(new_stdin: str) -> callable:
    """Temporary change stdin to the string value passed as argument."""

    def real_decorator(function: callable) -> callable:
        def wrapper(*args, **kwargs):
            import sys
            from io import StringIO

            previous_stdin = sys.stdin
            sys.stdin = StringIO(new_stdin)
            result = function(*args, **kwargs)
            sys.stdin.close()
            sys.stdin = previous_stdin
            return result

        return wrapper

    return
