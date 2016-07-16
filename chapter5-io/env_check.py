import os

confdir = os.getenv("JAVA_HOME")
conffile = 'env_check.conf'
conffilename = os.path.join(confdir, conffile)

for env_check in open(conffilename):
	env_check = env_check.strip()
	print('({})'.format(env_check))
	newenv = os.getenv(env_check)

	if newenv is None:
		print(env_check + 'is not set')
	else:
		print ('Current String for {}={}\n'.format(env_check, newenv))