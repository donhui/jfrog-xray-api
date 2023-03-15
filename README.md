# Python wrapper for JFROG Xray REST API
`jfrog-xray-api` is a live python package for JFrog Xray REST API. 

[![jfrog-xray-api on PyPI](https://img.shields.io/pypi/v/jfrog-xray-api.svg)][1]
[![jfrog-xray-api license](https://img.shields.io/pypi/l/jfrog-xray-api.svg)][2]
[![jfrog-xray-api downloads](https://pepy.tech/badge/jfrog-xray-api)][3]
[![jfrog-xray-api downloads/month](https://static.pepy.tech/badge/jfrog-xray-api/month)][3]
![pylint](https://github.com/donhui/jfrog-xray-api/actions/workflows/pylint.yml/badge.svg)


[1]: https://pypi.python.org/pypi/jfrog-xray-api
[2]: https://github.com/donhui/jfrog-xray-api/blob/master/LICENSE
[3]: https://pepy.tech/project/jfrog-xray-api


# Tables of Contents

<!-- toc -->
- [Install](#install)
- [Usage](#usage)
  * [Authentication](#authentication)
  * [SYSTEM](#system)
    + [Create Bundle](#create-bundle)
    + [Ping Request](#ping-request)  
    + [Get Version](#get-version)
    + [Metrics](#metrics)
  * [Components](#components)
    + [Find Component by Name](#find-component-by-name)
    + [Find Components by CVEs](#find-components-by-cves)
    + [Find CVEs by Components](#find-cves-by-components)
    + [Get Component List Per Watch](#get-component-list-per-watch)
    + [Get Artifact Dependency Graph](#get-artifact-dependency-graph)
    + [Compare Artifacts](#compare-artifacts)
    + [Get Build Dependency Graph](#get-build-dependency-graph)
    + [Compare Builds](#compare-builds)
    + [Export Component Details](#export-component-details)
  * [SUMMARY](#summary)
    + [Build Summary](#build-summary)
    + [Artifact Summary](#artifact-summary)
  * [ISSUES](#issues)   
    + [Create Issue Event](#create-issue-event)
    + [Update Issue Event](#update-issue-event)
    + [Get Issue Event](#get-issue-event)
  * [SCANNING](#scanning)   
    + [Scan Artifact](#scan-artifact)  
    + [Scan Build](#scan-build)
    + [Scan Status](#scan-status)
    + [Scan Now](#scan-now)
<!-- tocstop -->

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

## SYSTEM
### Create Bundle
```python
system = xray_rest_client.system
response = system.create_bundle("bundle-2023-001")
print(response.json())
```
### Ping Request
```python
system = xray_rest_client.system
response = system.system.send_ping()
print(response.json())
```
### Get Version
```python
system = xray_rest_client.system
response = system.get_version()
print(response.json())
```
### Metrics
```python
system = xray_rest_client.system
response = system.get_metrics()
print(response.json())
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

## SUMMARY
### Build Summary
```python
summary = xray_rest_client.summary
response = summary.get_build_summary("build_name", "123")
print(response.json())
```
### Artifact Summary
```python
summary = xray_rest_client.summary
response = summary.get_artifact_summary(paths=["/Artifactory/pnnl/goss/goss-core-client/0.1.7/goss-core-client-0.1.7-sources.jar"])
print(response.json())
```

## Issues
### Create Issue Event
```python
from xray.common import PackageType
issues = xray_rest_client.issues
response = issues.create_issue_event(
    issue_id='test-2023-0221',
    summary='test-2023-0221',
    description='test-2023-0221',
    package_type=PackageType.MAVEN.value,
    component_id='com.test:test',
    vulnerable_versions=["[1.0.10.2,)"],
)
print(response.json())
```

### Update Issue Event
```python
from xray.common import PackageType
issues = xray_rest_client.issues
response = issues.update_issue_event(
    issue_id='test-2023-0221',
    summary='test-2023-0221',
    description='test-2023-0221 update',
    package_type=PackageType.MAVEN.value,
    component_id='com.test:test',
    vulnerable_versions=["[1.0.10.2,)"],
)
print(response.content)
```
### Get Issue Event
```python
issues = xray_rest_client.issues
# get issue event v1
# Note: This API is deprecated in Xray version 3.51.0
response = issues.get_issue_event("test-2023-0221")
# get issue event v2
# Since: Xray  3.51.0
response = issues.get_issue_event("test-2023-0221", api_version="v2")
print(response.json())
```

## SCANNING
### Scan Artifact
```python
scanning = xray_rest_client.scanning
response = scanning.scan_artifact("docker://image_name:image_tag")
print(response.json())
```
### Scan Build
```python
scanning = xray_rest_client.scanning
# scan build v1
response = scanning.scan_build("build_name", "build_number")
# scan build v2
# Starting from Xray version 3.42.3
response = scanning.scan_build("build_name", "build_number", api_version='v2')
print(response.json())
```

### Scan Status
```python
from xray.common import PackageType
scanning = xray_rest_client.scanning
# get scan status for artifact
response = scanning.get_scan_status_for_artifact(
    PackageType.NPM.value,
    'npm-local/static-module-3.0.4.tar.gz',
    'b0a887f6e5c16134b7d1280c2150d38811357642d56c622c6f7f6b239f668608'
)
print(response.json())
# get scan status for build
scanning = xray_rest_client.scanning
response = scanning.get_scan_status_for_build("test-build", "1")
print(response.json())
# get scan status for build with project
scanning = xray_rest_client.scanning
response = scanning.get_scan_status_for_build("test-build", "1", project="proj1")
print(response.json())
```

### Scan Now
```python
from xray.common import PackageType
scanning = xray_rest_client.scanning
# scan now
response = scanning.scan_now("local-maven-repo/org/jenkins-ci/main/jenkins-war/2.289.1/jenkins-war-2.289.1.war")
print(response.json())
```