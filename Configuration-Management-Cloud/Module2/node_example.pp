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
