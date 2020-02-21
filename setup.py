import logging
import os

from setuptools import find_packages, setup

logger = logging.getLogger(__name__)

# Get the base directory
here = os.path.dirname(__file__)
if not here:
    here = os.path.curdir
here = os.path.abspath(here)

try:
    readme = os.path.join(here, "README.md")
    long_description = open(readme, "r").read()
except IOError:
    logger.warning("README file not found or unreadable.")
    long_description = "See https://github.com/arpitbbhayani/overload"

setup(
    name="overload",
    zip_safe=False,
    version="0.1.0",
    description="Overload Functions in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arpit Bhayani",
    author_email="arpit.b.bhayani@gmail.com",
    url="https://github.com/arpitbbhayani/overload",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["README.md"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.4",
    install_requires=[],
)
