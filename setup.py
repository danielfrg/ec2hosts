import versioneer

from distutils.core import setup
from setuptools import find_packages

cmdclass = versioneer.get_cmdclass()

setup(
    name="ec2hosts",
    version=versioneer.get_version(),
    author="Daniel Rodriguez",
    author_email="df.rodriguez143@gmail.com",
    url="https://github.com/danielfrg/ec2hosts",
    cmdclass=cmdclass,
    license="Apache License Version 2.0, January 2004",
    install_requires=["boto3", "click"],
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        ec2hosts=ec2hosts.cli:main
    """,
)
