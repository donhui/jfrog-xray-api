import requests
from requests.auth import HTTPBasicAuth

from xray.system import XraySystem
from xray.components import XrayComponents


class XrayRestClient(object):
    def __init__(self, *, base_url, username, password):
        self.base_url = base_url
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(username, password)

    @property
    def system(self):
        return XraySystem(base_url=self.base_url, session=self._session)

    @property
    def components(self):
        return XrayComponents(base_url=self.base_url, session=self._session)
