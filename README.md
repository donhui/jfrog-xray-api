# Python wrapper for JFROG Xray REST API
`jfrog-xray-api` is a live python package for JFrog Xray REST API. 

# Install
```
pip install jfrog-xray-api
```
# Usage

## Authentication
```python
# User and password OR API_KEY
from xray import XrayRestClient
xray_rest_client = XrayRestClient(
    base_url="http://localhost:8082/xray",
    username='USERNAME',
    password='PASSWORD or API_KEY'
)
```
## Components
### Find Component by Name
```python
components = xray_rest_client.components
response = components.find_component_by_name("jenkinsapi")
print(response.json())
```
### Find Components by CVEs
```python
components = xray_rest_client.components
cve_list = ['CVE-2021-4104']
response = components.find_components_by_cves(cve_list)
print(response.json())
```
### Find CVEs by Components
```python
components = xray_rest_client.components
components_id_list = ['gav://commons-collections:commons-collections:3.2.1', 'gav://commons-collections:commons-collections:3.2.2']
response = components.find_cves_by_components(components_id_list)
print(response.json())
```
### Get Component List Per Watch
```python
# TODO
```
### Get Artifact Dependency Graph
```python
components = xray_rest_client.components
artifact_path = '/Artifactory/pnnl/goss/goss-core-client/0.1.7/goss-core-client-0.1.7-sources.jar'
response = components.get_artifact_dependency_graph(artifact_path)
print(response.json())
```
### Compare Artifacts
```python
components = xray_rest_client.components
source_artifact_path = '/Artifactory/pnnl/goss/goss-core-client/0.1.7/goss-core-client-0.1.7-sources.jar'
target_artifact_path = '/Artifactory/pnnl/goss/goss-core-client/0.1.8/goss-core-client-0.1.8-sources.jar'
response = components.compare_artifacts(source_artifact_path, target_artifact_path)
print(response.json())
```
### Get Build Dependency Graph
```python
components = xray_rest_client.components
artifactory_instance = "myInstance",
build_name = "someBuild",
build_number = "someNumber"
response = components.get_build_dependency_graph(artifactory_instance, build_name, build_number)
print(response.json())
```
### Compare Builds
```python
components = xray_rest_client.components
response = components.compare_builds(
    "my-instance", "someOriginBuild", "111",
    "my-instance", "someTargetBuild", "222",
)
print(response.json())
```
### Export Component Details
```python
# TODO
```
