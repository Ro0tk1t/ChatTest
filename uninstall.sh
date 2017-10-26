#! /bin/sh
[ `whoami` == 'root' ] || echo "please run as root"&& exit 0

`rm -vf /etc/pts.conf`
`rm -Rvf /usr/share/pentoolset-framework`
`rm -Rvf /usr/lib/pentoolset-framework`
`rm -Rvf /usr/bin/pts`

echo "uninstall done !"
