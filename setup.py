import os
import re

from setuptools import setup, find_packages


def read_meta():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'gtdb/__init__.py')
    with open(path) as fh:
        hits = re.findall(r'__(\w+)__ ?= ?["\'](.+)["\']\n', fh.read())
    return {k: v for k, v in hits}


def readme():
    with open('README.md') as f:
        return f.read()


meta = read_meta()
setup(name=meta['title'],
      version=meta['version'],
      description=meta['description'],
      long_description=readme(),
      long_description_content_type='text/markdown',
      author=meta['author'],
      author_email=meta['author_email'],
      url=meta['url'],
      license=meta['license'],
      project_urls={
          'Bug Tracker': meta['bug_url'],
          'Documentation': meta['doc_url'],
          'Source Code': meta['src_url'],
      },
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      packages=find_packages(),
      include_package_data=True,
      install_requires=['tqdm'],
      python_requires='>=3.6',
      )
