from functions.run_python_file import run_python_file

print("Print the calculator's usage instructions:")
print(run_python_file("calculator", "main.py"))
print("\n")

print("should run the calculator:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("\n")

print("Should run the calculator's tests successfully:")
print(run_python_file("calculator", "tests.py"))
print("\n")

print("This should return an error:")
print(run_python_file("calculator", "../main.py"))
print("\n")

print("This should return an error:")
print(run_python_file("calculator", "nonexistent.py"))
print("\n")

print("This should return an error:")
print(run_python_file("calculator", "lorem.txt"))
print("\n")