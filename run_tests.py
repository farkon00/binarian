from asyncio import subprocess
from re import sub
import sys
from .binarian import main
from subprocess import run
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
def test_python(name, argv):
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

global is_exe_test
is_exe_test = False

# This test isnt running on pushes, because
# exe file isnt updated as often as python source code,
# so some features for tests may be not implomented
@pytest.mark.parametrize(["name", "argv"], tests)
def test_exe(name, argv):
    global is_exe_test
    is_exe_test = True

    sys.stdout = open(f"tests_results/exe_{name}.txt", "w")

    try:
        sys.stdin = open(f"tests/{name}_input.txt", "r")
    except FileNotFoundError:
        pass
    
    try:
        run(("binarian", f"tests/{name}.bino", *argv), shell=True)
    except SystemExit:
        pass

    sys.stdout.close()

    result = open(f"tests_results/{name}.txt", "r").read()
    expected = open(f"tests/expected_results/{name}.txt", "r").read()

    cut_index = result.rfind("Finished in")
    if cut_index != -1:
        result = result[:cut_index-2]

    assert result == expected

if is_exe_test:
    print("Exe file isnt updated as often as python source code, \nso some features for tests may be not implomented \n\n")