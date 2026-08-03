"""
A small sanity-check test. This doesn't call the AI (that would cost money
and need internet every time you run tests), it just checks that the
functions exist and are callable. Real testing of the AI output happens
by using the app itself.
"""

from assistant import generate_code, explain_code, find_bugs


def test_functions_exist():
    assert callable(generate_code)
    assert callable(explain_code)
    assert callable(find_bugs)
