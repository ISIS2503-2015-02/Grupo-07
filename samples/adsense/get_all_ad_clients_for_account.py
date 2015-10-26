#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets all ad clients for an account.

Tags: accounts.adclients.list
"""

__author__ = 'jalc@google.com (Jose Alcerreca)'

import argparse
import sys

from apiclient import sample_tools
from oauth2client import client

MAX_PAGE_SIZE = 50

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('account_id',
                     help='The ID of the account for which to get ad clients')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'adsense', 'v1.3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/adsense.readonly')

  account_id = flags.account_id

  try:
    # Retrieve ad client list in pages and display data as we receive it.
    request = service.accounts().adclients().list(accountId=account_id,
                                                  maxResults=MAX_PAGE_SIZE)

    while request is not None:
      result = request.execute()
      ad_clients = result['items']
      for ad_client in ad_clients:
        print ('Ad client for product "%s" with ID "%s" was found. '
               % (ad_client['productCode'], ad_client['id']))

        print ('\tSupports reporting: %s' %
               (ad_client['supportsReporting'] and 'Yes' or 'No'))

      request = service.adclients().list_next(request, result)

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
