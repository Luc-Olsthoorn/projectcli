from setuptools import setup

setup(name='projectcli',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Luc Olsthoorn',
      author_email='me@lucolsthoorn.com',
      license='MIT',
      packages=['projectcli'],
      entry_points = {
        'console_scripts': [
            'projectcli=projectcli.cli:main',
        ],
      },
      zip_safe=False)