from jinja2 import Environment, PackageLoader, select_autoescape


def create_environment():
    return Environment(
        loader=PackageLoader("baphy", "templates"),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )
