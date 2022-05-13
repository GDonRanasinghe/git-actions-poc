from setuptools import setup, find_packages

setup(
    name="git-actions-poc",
    version="0.0.6",
    author="Gishan Don Ranasinghe",
    author_email="gishan.ranasinghe@gsscogs.uk",
    description="Git actions test poc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["git-actions-poc = src.main:main"]},
)
