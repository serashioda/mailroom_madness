from setup tools import setup

setup(
    name="mailroom",
    description="Python 401 Mailroom madness project",
    version=0.1,
    author="Casey O'Kane", "Sera Smith",
    license="MIT",
    py_modules=["mailroom"],
    install_requires=[],
    extras_require={"test": ["pytest", "tox"]},
)