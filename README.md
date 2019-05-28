

# OpenStax Faculty Verification

OpenStax Faculty Verification is a set of APIs to request faculty verification and query on user verification status. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* verify (verification APIs and workflow)
* saleforce (Salesforce connection and query code)
* accounts (authentication)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv verification`
    2. `$ . verification/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
