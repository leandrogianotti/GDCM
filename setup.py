import sys

from skbuild import setup

def exclude_static_libraries(cmake_manifest):
    return list(filter(lambda name: not (name.endswith('.a')), cmake_manifest))

setup(
    name="gdcm-tools",
    version="3.0.25",
    description="GDCM tools wrapped into a Python package",
    author='The scikit-build team',
    license="Simplified BSD license,",
    setup_requires=[],
    package_data={
        "": ["*"]
    },
    py_modules=['cmake'],
    long_description=open('README.Copyright.txt').read(),
    cmake_args=['-DGDCM_WRAP_PYTHON:BOOL=OFF',
                '-DGDCM_DOCUMENTATION_SKIP_MANPAGES:BOOL=TRUE',
                '-DGDCM_DOCUMENTATION:BOOL=FALSE',
                '-DGDCM_BUILD_APPLICATIONS:BOOL=ON',
                '-DGDCM_BUILD_DOCBOOK_MANPAGES:BOOL=OFF',
                '-DGDCM_BUILD_SHARED_LIBS:BOOL=OFF'],
    cmake_process_manifest_hook=exclude_static_libraries
)