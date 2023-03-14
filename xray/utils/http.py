class RestApiAccessor:
    """
    Implements operations with REST API
    """

    def __init__(self, base_url, session):
        self._session = session
        self.base_url = base_url

    def rest_get(self,
                 url,
                 params=None,
                 headers=None,
                 verify=True,
                 cert=None,
                 timeout=None,
                 ):
        """
        Perform a GET request to url
        :param url:
        :param params:
        :param headers:
        :param verify:
        :param cert:
        :param timeout:
        :return: response object
        """
        response = self._session.get(
            url,
            params=params,
            headers=headers,
            verify=verify,
            cert=cert,
            timeout=timeout,
        )
        return response

    def rest_post(self,
                  url,
                  params=None,
                  headers=None,
                  verify=True,
                  cert=None,
                  timeout=None,
                  json_data=None,
                  ):
        """
        Perform a POST request to url
        :param url:
        :param params:
        :param headers:
        :param verify:
        :param cert:
        :param timeout:
        :param json_data:
        :return: response object
        """
        response = self._session.post(
            url,
            json=json_data,
            params=params,
            headers=headers,
            verify=verify,
            cert=cert,
            timeout=timeout,
        )
        response.raise_for_status()
        return response

    def rest_put(self,
                 url,
                 params=None,
                 headers=None,
                 verify=True,
                 cert=None,
                 timeout=None,
                 json_data=None,
                 ):
        """
        Perform a PUT request to url
        :param url:
        :param params:
        :param headers:
        :param verify:
        :param cert:
        :param timeout:
        :param json_data:
        :return: response object
        """
        response = self._session.put(
            url,
            json=json_data,
            params=params,
            headers=headers,
            verify=verify,
            cert=cert,
            timeout=timeout,
        )
        return response
