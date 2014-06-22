import os
import sys
settings=open('/var/is2/aps/settings.py', 'r+')
settings2=open('/var/is2/aps/settings2.py', 'w')
for line in settings:
	if line.find('projectManager')>0:
		settings2.write(line.replace('projectManager', sys.argv[1]))
	elif line.find('EBUG = True')>0:
		settings2.write(line.replace('DEBUG = True', 'DEBUG = False'))	
	elif line.find('LLOWED_HOSTS')>0:
		settings2.write(line.replace('ALLOWED_HOSTS = []',"ALLOWED_HOSTS =['*']"))
	else:
		settings2.write(line)

wsgi=open('/var/is2/aps/wsgi.py', 'r+')
wsgi2=open('/var/is2/aps/wsgi2.py', 'w')
wsgi2.write('import sys\n')
wsgi2.write("sys.path.append('/var/is2')\n")
wsgi2.write("sys.path.append('/var/is2/aps')\n")
for line in wsgi:
	wsgi2.write(line)

manage=open('/var/is2/aps/manage.py', 'r+')
manage2=open('/var/is2/aps/manage2.py', 'w')
manage2.write('import sys\n')
manage2.write("sys.path.append('/var/is2')\n")
manage2.write("sys.path.append('/var/is2/aps')\n")
for line in manage:
	manage2.write(line)





settings.close()
settings2.close()
wsgi.close()
wsgi2.close()
os.remove('/var/is2/aps/settings.py')
os.rename('/var/is2/aps/settings2.py','/var/is2/aps/settings.py')
os.remove('/var/is2/aps/wsgi.py')
os.rename('/var/is2/aps/wsgi2.py','/var/is2/aps/wsgi.py')
os.remove('/var/is2/aps/manage.py')
os.rename('/var/is2/aps/manage2.py','/var/is2/aps/manage.py')
os.system('sudo -u postgres createdb ' + sys.argv[1])
