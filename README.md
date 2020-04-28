[![Build Status](https://travis-ci.org/colin-nolan/ansible-shinobi.svg?branch=master)](https://travis-ci.org/colin-nolan/ansible-shinobi)
# Ansible Shinobi
_Ansible role for installing and Ansible modules for controlling [Shinobi](https://gitlab.com/Shinobi-Systems/Shinobi)
(an open-source video management solution)._

## About
This repository contains an [Ansible](https://github.com/ansible/ansible) role that installs and configures a [Shinobi
installation, which runs inside Docker](https://github.com/colin-nolan/docker-shinobi/).


## Requirements
- Debian/Ubuntu (un-tested for other distributions).
- x86 or armv7 architectures (i.e. works on Raspberry Pi!).
- Docker on the host machine.


## Usage
### Role
#### Installation
TODO: make this work!
```bash
ansible-galaxy role install git+https://github.com/colin-nolan/python-shinobi-client.git,master
```

#### Configuration
For configuration options, please [see the defaults file](defaults/main.yml). Note that there are a number of
configuration values that must be provided (detailed provided at the top of the defaults file, linked above).

Important notes:
- The default Shinobi installation (non-community edition) is not free for use in all situations - see `shinobi_source`.
- The default Shinobi Docker base image has a build of `ffmpeg` (the software that deals with video) that is will not be
  optimised for your host - see `shinobi_docker_shinobi_base_image`.

#### Example:
```yaml
# playbook.yml

- hosts: shinobi-servers
  roles:
     - colin-nolan.shinboi
  vars:
    shinobi_database_root_password: password123
    shinobi_database_user_name: user123
    shinobi_database_user_password: password123

    shinobi_super_user_email: admin@localhost
    shinobi_super_user_password: password123
    shinobi_super_user_token: token123

    shinobi_users:
      - email: user@localhost
        password: password123

    shinobi_host_address: 0.0.0.0
    shinobi_host_port: 8080

    shinobi_source:
      repository: https://gitlab.com/Shinobi-Systems/Shinobi.git
      version: master

    shinobi_docker_shinobi_base_image: colinnolan/ffmpeg:latest
```

### Modules
There are 2 Ansible modules in this project that you may wish to use (without necessarily using the role - put them into
your library):
- [`shinobi_user`](library/shinobi_user.py): manages users.
- [`shinobi_monitor`](library/shinobi_monitor.py): manages monitors (user camera setups).


## Development
### Requirements
- Python >= 3.6 with pip for testing.

### Testing
Testing has been setup with molecule. To install:
```bash
pip install -r molecule/default/requirements.txt
```
To run all tests:
```
module test [--destory=never]
```


## Related Projects
- [Dockerised Shinobi setup](https://github.com/colin-nolan/docker-shinobi).
- [Shinobi Pythion client](https://github.com/colin-nolan/python-shinobi).


## Alternatives
- [Official Ansible role](https://gitlab.com/Shinobi-Systems/ansible-shinobi) - not containerised, a little unpolished.


## Legal
[GPL v3.0](LICENSE.txt). Copyright 2020 Colin Nolan.

I am not affiliated to the development of Shinobi project in any way. This work is in no way related to the company that
I work for.
