Instructions below use `apt-get` and are for Debian-based distributions.

> Do step 1. Install necessary software ONLY for a PRODUCTION SERVER

1. Install necessary software
- NGINX

```bash
sudo apt-get nginx
```

- NPM - https://nodejs.org/en/download/package-manager/

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
# clone inside server directory
git clone https://github.com/dtasev/mp-fe tanks_frontend
```

3. Install server dependencies
```bash
# inside tanks_server folder
pip install -r requirements.txt
```

4. Install front-end dependencies
```bash
cd tanks_frontend
# inside tanks_frontend folder
npm install
```

5. Build front-end
```bash
# inside tanks_frontend folder
npm run fullbuild
```
6. Set up NGINX configuration
```bash
# go back to tanks_server folder
cd ../production_settings
# copy the file
sudo cp sites-available/tanks /etc/nginx/sites-available
# go to nginx's settings directory
cd /etc/nginx/sites-available
# create symlink to sites-enabled
sudo ln -s tanks ../sites-enabled
```
7. Set-up GUnicorn service
```bash
# go back to the tanks_server/production_settings folder
cd -
# copy the gunicorn service
sudo cp gunicorn.service /etc/systemd/system/gunicorn.service
```

8. Collect static files for Django to serve
```bash
python manage.py collectstatic
```

9. Start NGINX and Gunicorn
```bash
sudo service nginx start
sudo service gunicorn start
```