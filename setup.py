# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['datacenter', 'datacenter.migrations']

package_data = \
{'': ['*'], 'datacenter': ['templates/*']}

install_requires = \
['django==1.11.21', 'psycopg2==2.7.3.1', 'pytz==2017.2']

setup_kwargs = {
    'name': 'datacenter',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
