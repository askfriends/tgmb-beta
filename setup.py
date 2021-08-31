import setuptools

setuptools.setup(
    name="tgmb-beta",
    version="1.1b",
    author="SomesH S",
    author_email="ksssomesh12@gmail.com",
    description="tgmb-beta",
    long_description=open('README.md', 'rt', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ksssomesh12/tgmb-beta",
    project_urls={
        "Bug Tracker": "https://github.com/ksssomesh12/tgmb-beta/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt', 'rt', encoding='utf-8').read().split('\n'),
    python_requires=">=3.8"
)
