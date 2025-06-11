import sys

from pkg.calculator import Calculator
from pkg.render import render

def main():
    calculator = Calculator()

    if len(sys.argv) <= 1:
        print("Calculator App")
        print("Usage: python main.py \"<expression>\"")
        print("Example: python main.py \"3 + 5\"")
        return

    expression = " ".join(sys.argv[1])

    try:
        result = calculator.evaluate(expression=expression)
        to_print = render(expression=expression, result=result)
        return to_print
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()