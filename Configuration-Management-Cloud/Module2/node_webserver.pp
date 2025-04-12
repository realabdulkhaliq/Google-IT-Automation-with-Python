sudo puppet config --section master set autosign true
ssh webserver
sudo apt install puppet

sudo puppet config set server ubuntu.example.com
sudo puppet agent -v --test
