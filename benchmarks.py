from timeit import timeit
from shutil import get_terminal_size
from pyjsx import *


ITERATIONS = 100_000
COLS, ROWS = get_terminal_size((80, 80))


def benchmark(stmt: str, name: str):
    print("=" * COLS)
    print(f"Benchmark: '{name}'")
    print("=" * COLS)
    time = timeit(stmt, number=ITERATIONS, globals=globals())
    print(f"{round(time * 1000, 4)} miliseconds for {ITERATIONS} renders of '{name}'")
    print(f"Avg {round((time / ITERATIONS) * 1000, 4)} miliseconds for one render.")
    # Add linebreaks between runs.
    print("")


benchmark("render(_.p('Hello world!'))", name="Hello world")


SIMPLE_DOC = """
render(
    _.html(
        _.head(
            _.link(rel="stylesheet", type="text/css", ref="/index.css"),
            _.title("JSX In Python... Kinda.")
        ),
        _.body(
            _.main(
                _.article(
                    _.header(
                        _.h1("Wow, it's like JSX in python!!"),
                        _.h3("That's really cool."),
                    ),
                    _.p(
                        "It's like a mini-React kinda. What's really cool is that it"
                        "allows the usual Python tricks for functions. You can"
                        "compose HTML fragments as functions. Really cool."
                    ),
                )
            )
        )
    )
)
"""

benchmark(SIMPLE_DOC, name="Simple HTML document.")
