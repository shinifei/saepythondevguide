
from setuptools import setup

setup(
    name = "sae-python-dev",
    version = "1.0testing",
    author = "Jaime Chen",
    author_email = "chenzheng2@staff.sina.com.cn",
    description = ("SAE Python development server"),
    install_requires = [
        'Werkzeug',
        'pip',
        'PyYAML',
        'argparse',
        #'Django==1.2.7',
        #'bottle==0.9.6',
        #'tornado==2.1.1',
        #'Flask==0.7.2',
        #'Uliweb',
        #"web.py==0.36",
        #'flask-sqlalchemy',
        #'jinja2',
        #'MySQL-python'
        ],
    platforms='any',
    license = "",
    url = "http://appstack.sinaapp.com",
    packages=['sae'],
    scripts = ['dev_server.py', 'saecloud'],
)
