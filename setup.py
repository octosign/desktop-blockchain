import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='octosignblockchain-durasj',
    version='0.0.1',
    author='Jakub Duras',
    author_email='jakub@duras.me',
    description='Experimental Octosign backend using blockchain for document signing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/durasj/octosign-blockchain',
    test_suite='tests',
    packages=['octosign-blockchain'],
    scripts=['scripts/dist.sh'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
