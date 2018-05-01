[![Build Status](https://travis-ci.org/DTasev/dawdle-web.svg?branch=master)](https://travis-ci.org/DTasev/dawdle-web)

Production instructions below use `apt-get` and are for Debian-based distributions. The instructions require to have Python and NPM executables avaialble on the PATH. This will be done automatically, unless running on Windows, where additional configuration might be necessary to include them on the PATH.

**MINIMUM PYTHON VERSION: 3.5.2**. Versions below 3.5.2 have not tested and functionality is not guaranteed.

### If performing a clean install LOCALLY -- do steps 2, 3, 4, 5 and 6.

### If running the server from the Assignment Submission make sure you are:
- using a Python Virtual Environment (step 1)
- do steps 3, 4, 5 and 6

---

> Do step 1. Install necessary software ONLY for a PRODUCTION SERVER

1. Install necessary software
- NGINX

```bash
sudo apt-get nginx
```

- NPM - https://nodejs.org/en/download/package-manager/

```bash
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
```

- GUnicorn - preferred way is to create a virutal environment

```bash
pip install virtualenv
cd ~ && virtualenv -p python3 python_tanks
# activate the virtualenv
source activate ~/python_tanks/bin/activate
pip install gunicorn
```

> If installing locally start from here!

2. Clone the server and front-end repositories

```bash
git clone https://github.com/dtasev/mp-server tanks_server
cd tanks_server
# clone the front-end files inside the server directory
git clone https://github.com/dtasev/mp-fe tanks_frontend
```

3. Install server dependencies.
> If not using a virtual Python environment refer to step 1.
```bash
# inside tanks_server folder run this command to install all Python dependencies
pip install -r requirements.txt
```

4. Install front-end dependencies
```bash
cd tanks_frontend
# inside tanks_frontend folder run this command to install all NPM dependencies
npm install
```

5. Build front-end, run one of the commands
```bash
# inside tanks_frontend folder run this command for a production build
npm run fullbuild:prod
```
OR
```bash
# inside tanks_frontend folder run this command for a development build
npm run fullbuild:dev
```

---
> BELOW not necessary for local builds, only for production
6. Set up NGINX configuration
```bash
# go back to tanks_server folder
cd ../production_settings
# copy the file
sudo cp nginx/sites-available/tanks /etc/nginx/sites-available
# go to nginx's settings directory
cd /etc/nginx/sites-enabled
# create symlink to sites-enabled
sudo ln -s ../sites-available/tanks tanks
```
7. Set-up GUnicorn service
```bash
# go back to the tanks_server/production_settings folder
cd -
# copy the gunicorn service
sudo cp gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
# give read and execute permissions to everyone
sudo chmod +rx /etc/systemd/system/gunicorn.service
```

8. Start NGINX and Gunicorn
```bash
sudo service nginx start
sudo service gunicorn start
```

Single code block, for Ubuntu 16.04

```bash
sudo apt-get update
sudo apt-get install python-pip
pip install virtualenv
pip install --upgrade pip
virtualenv --help
cd ~ && virtualenv -p python3 pytanks
```