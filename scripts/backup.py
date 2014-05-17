__author__ = 'root'
import os
os.system('pg_dump -U postgres -W -h localhost projectManager -a > backup.sql')
