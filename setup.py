from distutils.core import setup

setup(
    name='predictors_api',
    version='0.1',
    packages=['predictor'],
    url='',
    license='Raphaël Courivaud',
    author='Raphaël Courivaud',
    author_email='r.courivaud@gmail.com',
    description='Python Library used to release Machine Learning predictors on Flask API ',
    install_requires=[
        "flask"
    ]
)
