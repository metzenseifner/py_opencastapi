#!/usr/bin/env python3
#
# Copyright 2021 Jonathan Lee Komar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

import pytest
from hamcrest import *
from opencastapi.adapters import config

class FakeConfiguration(config.Configuration):

    DUMMY_TARGET = "dummy"

    """The test configuration implementation.
    """
    def __init__(self, target="http://localhost:55000", username="testuser", password="testpassword"):
        self._target = target
        self._username = username
        self._password = password

    def target(self, target_id: str):
        return self._target 
    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password

@pytest.fixture
def test_config() -> config.Configuration:
	yield FakeConfiguration()

def test_can_read_username(test_config):
	assert_that(test_config.username, equal_to("testuser"))

def test_can_read_password(test_config):
	assert_that(test_config.password, equal_to("testpassword"))

def test_can_read_target(test_config):
	assert_that(test_config.target(FakeConfiguration.DUMMY_TARGET), equal_to("http://localhost:55000"))
