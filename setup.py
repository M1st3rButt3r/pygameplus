import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygameplus",
    version="0.0.1",
    author="M1st3rButt3r",
    author_email="m1st3rbutt3r@gmail.com",
    description="A small addon for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M1st3rButt3r/pygameplus",
    project_urls={
        "Bug Tracker": "https://github.com/M1st3rButt3r/pygameplus/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'pygame'
    ],
    setup_requires=[
        'pygame'
    ]
)