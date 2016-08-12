from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def vagrant(port): 
    env.user = 'vagrant'
    # Give the port as an arugment -- this changes depending on the VM
    env.hosts = ['127.0.0.1:%s' % port]
    # use vagrant ssh key // via http://sysadminpy.com/sysadmin/2011/04/30/use-fabric-on-vagrant-instances/ updated to vagrant-ssh
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
