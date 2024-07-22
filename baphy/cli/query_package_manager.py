import questionary

from baphy.choices import Choices, PackageManagerChoice


def query_package_manager(user_choices: Choices):
    result_value = questionary.select(
        "Select desired package manager:",
        choices=[x.value for x in PackageManagerChoice],
    ).ask()

    # Set the selected project type in user_choices
    user_choices.package_manager = PackageManagerChoice(result_value)
