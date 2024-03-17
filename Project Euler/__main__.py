import time

from src.problems.pb001_multiples_of_3_or_5 import multiples_of_3_or_5
from src.problems.pb002_even_fibonacci_numbers import even_fibonacci_numbers
from src.problems.pb003_largest_prime_factor import largest_prime_factor
from src.problems.pb004_largest_palindrome_product import largest_palindrome_product
from src.problems.pb005_smallest_multiple import smallest_multiple
from src.problems.pb006_sum_square_difference import sum_square_difference
from src.problems.pb007_10001st_prime import ten_thousand_first_prime
from src.problems.pb008_largest_product_in_a_serie import largest_product_in_a_series
from src.problems.pb009_special_pythagorean_triplet import special_pythagorean_triplet
from src.problems.pb010_summation_of_primes import summation_of_primes
from src.problems.pb011_largest_product_grid import largest_product_in_a_grid
from src.problems.pb012_highly_divisible_triangle_number import (
    highly_divisible_triangle_number,
)
from src.problems.pb013_large_sum import large_sum
from src.problems.pb038_pandigital_multiples import pandigital_multiples


def main():
    problems = {
        # 1: multiples_of_3_or_5,
        # 2: even_fibonacci_numbers,
        # 3: largest_prime_factor,
        # 4: largest_palindrome_product,
        # 5: smallest_multiple,
        # 6: sum_square_difference,
        # 7: ten_thousand_first_prime,
        # 8: largest_product_in_a_series,
        # 9: special_pythagorean_triplet,
        # 10: summation_of_primes,
        # 11: largest_product_in_a_grid,
        # 12: highly_divisible_triangle_number,
        13: large_sum,
        # 38: pandigital_multiples,
    }

    for problem_number, problem_function in problems.items():
        t1 = time.time()
        result = problem_function()
        t2 = time.time()
        print(
            format_problem_results(
                problem_number=problem_number,
                problem_function=problem_function,
                result=result,
                time_to_completion=t2 - t1,
            )
        )


def format_problem_results(
    problem_number: int,
    problem_function: callable,
    result: dict,
    time_to_completion: float,
) -> str:
    success = "✔" if result["result"] == result["expected"] else "❌"
    return f"{problem_number}. {problem_function.__name__} : {result['result']:,} [{success}] ({round(time_to_completion, 4)}s)"


if __name__ == "__main__":
    main()
