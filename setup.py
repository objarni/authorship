
#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

VERSION = "0.1"
AUTHORS = '''Olof Bjarnason'''
HOMEPAGE = 'https://github.com/objarni/authorship'


if __name__ == '__main__':
    setup(
        name='authorship',
        version=VERSION,
        description='Analyse line-by-line authorship of a git repository',
        long_description='Use instructions found on home page. Happy hacking, contributions welcome!',
        author=AUTHORS,
        author_email="olof.bjarnason@gmail.com",
        license='MIT',
        url=HOMEPAGE,
        scripts=['src/authorship.py'],
        test_suite='nose.collector',
        zip_safe=True
    )
