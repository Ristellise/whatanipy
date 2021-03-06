import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatanipy",
    version="0.0.1",
    author="Ristellise",
    author_email="joshwoo71@gmail.com",
    description="Whatanime.ga python wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ristellise/whatanipy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['requests', 'human_time_formatter'],
)
