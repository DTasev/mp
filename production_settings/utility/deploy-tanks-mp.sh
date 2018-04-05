#!/bin/bash
curl -H "Travis-API-Version: 3" \
-H "Authorization: token vg3l6DLoLyBdoZb-vkdM6w" \
"https://api.travis-ci.com/repo/DTasev%2Fmp-fe/builds?limit=1&branch.name=master" | python3 ~/secret/crontab/check-build-status.py

if [ ! $? -eq 0 ]; then
    echo "The python build status script did not exit successfully. The repository was not deployed"
else
    cd ~/tanks
    git checkout master
    # Pull the latest changes
    git pull
    # Install any new packages (if present)
    npm install
    # Builds the TS source to JS and bundles the built JS into a production distribution package
    npm run fullbuild
fi

