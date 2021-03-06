# Copyright (c) 2014-2018. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import os

from setuptools import setup

readme_filename = "README.md"
current_directory = os.path.dirname(__file__)
readme_path = os.path.join(current_directory, readme_filename)

# if README parsing fails, we'll still at least have this empty string
try:
    with open(readme_path, 'r') as f:
        readme_markdown = f.read()
except Exception as e:
    readme_markdown = ""
    print (e)
    print("Failed to open %s" % readme_path)

try:
    import pypandoc
    readme_restructured = pypandoc.convert(readme_markdown, to='rst', format='md')
except Exception as e:
    readme_restructured = readme_markdown
    print(e)
    print("Conversion of long_description from MD to reStructuredText failed")
    pass


if __name__ == '__main__':
    setup(
        name='typechecks',
        version="0.1.0",
        description="Helper functions for runtime type checking",
        author="Tim O'Donnell",
        author_email="tim.odonnell@mssm.edu",
        url="https://github.com/openvax/typechecks",
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
        ],
        install_requires=[],
        long_description=readme_restructured,
        packages=['typechecks'],
    )
