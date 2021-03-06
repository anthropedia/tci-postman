# TCI Postman

Email sender for the TCI Flask projects.


## Installation

- `pip install -e https://github.com/anthropedia/tci-postman.git#egg=tci-postman`
from within your project's _virtual environment_.

Note that the project using TCI Postman should be installing
[the TCI Database private project](https://bitbucket.org/anthropedia/tci-database).

add this to your code:

```
import tcipostman
tcipostman.init_app(app)
```


## Required configuration

Default configuration is [available in Flask-Mail configuration documentation] ](https://pythonhosted.org/Flask-Mail/#configuring-flask-mail).

In addition to these config, `app.config` must contain the following keys:

- `TCI_TEST_URL`: the absolute URL for passing a test. the pattern `{token}`
will be replaced with the token key.
