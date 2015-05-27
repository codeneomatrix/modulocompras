from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6','Unipath==0.2.1','Pillow==2.3.0','python-mimeparse==0.1.4','dateutil==1.5','lxml==3.3.3', 'defusedxml==0.4.1','django-tastypie==0.9.15',]


if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

