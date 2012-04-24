gateman
=======
в etc/services/   дописать   path_to_simple_server.py port/tcp

sudo cp ./testx /etc/xinetd.d
sudo service xinetd reload
sudo service xinetd restart
