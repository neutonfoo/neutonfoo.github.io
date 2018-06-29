#!/usr/bin/env python3

import os
import re

navigationYml = '_data/navigation.yml'
folders = ('guides',)
mainNav = """
main:
  - title: "Guides"
    url: /guides/
  - title: "Contact"
    url: /contact/
"""

navigationYmlF = open(navigationYml, 'w')
navigationYmlF.write('###### Autogenerated Navigation ######')
navigationYmlF.write('\n')
navigationYmlF.write(mainNav)
navigationYmlF.write('\n')

for folder in folders:
	for subFileOrFolder in os.listdir(folder):
		fullDir = folder + '/' + subFileOrFolder
		if os.path.isdir(fullDir):
			navName = subFileOrFolder + '-nav:'

			navigationYmlF.write(navName + '\n')
			navigationYmlF.write('  - title: "Jump to"\n')
			navigationYmlF.write('    children:\n')

			indexMdDir = fullDir + '/index.md'

			indexMdF = open(indexMdDir, 'r')
			for line in indexMdF:
				if line[:2] == '##':
					sectionTitle = line[3:-1]
					sectionLocationHash = re.sub(r'[^\w\s]', '', sectionTitle)
					sectionLocationHash = sectionLocationHash.lower()
					sectionLocationHash = sectionLocationHash.replace(' ', '-')

					navigationYmlF.write('      - title: "' + sectionTitle + '"\n')
					navigationYmlF.write('        url: "' + fullDir + '#' + sectionLocationHash + '"\n')
			navigationYmlF.write('\n')
