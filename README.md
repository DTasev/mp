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
sudo apt-get install nginx
```

- NPM - https://nodejs.org/en/download/package-manager/

```bash
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
```

- GUnicorn - preferred way is to create a virutal environment

```bash
sudo apt install python-pip
pip install virtualenv
cd ~ && virtualenv -p python3 python_tanks
# activate the virtualenv
source ~/python_tanks/bin/activate
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
> below ONLY necessary for production. For LOCAL builds, go to last step
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
cd ~ && virtualenv -p python3 python_tanks
```

### Running the Django server

> Make sure you are in the tanks_server directory! If following these instructions it will be at ~/tanks_server
> Make sure you have the Python Tanks Virtual environment activated. Command is: `source ~/python_tanks/bin/activate`

1. Applying the database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Run the Django server
```bash
# if python tanks virtual environment not active do
# source ~/python_tanks/bin/activate

python manage.py runserver
```

3. Go to http://localhost:8000

# Troubleshooting Django errors

> Invalid HTTP_HOST header: '<CURRENT_URL>'. You may need to add '<CURRENT_URL>' to ALLOWED_HOSTS.

This may happen if Django is not configured to allow the current domain used to access the server. To fix this either:

- Go to http://localhost:8000
- Add the URL you used in Tanks/settings.py. The variable that has to be changed is ALLOWED_HOSTS

# After submission
The automatic deployment will be stopped on the day of the submission deadline. The repositories of the project will be archived (made read-only) and public. Any future work on the project will continue in a fork.

I guarantee that the Tanks game project will be kept accessible online at least until the marks for the Major Project module are released. 

Access to the production server is not be provided in the submission, but may be explicitly requested by the markers of the submission. To request access to the production server please email me at dbt@aber.ac.uk.

# Public Address
The public address for the Tanks game is: https://dtasev.me/tanks

