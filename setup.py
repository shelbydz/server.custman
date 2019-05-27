from setuptools import setup


requires = [
    'pyramid',
    'waitress',
    'pyramid_chameleon'
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(
    name='custman',
    install_requires=requires,
    extra_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = custman:main'
            ]
        }
)
