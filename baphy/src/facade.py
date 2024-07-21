# FIXME: I am probably against disabling linters but I am too lazy for now
# pylint: disable=relative-beyond-top-level


import typer
from typing_extensions import Annotated

from .queries.project_name import query_project_info

# from .template_engine import create_environment
from .welcome import welcome


def main(
    target: Annotated[
        str,
        typer.Argument(help="Name of directory/project to create", show_default=False),
    ]
):
    # env = create_environment()

    # p = pathlib.Path("smth/")
    # p.mkdir(parents=True, exist_ok=True)

    template_variables = {}

    welcome()

    query_project_info(target, template_variables)

    print(template_variables)

    # template = env.get_template("CMakeLists.jinja")
    # print(template.render({"project_name": "smth"}))
