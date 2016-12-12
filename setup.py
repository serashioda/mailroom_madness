"""This is the setup for the mailroom_madness."""

from setuptools import setup

setup(
    name="mailroom",
    description="Python 401 Mailroom madness project",
    version=0.1,
    author="Casey O'Kane" "Sera Smith",
    authors_email="seras37@gmail.com",
    license="MIT",
    py_modules=["mailroom"],
    package_dir={'': 'src'},
    install_requires=["pytest", "tox"],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", "tox"]
    },
)