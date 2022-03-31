import pytest
from hamcrest import *

from opencastapi import bootstrap
from opencastapi.adapters.config import AbstractConfiguration
from opencastapi.adapters.http_client import AbstractHttpClient
from opecnastapi.domain.opencast_api_call import OpencastApiCall

class FakeConfiguration(AbstractConfiguration):
    def __init__(self):
        pass
class FakeClient(AbstractHttpClient):
    """ Spy Object """
    calls = []
    def __init__(self, known_paths: Dict={}):
        self.known_paths = known_paths

    def call(self, opencast_api_call: OpencastApiCall):
        calls.append(opencast_call)

# Fixture
opencastapi = bootstrap.bootstrap(config=FakeConfiguration(), client=FakeClient())

class Test_Instantiation:
    def test_create_call(self):
        sut = opencastapi.create_call(target="admin", http_verb="get", path="/api/workflows", parameters={'pkey', 'pvalue'}, data={'dkey', 'dvalue'})
        assert_that(sut, instance_of(OpencastApi))

class Test_HTTP_GET:
    def test_get(self):
        call = opencastapi.create_call(target="admin", http_verb="get", path="/api/workflows", parameters={'pkey', 'pvalue'}, data={'dkey', 'dvalue'})
        sut = call()
        assert_that(sut, equal_to="")
