#! /bin/sh
systemVersion=`cat /etc/issue | awk '{print $1}'`
[ `whoami` == 'root' ] || echo '[*] plase run as root' && exit 0
[ `mysql -V | awk '{print $1}'` == 'mysql' ] || echo '[-] you have not install mysql,would you wan to install,[y/n]' && read arg

if [ arg == 'y' ]
do
	`apt-get install mysql-server mysql-common mysql-cilent`
done

`mv ./pts.conf /etc/` || echo '[-] permision deny'
`mkdir /usr/bin/share/pentoolset-framework` || echo "[-] can't create main derictory"
`mv -R ./modules /usr/share/pentoolset-framework` || echo "[-] can't move modules to main derictory"

#
#
#create .desktop file
#
#
