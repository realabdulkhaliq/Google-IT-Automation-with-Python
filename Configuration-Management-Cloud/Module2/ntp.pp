class ntp {
  package { 'ntp':
    ensure => latest,
  } 
  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/etc/ntp.conf'],
    # We use lowercase for the original resource, and capitalize the resource name when referencing a relationship.
  }
}

include ntp

# To Run: sudo puppet apply -v ntp.pp