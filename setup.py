try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'libnemesis',
    'author': "Student Robotics Competitor Services Team",
    'url': 'https://github.com/srobo/libnemesis',
    'download_url': 'https://github.com/srobo/libnemesis',
    'author_email': 'srobo-devel@googlegroups.com',
    'version': '0.0.1',
    'install_requires': ['nose', 'python-ldap', 'Unidecode'],
    'packages': ['libnemesis'],
    'scripts': [],
    'name': 'libnemesis'
}

setup(**config)
