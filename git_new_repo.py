#!/usr/bin/env python

##import libraries
import argparse
import subprocess
import os
import re

##set arguments used in script
parser = argparse.ArgumentParser(description='Commit new or update git repo. Prior to comming new repo, one must be made on github')
parser.add_argument('-p', '--push_pull', dest='push_pull', help="do you want to push ('push') or pull ('pull') a repository?", required=True)
parser.add_argument('-d', '--directory', dest='directory', help='pathway to working directory, where the repository is (or will be) kept', required=True)
parser.add_argument('-r', '--name_of_repository', dest='repository_name', help="name give for repository when you made (this will be echo'd into README.md file")
parser.add_argument('-c', '--commit', dest='commit', help='name of commit')
parser.add_argument('-s', '--ssh', dest='ssh', help='ssh address of repository to be pulled from or to be pushed to')
parser.add_argument('-f', '--file', dest='file', help='name of file in working directory to commit', required=True)

args = parser.parse_args()
##set directory
os.chdir(args.directory)

if args.push_pull == 'pull':
	parser = argparse.ArgumentParser(description='Pull git repo')

elif args.push_pull == 'push':

	f = open('README.md', 'w')
	a = f"echo '# {args.repository_name}'"
	subprocess.call(a, shell=True, stdout=f)
	subprocess.Popen('git init', shell=True)
	subprocess.Popen('git add README.md', shell=True)
	subprocess.Popen(f'git add {args.file}', shell=True)
	subprocess.Popen(f"git commit -m {args.commit}", shell=True)
	subprocess.Popen('git branch -M main', shell=True)
	subprocess.Popen(f'git remote add origin {args.ssh}', shell=True)
	subprocess.Popen('git push -u origin main', shell=True)
