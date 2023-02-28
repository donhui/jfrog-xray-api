from xray.utils.http import RestApiAccessor


class XrayScanning(RestApiAccessor):
    """
    Xray REST API: SCANNING
    See: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API#XrayRESTAPI-SCANNING
    """
    def scan_artifact(self, component_id):
        """
        Invokes scanning of an artifact
        :param component_id: sample: docker://image_name:image_tag
        :return:
        """
        url = self.base_url + "/api/v1/scanArtifact"
        json_data = {
            "componentID": component_id
        }

        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def scan_build(self, build_name, build_number, api_version='v1'):
        """
        Invokes scanning of a build that was uploaded to Artifactory as requested by a CI server
        :param build_name:
        :param build_number:
        :param api_version: api/v2 starting from Xray version 3.42.3
        :return:
        """
        assert api_version in ['v1', 'v2']
        url = ''
        json_data = {}
        if api_version == 'v1':
            url = self.base_url + "/api/v1/scanBuild"
            json_data = {
                "buildName": build_name,
                "buildNumber": build_number,
                "rescan": True,
                "filters": {
                    "includeLicenses": True
                }
            }
        elif api_version == 'v2':
            url = self.base_url + "/api/v2/ci/build"
            json_data = {
                "buildName": build_name,
                "buildNumber": build_number
            }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response
