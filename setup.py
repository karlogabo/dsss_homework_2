from setuptools import setup, find_packages

setup(
    name='DSSHomework',
    version='0.1',
    author='Karlo Fonseca',
    author_email='karlogabo51@gmail.com',
    description='Homework for DSSS and hello there :)',
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package.module:main_function',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
