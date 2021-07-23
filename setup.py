import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scpreader",
    version="0.2.5",
    scripts=['scp_reader'],
    author="Gaffclant",
    author_email="gaffclant@gmail.com",
    description="Read the scp wiki from the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaffclant/scp-reader",
    project_urls={
        "Bug Tracker": "https://github.com/gaffclant/scp-reader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
