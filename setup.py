#!/usr/bin/env python
from setuptools import setup, find_packages, Extension

# proj = Extension('proj', sources=[ 'proj/main', 
#                                     'proj/main.m', 
#                                     'proj/Makefile', 
#                                     'proj/build/imageleap', 
#                                     'proj/imageleap.xcodeproj/project.xcodeworkspace/xcshareddata/imageleap.xccheckout', 
#                                     'proj/imageleap.xcodeproj/project.xcodeworkspace/contents.xcworkspace', 
#                                     'proj/imageleap.xcodeproj/project.pbxproj/'], 
#                         depends=['proj/main', 
#                                     'proj/main.m', 
#                                     'proj/Makefile', 
#                                     'proj/build/imageleap', 
#                                     'proj/imageleap.xcodeproj/project.xcodeworkspace/xcshareddata/imageleap.xccheckout', 
#                                     'proj/imageleap.xcodeproj/project.xcodeworkspace/contents.xcworkspace', 
#                                     'proj/imageleap.xcodeproj/project.pbxproj/'])

setup(name='greatjob',
      version='1.0',
      description='Congratulations',
      author='Celeen Rusk',
      author_email='celeenrusk@gmail.com',
      liscense="MIT",
      # ext_modules=[proj],
      packages=find_packages(),
      package_data={
            '': ['imageleap', 'sparkle.png', 'thumbsup.png', 'proj/*']
      },
      entry_points={
      	'console_scripts': [
      		'greatjob=greatjob:main'
      	]
      }
     )