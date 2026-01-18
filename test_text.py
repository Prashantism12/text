from test import clean_text

def test_case1():
    assert clean_text("madam") == "palindrome"

def test_case2():
    assert clean_text("hello") == "not palindrome"

def test_no_leave():
    assert clean_text("madam") == "palindrome"