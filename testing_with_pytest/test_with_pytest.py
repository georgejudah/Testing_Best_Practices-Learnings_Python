# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

# You usually want to put your tests into their own folder called tests at the root level of your project.

# Easy to Filter Tests
# As your test suite grows, you may find that you want to run just a few tests on a feature and save the full suite for later. pytest provides a few ways of doing this:

# Name-based filtering: You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
# Directory scoping: By default, pytest will run only those tests that are in or under the current directory.
# Test categorization: pytest can include or exclude tests from particular categories that you define. You can do this with the -m parameter.