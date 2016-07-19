from pip.req import parse_requirements
from setuptools import find_packages
from setuptools import setup
from subprocess import call
from setuptools.command.install import install as _install


install_requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_requirements]


class install(_install):

    def run(self):
        _install.run(self)


setup(
    name='lights',
    version='0.1.1',
    author='Karim Mango',
    author_email='karim.mango@magine.com',
    description="""
       This is a Raspberry Pi experiment, utilizing the addon Piface to the
       Raspberry Pi to connect speakers, warning tower light, and siren
       combined with code in Python to simultaneously fire off the lights
       and play an mp3 file.""",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    cmdclass={'install': install},
    license='MIT',					
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'lights=lights.server:run',
        ]},
    )
