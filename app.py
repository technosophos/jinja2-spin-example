from spin_http import Response

# The basics we need from Jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape


def handle_request(request):
    # Declare a few Jinja variables
    title = "Hello Jinja"
    features = ["fast to run", "fun to write", "friendly for Python"]

    # The environment is the main encapsulation for jinja templates
    # We use the FileSystemLoader because Spin will package up only
    # the files we tell it to package. And that does not include the source
    # Python project (which is preloaded).
    #
    # IMPORTANT: You need to specify in `spin.toml` that the `templates/`
    # directory should be loaded.
    env = Environment(
        loader=FileSystemLoader("/templates"), autoescape=select_autoescape()
    )

    # Do the template loading. this will look in /templates for index.html
    template = env.get_template("index.html")
    out = template.render(title=title, features=features)

    # Send back the output as a response
    return Response(
        200,
        {"content-type": "text/html"},
        bytes(out, "utf-8"),
    )
