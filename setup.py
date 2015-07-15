import setuptools

def get_requirements(file_name='requirements.txt'):
    filename = open(file_name)
    lines = [i.strip() for i in filename.readlines()]
    filename.close()
    return lines


setuptools.setup(
    name="blog",
    version="0.1.0",
    url="https://github.com/helderm/blog",

    author="Helder Martins",
    author_email="heldergaray@gmail.com",

    description="My personal tech deviations",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=get_requirements(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
