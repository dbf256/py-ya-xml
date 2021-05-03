from setuptools import setup

setup(name='pyyaxml',
      version='0.6.2',
      description='Python API to Yandex.XML',
      url='https://github.com/dbf256/py-ya-xml',
      author='Alexey Moskvin',
      author_email='dbf256@gmail.com',
      license='MIT',
      packages=['pyyaxml'],
      install_requires=[
          'six',
      ],
      zip_safe=False)
