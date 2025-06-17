from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Result for running file main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for running file tests.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for running file ../main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running file nonexistent.py:")
    print(result)
    print("")

if __name__ == "__main__":
    test()
