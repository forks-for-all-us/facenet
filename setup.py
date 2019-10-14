from setuptools import setup, find_packages
import os

if os.path.exists("version"):
    with open("version","r") as ver:
        version = str(ver.readline())
else:
    version = "0.0.0"

# PRIVATE DEPENDENCIES (Semantix Modules/Other Projects) NOT IN PYPi.ORG
# Set the version from these packages here

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="smtx-facenet",
    version=f"{version}",
    packages=find_packages(exclude=["test", "*.test", "*.test.*", "test.*"]),
    # scripts=['say_hello.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine

    install_requires=[install_requires],

    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['version'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata to display on PyPI
    author="David Sandberg",
    author_email="ai-lab@semantix.com.br",
    description="TensorFlow implementation of the face recognizer described in the paper 'FaceNet: A Unified Embedding for Face Recognition and Clustering'.",
    keywords="Facenet, face, recognition",
    url="https://github.com/forks-for-all-us/facenet",   # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
    # classifiers=[
    #     'License :: OSI Approved :: Python Software Foundation License'
    #
    include_package_data=True

    # could also include long_description, download_url, etc.
)
