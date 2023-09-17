from setuptools import setup

setup(name='useful',
      version='0.0.1',
      description='Very useful code',
      url='hhtp',
      author='Vitalii',
      author_email='test@mail.com',
      license='MIT',
      packages=['useful'],
      include_package_data=True,
      install_requires=['markdown'],
      entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
      )