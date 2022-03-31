#!/usr/bin/env python3

from .adapters import config
from .service_layer import services

"""
1. Declare default dependencies but allow overrides for testing
2. Do any initialization.
"""

def bootstrap(
    conf: config.Configuration = config.EnvironmentThenFileConfiguration(),
    client: AbstractHttpClient = OpencastHttpApiClient()
    ) -> services.OpencastApi:
    """Composition root to handle early initialization 

        returning a ready OpencastApi object.
        Dependency injection makes tests cleaner.
    """
    return services.OpencastApi(conf, client=client)
