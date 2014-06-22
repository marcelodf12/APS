#apt-get install apache2 libapache2-mod-wsgi
#sudo apt-get install python-pip
#sudo apt-get install python-virtualenv
if [ "$1" = "1.0" ]
then
  url='https://github.com/marcelodf12/APS/archive/v'$1'.tar.gz'
  archivo='v'$1'.tar.gz'
else
  url='https://github.com/marcelodf12/APS/archive/V'$1'.tar.gz'
  archivo='V'$1'.tar.gz'
fi
echo 'Se esta descargando la version '$1
wget $url > /dev/null
echo 'Descargar completa'
echo 'Desempaquetando...'
tar -xvf $archivo > /dev/null
echo 'Desempaquetado completo.'
actual=$(pwd)
echo $actual
directorio=$actual/'APS-'$1
echo $directorio
rm -r /var/is2
mkdir /var/is2
cp -r $directorio/aps /var/is2/
cp -r $directorio/templates /var/is2/
cp -r $directorio/static /var/is2/
mkdir /var/is2/media
./sincronizar.sh $2
if [ "$1" = "6.0" ]
then
	psql -U postgres -h localhost $2 < poblar.sql
fi
# descompimir django
# copiar t o d o   a / v ar / i s 2
# copiar aps.is2.conf a /etc/apache2/sites-available/
# editar archivo wsgi.py para agregarle el path
#a2enmod rewrite | a2ensite misitio.com
#service apache2 restart
