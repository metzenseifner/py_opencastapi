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
import requests

class AbstractHttpClient():
    """
        IETF Hypertext Transfer Protocol HTTP/1.1
        https://datatracker.ietf.org/doc/html/rfc2616#section-5.1
    """
    def call(self, OpencastApiCall) -> OpencastResponse:
        raise NotImplementedError

class RequestsHttpClient(AbstractHttpClient):
   verbsToFunctions = {  'GET': requests.get,␠
                         'POST': requests.post,␠
                         'PUT': requests.put,␠
                         'DELETE': requests.delete,␠
                         'PATCH': requests.patch,
                         'HEAD': requests.head
                     }
   authStrategiesToFunctions = { 'digest': requests.auth.HTTPDigestAuth,
                                 'basic': requests.auth.HTTPBasicAuth
                               }

    def call(self, opencast_api_call: OpencastApiCall):
        http_request_func = MapUtilities.getMapValue(
            opencast_api_call.http_verb.upper(),
            verbsToFunctions).forEachOrFail(lambda e: None).forEach(lambda s: logger.error(s))
        auth_strategy_func = MapUtilities.getMapValue(
            auth_strategy,
            authStrategiesToFunctions).getOrElse(requests.auth.HTTPBasicAuth)
        http_request_func(
            opencast_api_call.url,
            auth=self.auth_strategy_func(
                opencast_api_call.username, opencast_api_call.password
            ),
            headers=opencast_api_call.headers, # every req supports this
            verify=True,
            **dict((x,y) for x,y in self._bind_request_arguments_to_members())
            )

    def _bind_request_arguments_to_members(self) -> List[Tuple]:⏎
      result = []⏎
      for p in inspect.signature(self.http_request_func).parameters:⏎
        r = getattr(self, p, None)⏎
        if r is not None:⏎
          logger.debug(f"Binding {self}.{r} to {p}")⏎
          result.append((p, r))⏎
      return result⏎
