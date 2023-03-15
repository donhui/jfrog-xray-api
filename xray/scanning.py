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

    def get_scan_status_for_artifact(self, repository_pkg_type, path, sha256):
        """
        Get scan status for artifact
        :param repository_pkg_type:
        :param path:
        :param sha256:
        :return:
        """
        url = self.base_url + "/api/v1/scan/status/artifact"
        json_data = {
            "repository_pkg_type": repository_pkg_type,
            "path": path,
            "sha256": sha256,
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def get_scan_status_for_build(self, name, version, project=None):
        """
        Get scan status for build
        :param name:
        :param version:
        :param project:
        :return:
        """
        url = self.base_url + "/api/v1/scan/status/build"
        json_data = {
            "name": name,
            "version": version,
        }
        if project is not None:
            json_data['project'] = project
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def scan_now(self, path):
        """
        Enables you to index resources on-demand, even those that were not marked for indexing
        :param path:
        :return:
        """
        url = self.base_url + "/api/v2/index"
        json_data = {
            "repo_path": path
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response
