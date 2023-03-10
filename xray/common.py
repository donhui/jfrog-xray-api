from enum import Enum


class PackageType(Enum):
    ALPINE = "alpine"
    BOWER = "bower"
    CHEF = "chef"
    COCOAPODS = "cocoapods"
    COMPOSER = "composer"
    CONAN = "conan"
    CRAN = "cran"
    DEBIAN = "debian"
    DOCKER = "docker"
    GEMS = "gems"
    GENERIC = "generic"
    GO = "go"
    GRADLE = "gradle"
    HELM = "helm"
    IVY = "ivy"
    MAVEN = "maven"
    NPM = "npm"
    NUGET = "nuget"
    PUPPET = "puppet"
    PYPI = "pypi"
    RPM = "rpm"
    SBT = "sbt"
    YUM = "yum"
