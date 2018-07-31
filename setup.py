import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='msfdevops',
        version='1.0',
        description='Example repo for MSF Dev Ops',
        author='Jessica A. Nash',
        author_email='janash@vt.edu',
        url="https://github.com/janash/msfdevops",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
        ],
        extras_require={
            'docs': [
                'sphinx',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=False,
    )
