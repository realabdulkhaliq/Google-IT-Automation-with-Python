node default {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
} /

The command node default installs the sudo and ntp classes on all default nodes. The sudo class is installed with its default parameters, because no parameters are specified. The ntp class is installed with an additional parameter, indicated by servers => ['ntp1.example.com', 'ntp2.example.com'].


node webserver.example.com {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
  class { 'apache': }
}

The command node webserver.example.com installs the sudo, ntp, 
and apache classes on nodes with the fully-qualified domain name 
(FQDN) webserver.example.com.
Note: Because nodes with this FQDN have a specific set of classes 
that apply to them, the node default command will not apply any 
classes to them. 