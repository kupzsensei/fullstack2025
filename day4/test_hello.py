from .samplelib import hello , multiply_by_two
# def main():
#     hello()


def test_hello():
    assert hello("milo") == "hello , milo"
    assert hello("greg") == "hello , greg"
    assert hello("jose") == "hello , jose"
    
def test_multiply_by_two():
    assert multiply_by_two(2) == 4
    assert multiply_by_two(1) == 2
    assert multiply_by_two(5) == 10

# linux
# python3 -m venv venv

# windows
# python -m venv venv


# activate virtual env.
# venv\Scripts\activate (windows)
# source venv/bin/activate (linux)

# pip install pytest

# runtest
# pytest ./day4/test_hello.py

# deactivate
# deactivate