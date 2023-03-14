from xray.exceptions import ArgsException
from xray.utils.http import RestApiAccessor


class XraySummary(RestApiAccessor):
    """
    Xray REST API: SUMMARY
    See: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API#XrayRESTAPI-SUMMARY
    """
    def get_artifact_summary(self, **kwargs):
        """
        Provides details about any artifact specified by path identifiers or checksum.
        :param kwargs:
        :return:
        """
        url = self.base_url + "/api/v1/summary/artifact"
        json_data = {}
        if "checksums" in kwargs:
            json_data['checksums'] = kwargs['checksums']
        elif "paths" in kwargs:
            json_data['paths'] = kwargs['paths']

        if "checksums" not in kwargs and "paths" not in kwargs:
            raise ArgsException("checksums or paths cannot be null.")

        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def get_build_summary(self, build_name: str, build_number: str):
        """
        Provides details about any build specified by build identifier (name + number)
        :param build_name:
        :param build_number:
        :return:
        """
        url = self.base_url + f'/api/v1/summary/build?build_name={build_name}&build_number={build_number}'
        response = self.rest_get(
            url
        )
        return response
