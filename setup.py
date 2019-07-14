import os
import setuptools

setuptools.setup(
    name = "jhulib_slack_api",
    version = "0.0.1",
    author = "Derek Belrose",
    author_email = "dbelrose@jhu.edu",
    description = ("A python implementation of the slack API including SCIM"),
    license = "Apache",
    keywords = "slack api scim",
    url = "https://github.com/jhu-sheridan-libraries/python_slack_api",
    packages=setuptools.find_packages()
)