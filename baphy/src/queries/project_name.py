import questionary
from prompt_toolkit.validation import ValidationError, Validator


class WrongStartError(ValidationError):
    def __init__(self):
        super().__init__(
            message="Project name must begin with a letter or an underscore (_)"
        )


class ForbiddenCharsError(ValidationError):
    def __init__(self):
        super().__init__(
            message="Project name can't contain whitespace or special characters like !, #, %, etc."
        )


class NameValidator(Validator):
    def validate(self, document):
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
    # TODO: Let user call tool without specifying project name

    template_variables["project_name"] = questionary.text(
        f"Enter the project name ({target}):", validate=NameValidator()
    ).ask()
