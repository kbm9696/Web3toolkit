from setuptools import setup, find_packages

setup(
    name='Web3toolkit',
    version='1.0.3',
    packages=find_packages(exclude=['tests*']),
    license='GNU General Public License v3.0',
    description='A python wrapper for the zora, mode and covalent web3 apis',
    long_description=open('README.md').read(),
    install_requires=[
        'requests',
    ],
    url='https://github.com/kbm9696/Web3toolkit',
    author='Balamurugan',
    author_email='kbala007.1996@gmail.com',
    long_description_content_type='text/markdown'
)
