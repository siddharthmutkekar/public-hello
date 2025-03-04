import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="public_hello",
    version="0.2",
    author="Siddharth",
    author_email="siddharth.git@gmail.com",
    description="A public github-hosted python package for test, with dependency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.ibm.com/SiddharthMutkekar/public-hello",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)
