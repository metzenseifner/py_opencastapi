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
from typing import Dict, Tuple, List, Callable
from opencastapi.domain import events
import requests
from fpinpy import MapUtilities, Result, IniConfigReader
import inspect
import logging
logger = logging.getLogger('OpencastApiCall')

class OpencastApiCall:
  """HTTP-Protocol Action to an Opencast node.

     This object represents a tuple of all data necessary to make
     a call. It must have no dependencies, and must not pass the
     service layer boundary to the user.

     TODO: support different authentication strategies

     Parameters:
     http_verb: the HTTP verb
     address: the address segment
     path: the URL path segment
     parameters: the URL parameters segment
     headers: the headers to be used in the HTTP header section
     username: the username
     password: the password
  """
  def __init__(self, 
                http_verb: str="", 
                address: str="",
                path: str="", 
                headers: str="", 
                parameters: Dict={}, 
                auth_strategy: str="digest",
                data=b"",
                username: str="", 
                password:str="",
                callback: Callable):
    self.http_verb = http_verb # used only to create event
    self.address = address
    self.path = path
    self.params = parameters
    self.headers = headers
    self.data = data
    self.auth_strategy = auth_strategy
    self.username = username
    self.password = password
    self.url = Result.of(self.address)\
        .map(lambda url: url.rstrip('/'))\
        .map(lambda url: url + self.path).getOrException()
    self.callback = callback

    self.events = [] # used for testing

  def __call__(self) -> Callable:
    self.events.append(HttpCallCreatedEvent(
        self.http_verb,
        self.url,
        self.parameters,
        self.headers,
        self.data,
        self.username,
        self.password)
    self.callback(self)
