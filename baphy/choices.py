from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ProjectTypeChoice(Enum):
    EXECUTABLE = "Executable"
    HEADER_ONLY = "Header-only library"
    SHARED_LIBRARY = "Shared library"
    STATIC_LIBRARY = "Static library"


class PackageManagerChoice(Enum):
    NONE = "None"
    CONAN = "Conan"
    VCPKG = "Vcpkg"


class TestingFrameworkChoice(Enum):
    NONE = "None"
    GOOGLETEST = "GoogleTest"
    CATCH2 = "Catch2"
    DOCTEST = "Doctest"


@dataclass
class Choices:
    project_type: Optional[ProjectTypeChoice] = None
    package_manager: Optional[PackageManagerChoice] = None
    testing_framework: Optional[TestingFrameworkChoice] = None
