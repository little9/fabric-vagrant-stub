from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def vagrant(port):
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:%s' % port]
    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
