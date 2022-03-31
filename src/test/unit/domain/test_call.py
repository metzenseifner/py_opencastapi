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
from opencastapi.domain import opencast_api_call, events

# Unit tests the OpencastApiCall class.

def test_default_get_call_event():
    
    call_maker = opencast_api_call.OpencastApiCall(
        http_verb="GET",
        address="https://admin.opencast.org",
        path="/api/test",
        headers="",
        parameters={},
        auth_strategy="digest",
        data=b"",
        username="",
        password=""
        )

    call = call_maker()

    expected = events.HttpCallCreatedEvent(
        http_verb="", 
        url="", 
        parameters="", 
        headers="", 
        data="", 
        username="",
        password="")

    assert_that(call_maker.events[-1], equal_to(expected))

#def test_call_event_if_cannot_create():
#    pass
