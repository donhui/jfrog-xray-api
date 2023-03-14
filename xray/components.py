from xray.utils.http import RestApiAccessor


class XrayComponents(RestApiAccessor):
    """
    Xray REST API: COMPONENTS
    See: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API#XrayRESTAPI-COMPONENTS
    """

    def find_component_by_name(self, name: str):
        """
        Search for a component by name - applicable only for components synced from the JFrog Global database to Xray
        :param name:
        :return:
        """
        assert len(str(name)) > 0
        url = self.base_url + "/api/v1/component/" + name
        response = self.rest_get(
            url
        )
        return response

    def find_components_by_cves(self, cve_list: list):
        """
        Search for components by the CVEs it contains directly
        :param cve_list:
        :return:
        """
        assert len(cve_list) > 0
        url = self.base_url + "/api/v1/component/searchByCves"
        json_data = {
            "cves": cve_list
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def find_cves_by_components(self, components_id_list: list):
        """
        Search for CVEs by the infected components
        :param components_id_list:
        :return:
        """
        assert len(components_id_list) > 0
        url = self.base_url + "/api/v1/component/searchCvesByComponents"
        json_data = {
            "components_id": components_id_list
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def get_component_list_per_watch(self):
        """
        Gets a list of components associated with a specific watch
        :return:
        """

    def get_artifact_dependency_graph(self, artifact_path: str):
        """
        Get the complete dependency graph for an artifact
        :param artifact_path:
        :return:
        """
        url = self.base_url + "/api/v1/dependencyGraph/artifact"
        json_data = {
            "path": artifact_path
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def compare_artifacts(self, source_artifact_path: str, target_artifact_path: str):
        """
        Compares two artifacts and produces the difference between them
        :param source_artifact_path:
        :param target_artifact_path:
        :return:
        """
        url = self.base_url + "/api/v1/dependencyGraph/artifactDelta"
        json_data = {
            "source_artifact_path": source_artifact_path,
            "target_artifact_path": target_artifact_path
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def get_build_dependency_graph(self, artifactory_id: str, build_name: str, build_number: str):
        """
        Get the complete dependency graph for a build
        :param artifactory_id:
        :param build_name:
        :param build_number:
        :return:
        """
        url = self.base_url + "/api/v1/dependencyGraph/build"
        json_data = {
            "artifactory_id": artifactory_id,
            "build_name": build_name,
            "build_number": build_number
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def compare_builds(self,
                       source_artifactory_id: str,
                       source_build_name: str,
                       source_build_number: str,
                       target_artifactory_id: str,
                       target_build_name: str,
                       target_build_number: str
                       ):
        """
        Compares two builds and produces the difference between them
        :param source_artifactory_id:
        :param source_build_name:
        :param source_build_number:
        :param target_artifactory_id:
        :param target_build_name:
        :param target_build_number:
        :return:
        """
        url = self.base_url + "/api/v1/dependencyGraph/buildDelta"
        json_data = {
            "source_artifactory_id": source_artifactory_id,
            "source_build_name": source_build_name,
            "source_build_number": source_build_number,
            "target_artifactory_id": target_artifactory_id,
            "target_build_name": target_build_name,
            "target_build_number": target_build_number
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def export_component_details(self):
        """
        Export component details
        TODO
        :return:
        """
