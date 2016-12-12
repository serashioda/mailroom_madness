from setuptools import setup

setup(
    name="mailroom",
    description="Python 401 Mailroom madness project",
    version=0.1,
    author="Casey O'Kane" "Sera Smith",
    license="MIT",
    py_modules=["mailroom"],
    install_requires=["pytest", "tox"],
    extras_require={"test": ["pytest", "tox"]},
)
