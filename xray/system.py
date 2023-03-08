from xray.utils.http import RestApiAccessor


class XraySystem(RestApiAccessor):
    """
    Xray REST API: SYSTEM
    See: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API#XrayRESTAPI-SYSTEM
    """

    def get_version(self):
        """
        Gets the Xray version and revision you are running
        :return:
        """
        url = self.base_url + "/api/v1/system/version"
        response = self.rest_get(
            url
        )
        return response

    def get_metrics(self):
        """
        Get system metrics data
        :return:
        """
        url = self.base_url + "/api/v1/metrics"
        response = self.rest_get(
            url
        )
        return response

    def create_bundle(self,
                      bundle_name: str,
                      bundle_description='',
                      include_configuration=True,
                      include_system=True,
                      include_logs=False,
                      logs_start_date='2023-02-17T16:32:04+03:00',
                      logs_end_date='2023-02-17T16:32:04+03:00',
                      thread_dump_count=1,
                      thread_dump_interval=0,
                      ):
        """
        Create support bundle
        :return:
        """
        url = self.base_url + "/api/v1/system/support/bundle"
        json_data = {
            "name": bundle_name,
            "description": bundle_description,
            "parameters": {
                "configuration": include_configuration,
                "system": include_system,
                "logs": {
                    "end_date": logs_end_date,
                    "include": include_logs,
                    "start_date": logs_start_date,
                },
                "thread_dump": {
                    "count": thread_dump_count,
                    "interval": thread_dump_interval
                }
            }
        }
        response = self.rest_post(
            url,
            json_data=json_data
        )
        return response

    def send_ping(self):
        """
        Sends a ping request
        :return:
        """
        url = self.base_url + "/api/v1/system/ping"
        response = self.rest_get(
            url
        )
        return response
