# Module 2

## Deploying Puppet Locally

[Applying Rules Locally](https://www.coursera.org/learn/configuration-management-cloud/item/Lpu3d)

[Organizing your Puppet modules](https://www.coursera.org/learn/configuration-management-cloud/lecture/0dYuQ/organizing-your-puppet-modules)

https://puppet.com/docs/puppet/latest/style_guide.html

https://puppet.com/docs/puppetserver/latest/install_from_packages.html

[Setting up Puppet clients and servers](https://www.coursera.org/learn/configuration-management-cloud/lecture/tOqXw/setting-up-puppet-clients-and-servers)

http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/

[Modifying and testing manifests](https://www.coursera.org/learn/configuration-management-cloud/lecture/KZPEP/modifying-and-testing-manifests)

```
describe 'gksu', :type => :class do
  let (:facts) { { 'is_virtual' => 'false' } }
  it { should contain_package('gksu').with_ensure('latest') }
end
```

This code runs an rspec test to determine whether the gksu package has the intended behavior when the fact is_virtual is set to false. When this is the case, the gksu package should have the ensure parameter set to latest: ensure('latest').

https://rspec-puppet.com/tutorial/

http://puppet-lint.com/
