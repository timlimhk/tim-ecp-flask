import setuptools

setuptools.setup(
    name="TimEcpFlask",
    version="0.0.1",
    author="Tim Lim",
    author_email="timlimhk@gmail.com",
    description="A small example package",
    url="https://github.com/timlimhk/tim-ecp-flask",
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'flask',
        'rfc3339',
        'pytest',
        'pytest-flask',
        'requests',
        'coverage',
    ],
    entry_points={
       'console_scripts': [
           'TimEcpFlask = TimEcpFlask.cli:cli'
       ]
    },
)
