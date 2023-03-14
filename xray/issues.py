from enum import Enum
from xray.utils.http import RestApiAccessor


class XrayIssueType(Enum):
    SECURITY = 'Security'
    VERSIONS = 'Versions'
    PERFORMANCE = 'Performance'
    OTHER = 'Other'


class XrayIssueSeverity(Enum):
    INFORMATION = 'Information'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'


class XrayIssues(RestApiAccessor):
    """
    Xray REST API: ISSUES
    See: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API#XrayRESTAPI-ISSUES
    """

    def create_issue_event(self,
                           *,
                           issue_id,
                           package_type: str,
                           summary: str,
                           description: str,
                           component_id: str,
                           vulnerable_versions: list,
                           provider="Custom",
                           issue_type=XrayIssueType.SECURITY.value,
                           severity=XrayIssueSeverity.LOW.value,
                           cve_list=None
                           ):
        """
        Allows adding a custom issue
        :param issue_id:
        :param summary:
        :param description:
        :param package_type:
        :param component_id:
        :param vulnerable_versions:
        :param provider:
        :param issue_type:
        :param severity:
        :param cve_list:
        :return:
        """
        if cve_list is None:
            cve_list = []
        url = self.base_url + "/api/v1/events"
        json_data = {
            "id": issue_id,
            "type": issue_type,
            "provider": provider,
            "package_type": package_type,
            "severity": severity,
            "components": [
                {
                    "id": component_id,
                    "vulnerable_versions": vulnerable_versions
                }
            ],
            "cves": cve_list,
            "summary": summary,
            "description": description
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def update_issue_event(self,
                           *,
                           issue_id,
                           package_type: str,
                           summary: str,
                           description: str,
                           component_id: str,
                           vulnerable_versions: list,
                           provider="Custom",
                           issue_type=XrayIssueType.SECURITY.value,
                           severity=XrayIssueSeverity.LOW.value,
                           cve_list=None,
                           source_list=None,
                           ):
        """
        Allows an issue vendor to update an issue event
        :param issue_id:
        :param package_type:
        :param summary:
        :param description:
        :param component_id:
        :param vulnerable_versions:
        :param provider:
        :param issue_type:
        :param severity:
        :param cve_list:
        :param source_list:
        :return:
        """
        assert len(issue_id) > 0
        if cve_list is None:
            cve_list = []
        if source_list is None:
            source_list = []
        url = self.base_url + "/api/v1/events/" + issue_id
        json_data = {
            "id": issue_id,
            "package_type": package_type,
            "type": issue_type,
            "provider": provider,
            "summary": summary,
            "description": description,
            "severity": severity,
            "components": [
                {
                    "id": component_id,
                    "vulnerable_versions": vulnerable_versions
                }
            ],
            "cves": cve_list,
            "sources": source_list,
        }
        response = self.rest_put(
            url,
            json_data=json_data
        )
        return response

    def get_issue_event(self, issue_id: str, api_version='v1'):
        """
        Gets an issue created by a vendor
        :param issue_id:
        :param api_version: v1 is deprecated in Xray version 3.51.0 and v2 since 3.51.0
        :return:
        """
        assert len(issue_id) > 0
        assert api_version in ['v1', 'v2']
        url = self.base_url + f'/api/{api_version}/events/{issue_id}'
        response = self.rest_get(
            url
        )
        return response
