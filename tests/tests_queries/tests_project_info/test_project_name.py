from dataclasses import dataclass
import pytest

import baphy.src.queries.project_name as source

validator = source.NameValidator()


@dataclass
class MockDocument:
    text: str


### Test checks that all valid names are passing validator
@pytest.mark.parametrize(
    "test_text",
    [
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
        "",
    ],
)
def test_expect_valid_names(test_text):
    try:
        validator.validate(MockDocument(test_text))
    except source.WrongStartError:
        pytest.fail(
            f"Expected text {test_text} to be valid but it contains wrong start"
        )
    except source.ForbiddenCharsError:
        pytest.fail(
            f"Expected text {test_text} to be valid but it contains forbidden characters"
        )


### Test checks that any start except letter or underscore is failing validation
@pytest.mark.parametrize(
    "test_text",
    ["-startwithslash", "1startwithnumber"],
)
def test_expect_fail_with_wrong_start(test_text):
    with pytest.raises(source.WrongStartError):
        validator.validate(MockDocument(test_text))


### Test checks that all forbidden chars are failing validation
@pytest.mark.parametrize(
    "test_char",
    list("!@#$%^&*()+?=,<>/\"'"),
)
def test_expect_fail_with_wrong_start(test_char):
    text_with_special = f"test_{test_char}_test"
    with pytest.raises(source.ForbiddenCharsError):
        validator.validate(MockDocument(text_with_special))
