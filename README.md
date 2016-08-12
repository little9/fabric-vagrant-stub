# fabric-vagrant-stub
A basic Fabric module that lets you connect to a local Vagrant instance

# Usage

Put the fabfile in your Vagrant folder and use the vagrant function with the 
forwarded port as an arugment before your other commands:

```bash
fab vagrant:2222 
```
