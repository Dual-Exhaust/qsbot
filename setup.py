from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='qsbot',
    version='0.0.1',
    description='''A library for easy discord bot development''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Dual-Exhaust',
    author_email='kylecsacco@gmail.com',
    license='MIT',
    packages=['qsbot', 'qsbot/examples', 'qsbot/basicbot'],
    python_requires='>=3.7',
    scripts=['bin/qs_install_examples', 'bin/makebot'],
    install_requires=['discord.py==1.2.4'],
    include_package_data=True,
    zip_safe=False)
