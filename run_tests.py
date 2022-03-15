import sys
from .binarian import main
import pytest

tests = [
    ["set_debug", ["-d"]],
    ["io"],
    ["log_oper"],
    ["expr"],
    ["drop", ["-d"]],
    ["if"],
    ["for"],
    ["while"],
    ["func"],
    ["exception"],
    ["call_stack"],
    ["std", "-d"],
    ["no-std", ["-no-std"]]
]

# Adds argv everywhere
for test in tests:
    if len(test) == 1:
        test.append([])

@pytest.mark.parametrize(["name", "argv"], tests)
def test_language(name, argv):
    sys.stdout = open(f"tests_results/{name}.txt", "w")

    try:
        sys.stdin = open(f"tests/{name}_input.txt", "r")
    except FileNotFoundError:
        pass
    
    try:
        main(test_argv=["binarian.py", f"tests/{name}.bino", *argv])
    except SystemExit:
        pass

    sys.stdout.close()

    result = open(f"tests_results/{name}.txt", "r").read()
    expected = open(f"tests/expected_results/{name}.txt", "r").read()

    cut_index = result.rfind("Finished in")
    if cut_index != -1:
        result = result[:cut_index-2]

    assert result == expected