"""
Module contains a function to query the user for the project name.

Also it contains a class to validate the project name.
The class has a single method "validate" which is used
to validate the project name based on the rules:
  - The name must begin with a letter or an underscore (_)
  - The name can't contain whitespace or special characters like !, #, %, etc.

The class raises a ValidationError if the name is invalid.
"""

import questionary
from prompt_toolkit.validation import ValidationError, Validator


class WrongStartError(ValidationError):
    """
    A ValidationError subclass for when the project name starts with a wrong character.
    """

    def __init__(self):
        super().__init__(
            message="Project name must begin with a letter or an underscore (_)"
        )


class ForbiddenCharsError(ValidationError):
    """
    A ValidationError subclass for when the project name contains forbidden characters
    (whitespace or special characters like !, #, %, etc.)
    """

    def __init__(self):
        super().__init__(
            message="Project name can't contain whitespace or special characters like !, #, %, etc."
        )


class NameValidator(Validator):
    """
    The class has a single method "validate" which is used
    to validate the project name based on the rules:
    - The name must begin with a letter or an underscore (_)
    - The name can't contain whitespace or special characters like !, #, %, etc.
    """

    def validate(self, document):
        """
        A function to validate the input text based on specific rules.
        It checks if the text starts with a letter or an underscore,
        and does not contain forbidden characters.
        """
        text = document.text

        # Empty string means default value
        if len(text) == 0:
            return

        # Names must begin with a letter or an underscore (_)
        if not text[0].isalpha() and not text[0] == "_":
            raise WrongStartError()

        # Names can't contain whitespaces or special characters like !, #, %, etc.
        forbidden_characters = "!@#$%^&*()+?=,<>/\"'"
        if any(c in forbidden_characters for c in text):
            raise ForbiddenCharsError()


def query_project_info(target, template_variables):
    """
    Query the user for the project name and store it in the template variables.

    Args:
        target (str): The target project directory.
        template_variables (dict): A dictionary to store template variables.

    Returns:
        None
    """

    # TODO: Let user call tool without specifying project name

    # Ask the user to enter the project name
    template_variables["project_name"] = questionary.text(
        f"Enter the project name ({target}):", validate=NameValidator()
    ).ask()
