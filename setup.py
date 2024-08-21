"""
Flask-JSGlue
------------

Flask-JSGlue helps hook up your Flask application nicely with the front end.

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Flask-JSGlue',
    version='0.3.2', 
    url='https://github.com/sisitrs2/Flask-JSGlue',
    license='BSD',
    author='Daniel Arad', 
    author_email='sisitrs2@gmail.com',  # Optionally updated email
    description='Flask-JSGlue helps hook up your Flask application nicely with the front end.',
    long_description=__doc__,
    py_modules=['flask_jsglue'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=2.0.0',
        'Jinja2>=3.1.0',
        'Werkzeug>=2.0.0',
        'MarkupSafe>=2.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
