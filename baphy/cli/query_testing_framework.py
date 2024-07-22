import questionary

from baphy.choices import Choices, TestingFrameworkChoice


def query_testing_framework(user_choices: Choices):
    result_value = questionary.select(
        "Select desired testing framework:",
        choices=[x.value for x in TestingFrameworkChoice],
    ).ask()

    # Set the selected project type in user_choices
    user_choices.testing_framework = TestingFrameworkChoice(result_value)
