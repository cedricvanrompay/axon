""" Axon is a Synapse (Matrix homeserver) admin tool
"""

import os
import requests


class BaseClient():
    """ HTTP client for the synapse admin API
    """

    def __init__(self, config=None):
        if config is not None:
            self.config = config
        else:
            self.config = dict(
                url=os.environ["AXON_HOMESERVER"],
                token=os.environ["AXON_TOKEN"]
            )

    def query(self, method, url, qs=None, body=None):
        """ Run a query to the given admin API url
        """
        headers = {
            "Authorization": "Bearer " + self.config["token"]
        }
        return getattr(requests, method)(
            self.config["url"] + url,
            headers=headers,
            params=qs,
            json=body
        ).json()
