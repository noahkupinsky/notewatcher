from setuptools import setup, find_packages

setup(
    name='notewatcher',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies as needed
        'appdirs',
        'comutils',
        'cominfer',
    ],
    entry_points={
        'console_scripts': [
            'notewatcher=notewatcher.command:main',
        ],
    },
    author='Noah Kupinsky',
    author_email='noah@kupinsky.com',
    description='A tool for synchronizing note files to GitHub repositories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
