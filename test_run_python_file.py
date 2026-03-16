from functions.run_python_file import run_python_file

print(f'Results from running "calculator/main.py"')
print(run_python_file("calculator", "main.py"))

print(f'Results from running "calculator/main.py ["3 + 5"]')
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print(f'Results from running "calculator/tests.py"')
print(run_python_file("calculator", "tests.py"))

print(f'Results from running "calculator", "../main.py"')
print(run_python_file("calculator", "../main.py"))

print(f'Results from running "calculator", "nonexistent.py"')
print(run_python_file("calculator", "nonexistent.py"))

print(f'Results from running "calculator", "lorem.txt"')
print(run_python_file("calculator", "lorem.txt"))