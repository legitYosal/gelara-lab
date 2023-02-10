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
ansible-playbook -i inventories/ini facts.yml
ansible-playbook -i inventories/ini deployment.yml --ask-vault-pass
```

cluster map:
```
```
