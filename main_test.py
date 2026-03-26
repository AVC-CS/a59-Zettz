import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # Input: 5 3 1 2 -> prints 5, 3, 1 (stops when 2 > 1)
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b5\b', r'\b3\b', r'\b1\b'], content)

@pytest.mark.T2
def test_main_2():
    # Input: 10 7 4 1 8 -> prints 10, 7, 4, 1 (stops when 8 > 1)
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b10\b', r'\b7\b', r'\b4\b', r'\b1\b'], content)

@pytest.mark.T3
def test_main_3():
    # Input: 20 15 10 5 25 -> prints 20, 15, 10, 5 (stops when 25 > 5)
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b20\b', r'\b15\b', r'\b10\b', r'\b5\b'], content)

@pytest.mark.T4
def test_main_4():
    # Input: 100 50 25 200 -> prints 100, 50, 25 (stops when 200 > 25)
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b100\b', r'\b50\b', r'\b25\b'], content)
