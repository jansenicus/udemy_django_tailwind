# TLDR;
```bash
# ENVIRONMENT
## install python 3.9.18
pyenv install 3.9.18

## create virtual environment
python -m venv .env

## install python packages

pip install --upgrade pip
pip instal -r requirements.txt

## powershell
pwsh

## Activate environment
./.env/bin/Activate.ps1

## cd src
cd src

## python manage django
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```

# Longer Explanation
## Python Environment
### Python version installation
```bash
pyenv install 3.9.18
```

### Python virtual environment
```bash
python -m venv .env
```

### Python packages installation
```bash
pip install --upgrade pip
pip instal -r requirements.txt
```
## Powershell Environment
### Enter Powershell Environment
```bash
pwsh
```

### Activate Powershell environment
```bash
./.env/bin/Activate.ps1
```
## change directory to `src`
```bash
cd src
```


## Django Environment
### create super user
```bash
python manage.py createsuperuser
```
### migrate all data
```bash
python manage.py migrate
```
### run Django server
```bash
python manage.py runserver
```