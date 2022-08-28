# format_data.py

# Easier to Manage State and Dependencies
# pytest takes a different approach. It leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures. pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite. Any test that wants to use a fixture must explicitly use this fixture function as an argument to the test function, so dependencies are always stated up front:


# fixture_demo.py

import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1

# Fixtures: Managing State and Dependencies
# pytest fixtures are a way of providing data, test doubles, or state setup to your tests. Fixtures are functions that can return a wide range of values. Each test that depends on a fixture must explicitly accept that fixture as an argument.

# When to Create Fixtures
# In this section, you’ll simulate a typical test-driven development (TDD) workflow.

# Imagine you’re writing a function, format_data_for_display(), to process the data returned by an API endpoint. The data represents a list of people, each with a given name, family name, and job title. The function should output a list of strings that include each person’s full name (their given_name followed by their family_name), a colon, and their title:
# def test_format_data_for_display(people):
#     people = [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ]
#     assert test_format_data_for_display(people) == [
#         "Alfonsa Ruiz: Senior Software Engineer",
#         "Sayid Khan: Project Manager",
#     ]

# def test_format_data_for_excel():
#     people = [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ]

#     assert format_data_for_excel(people) == """given,family,title
# Alfonsa,Ruiz,Senior Software Engineer
# Sayid,Khan,Project Manager
# """

# Your to-do list grows! That’s good! One of the advantages of TDD is that it helps you plan out the work ahead. The test for the format_data_for_excel() function would look awfully similar to the format_data_for_display() function:

# Notably, both the tests have to repeat the definition of the people variable, which is quite a few lines of code.

# If you find yourself writing several tests that all make use of the same underlying test data, then a fixture may be in your future. You can pull the repeated data into a single function decorated with @pytest.fixture to indicate that the function is a pytest fixture:

# test_format_data.py

import pytest

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert test_format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
def test_format_data_for_excel(example_people_data):
    assert test_format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""

# Each test is now notably shorter but still has a clear path back to the data it depends on. Be sure to name your fixture something specific. That way, you can quickly determine if you want to use it when writing new tests in the future!

# When you first discover the power of fixtures, it can be tempting to use them all the time, but as with all things, there’s a balance to be maintained.

# When to Avoid Fixtures
# Fixtures are great for extracting data or objects that you use across multiple tests. However, they aren’t always as good for tests that require slight variations in the data. Littering your test suite with fixtures is no better than littering it with plain data or objects. It might even be worse because of the added layer of indirection.

# As with most abstractions, it takes some practice and thought to find the right level of fixture use.

# Nevertheless, fixtures will likely be an integral part of your test suite. As your project grows in scope, the challenge of scale starts to come into the picture. One of the challenges facing any kind of tool is how it handles being used at scale, and luckily, pytest has a bunch of useful features that can help you manage the complexity that comes with growth.
