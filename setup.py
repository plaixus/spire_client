from collections import OrderedDict
from setuptools import find_packages, setup

setup(
    name='spire-client',
    version='0.1',
    description='A library to interact with the SPIRE server',
    long_description='SPIRE client provides multiple helper functions to allow communication with the SPIRE server and manipulation of ROS bagfiles and topics',
    author="Plaixus",
    author_email="admin@plaixus.com",
    maintainer="Michael Rizakis, Mike Karamousadakis",
    maintainer_email="michail.rizakis@plaixus.com, mike@plaixus.com",
    url="https://github.com/plaixus/spire_client",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/plaixus/spire_client"),
            ("Issue tracker", "https://github.com/plaixus/spire_client/issues"),
        )
    ),
    license="APACHE 2.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8.0",
)
