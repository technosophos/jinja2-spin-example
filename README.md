# Using Jinja2 within a Python Spin App

This is an example of using the [Jinja2 template engine](https://jinja.palletsprojects.com/en/3.1.x/) inside of a Fermyon Spin app.

This shows how to load templates off of the filesystem and then render them and serve them back to the client.

Jinja docs:
* Python docs: https://jinja.palletsprojects.com/en/3.1.x/
* Template docs: https://jinja.palletsprojects.com/en/3.1.x/templates/

## Prerequisites

* [Spin](https://developer.fermyon.com/spin)
* [pipenv](https://pipenv.pypa.io/en/latest/index.html)

## Installing

* Install the dependencies with `pipenv update`
* Build with `spin build`

```
$ pipenv update
$ spin build
```

## How This Works

This example uses Jinja2 templates, which are stored in `templates/`. The main `app.py` loads and renders templates.

There are three things to keep in mind about this demo:

* In order to make this work, we need to tell `spin.toml` to make `templates/` available to the app. See the `spin.toml` file. See the `files` directive in [the component table](https://developer.fermyon.com/spin/v2/manifest-reference#the-component-table)
* Templates are bundled into the application, not read dynamically off of disk. So you may want to use `spin watch` during development
* Because the Python environment is pre-initialized, you cannot dynamically load template functions in runtime.
