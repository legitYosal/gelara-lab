# Configuration

## Setup project

Install requirements and ansible on ubuntu controller:
```bash
sudo apt install python3-venv
git clone git@github.com:legitYosal/gelara-lab.git
cd elara-lab
git submodule update --init --recursive
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Infra

Bootstrap cluster:  
```
ansible-playbook -i inventories/hosts.ini facts.yml
ansible-playbook -i inventories/hosts.ini deployment.yml --ask-vault-pass
```

cluster map:
```
```

# MariaDB
MariaDB have two storage backends named InnoDB and MyISAM, These two differ on their locking implementation: InnoDB locks the particular row in the table, and MyISAM locks the entire MySQL table. [source](https://stackoverflow.com/a/5414622/12131234)
