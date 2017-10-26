#! /bin/sh
systemVersion=`cat /etc/issue | awk '{print $1}'`
[ `whoami` == 'root' ] || echo '[*] plase run as root' && exit 0
[ `mysql -V | awk '{print $1}'` == 'mysql' ] || echo '[-] you have not install mysql,would you wanna install? [y/n]' && read arg
echo "[*] please set root user password for mysql" && read rootPasswd

if [ arg == 'y' ]
then
	`apt-get install mysql-server mysql-common mysql-cilent`
	echo $rootPasswd
fi
#use mysql
`service mysql start`
`mysql -uroot -p $rootPasswd -e "create database pts1;
create user pts1 identified by 'pts1';
grant all privileges to pts1@localhost for pts1 identified by 'pts1';
#build modules info table
create table modules();
###import all modules to database"`
`service mysql restart`

`mv ./pts.conf /etc/` || echo '[-] permision deny'
`mkdir /usr/share/pentoolset-framework` || echo "[-] can't create main derictory"
`mv -R ./modules /usr/share/pentoolset-framework` || echo "[-] can't move modules to main derictory"
`mkdir /usr/lib/pentoolset-framework` || echo "[-] can't create derictory"
`mv -R ./* /usr/lib/pentoolset-framework` || echo "[-] can't move file to /usr/lib"
if [ -e /usr/lib/pentoolset-framework/pentoolset.py ]
then
	`ln -s /usr/lib/pentoolset-framework/pentoolset.py /usr/bin/pts` || echo "[-] can't create link file"
fi


#
#
#create .desktop file
#
#
