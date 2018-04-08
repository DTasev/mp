#!/bin/bash
curl -H "Travis-API-Version: 3" \
-H "Authorization: token vg3l6DLoLyBdoZb-vkdM6w" \
"https://api.travis-ci.com/repo/DTasev%2Fmp-fe/builds?limit=1&branch.name=master" | python3 ~/secret/crontab/check-build-status.py

if [ ! $? -eq 0 ]; then
    echo "The latest build did NOT pass. The repository was not deployed!"
else
    echo "The latest build PASSED. Deploying repository"
    source ~/pydawdle/bin/activate
    # Deploy front-end
    cd ~/tanks_server/tanks_frontend
    git checkout master
    # Pull the latest changes
    git pull
    # Install any new packages (if present)
    npm install
    # Builds the TS source to JS and bundles the built JS into a production distribution package
    npm run fullbuild:prod

    # Deploy Server
    cd ~/tanks_server
    git checkout master
    # Pull the latest changes
    git pull
    # Collect the front-end build
    python manage.py collectstatic --no-input
fi
