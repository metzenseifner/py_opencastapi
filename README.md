# OpencastAPI

The `opencastapi` package offers an object-oriented to the Opencast Project's API.

# Features

- Object-oriented interface.
- Multitarget/multinode support (currently limited to a common username and password across nodes per configuration).
- Abstracted, persisted, and reusable configuration.

# Installation

```
pip install opencastapi
```

# Configuration

The default configuration path is `/etc/opencastapi/opencastapi.conf`, but can be overridden by setting the environment variable `OPENCASTAPI_CONF_PATH`.

Example Configuration

```
[Security]
username=myapiusername
password=myapipassword

[Targets]
admin_prod=https://admin.opencast.org
player_prod=https://player.opencast.org

admin_dev=https://admin-dev.opencast.org
player_dev=https://player-dev.opencast.org
```

# Usage

Simple example:

```
import opencastapi

workflows_call = opencastapi.create_call(target='admin_dev', http_verb='get', path='/api/workflows')
response = workflows_call()

print(response.text)
```

Example with filter

```
import opencastapi

filter = {"filter":"start:2021-11-16T00:00:00+01:00/2021-11-16T23:59:59+01:00}
workflows_call = opencastapi.create_call(target='admin_dev', http_verb='get', path='/api/workflows', parameters=filter)
response = workflows_call()

print(response.text)
```

# License

It was developed indendent of the https://opencast.org/ project, and is also licensed differently.
