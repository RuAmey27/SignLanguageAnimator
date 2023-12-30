import setuptools

setuptools.setup(
    name='Audio and Text to ISL converter',
    version='0.1.0',
    description='Python project',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)