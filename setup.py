from setuptools import setup

setup(
    name='process_vse_sort',
    author='Gabriel Montagné Láscaris-Comneno',
    author_email='gabriel@tibas.london',
    license='MIT',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'process_vse_sort = process_vse_sort.__main__:main'
        ]
    }
)
