import json
import itertools
from sympy import lcm, symbols
from sympy.polys.polyfuncs import interpolate

def evaluate_expression(expr):
    if expr.startswith("sum("):
        a, b = map(int, expr[4:-1].split(","))
        return a + b
    elif expr.startswith("multiply("):
        a, b = map(int, expr[9:-1].split(","))
        return a * b
    elif expr.startswith("lcm("):
        a, b = map(int, expr[4:-1].split(","))
        return lcm(a, b)
    else:
        return int(expr)

def load_shares(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    points = [(entry["id"], evaluate_expression(entry["value"])) for entry in data]
    return points

def find_secret(points, k):
    x = symbols('x')
    constant_counter = {}
    for combo in itertools.combinations(points, k):
        xi, yi = zip(*combo)
        poly = interpolate(list(zip(xi, yi)), x)
        constant = poly.as_expr().subs(x, 0)
        constant_counter[constant] = constant_counter.get(constant, 0) + 1

    secret = max(constant_counter, key=constant_counter.get)
    return int(secret), len(constant_counter), constant_counter[secret]

def main():
    input_path = "shamir_input.json"
    output_path = "shamir_secret_output.json"
    k = 3

    points = load_shares(input_path)
    secret, com
