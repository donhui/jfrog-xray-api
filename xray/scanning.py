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


