__author__ = 'root'
import os
os.system('rm ../doc/* -r -f; cd ..; pwd; epydoc aps/aplicaciones/* --docformat reStructuredText -o doc/ > /dev/null')
