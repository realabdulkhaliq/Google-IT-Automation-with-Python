sudo puppet config --section master set autosign true
ssh webserver
sudo apt install puppet

sudo puppet config set server ubuntu.example.com
sudo puppet agent -v --test



vim /etc/puppet/code/environments/production/manifests/site.pp


node webserver {
  class { 'apache': }
}

node default {}


sudo systemctl enable puppet
sudo systemctl start puppet
sudo systemctl status puppet