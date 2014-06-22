python configurar.py $1
python /var/is2/aps/manage.py syncdb
service apache2 restart
