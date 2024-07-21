"""
Module tests_project_info.test_project_name contains tests for the
baphy.src.queries.project_name.NameValidator class.
"""

from dataclasses import dataclass

import pytest

import baphy.src.queries.project_name as source

validator = source.NameValidator()


@dataclass
class MockDocument:
    """
    Mock class for testing purposes. Represents a document with a text field.
    """

    text: str


@pytest.mark.parametrize(
    "valid_name",
    [
        # Valid names
        "flatcase",
        "UPPERCASE",
        "camelCase",
        "PascalCase",
        "snake_case",
        "ALL_CAPS",
        "camel_Snake_Case",
        "Pascal_Snake_Case",
        "kebab-case",
        "COBOL-CASE",
        "HTTP-Header-Case",
        "_startwithunderscore",
        "endwithunderscore_",
        "containing111numbers222",
        # Empty string is also valid
        "",
    ],
)
def test_valid_names(valid_name):
    """
    Test that all valid names are validated without any errors.
    """
    try:
        # Validate the name
        validator.validate(MockDocument(valid_name))
    except source.ValidationError:
        pytest.fail(f"Expected name {valid_name} to be valid, but validation failed")


@pytest.mark.parametrize(
    "name",
    ["-startwithslash", "1startwithnumber"],
)
def test_invalid_names(name):
    """
    Test that names starting with non-letter or underscore raise WrongStartError.
    """
    with pytest.raises(source.WrongStartError):
        validator.validate(MockDocument(name))


@pytest.mark.parametrize(
    "special_char",
    list("!@#$%^&*()+?=,<>/\"'"),
)
def test_expect_fail_with_special_chars(special_char):
    """
    Test that any text with special characters is failing validation.
    """
    # Create a text with the special character
    text_with_special_char = f"test_{special_char}_test"

    # Validate the text with the special character
    with pytest.raises(source.ForbiddenCharsError):
        validator.validate(MockDocument(text_with_special_char))
