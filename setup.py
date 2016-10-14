from setuptools import setup, find_packages

setup(
    name='jbook',
    version='0.0.1',
    description='WebBook authoring framework built on jupyter notebooks',
    author='Loic Dutrieux',
    install_requires=['nbconvert',
                      'bs4',
                      'jinja2',
                      'Click'],
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
    [console_scripts]
    nb2book=jbook.scripts.cli:nb2book
    """
)