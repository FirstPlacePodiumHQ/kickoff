from setuptools import setup, find_packages

setup(
    name="kick-off",
    version="1.0.0",
    description="Automated folder and file creation for documenting your learning journey",
    author="Moh Ryan Alfa Maulana",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pytest>=5.0"],
    entry_points={
        "console_scripts": [
            "kick-off=kickoff:main",
        ]
    },
)
