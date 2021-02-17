from setuptools import setup, find_packages
 
setup(name='clida',
      version='1.0',
      url='https://github.com/RenatYakublevich/clida',
      license='MIT',
      author='Renat Yakublevich',
      author_email='merlinincorp@gmail.com',
      description='clida - console line interface designer application',
      packages=find_packages(exclude=['clida']),
      long_description=open('README.md').read(),
      zip_safe=False)