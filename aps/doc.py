__author__ = 'root'
import os
os.system('rm ../doc/* -r -f; cd ..; pwd; epydoc aps/aplicaciones/* -o doc/ > /dev/null')
#os.system('epydoc ./aplicaciones/ -o ../doc')
#os.system('ls ./aplicaciones/')
#os.system('epydoc aps/aplicaciones/* doc/ ')