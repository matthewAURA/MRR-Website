#!/bin/sh

set -e

if [ $TRAVIS_PULL_REQUEST != "false" -o $TRAVIS_BRANCH != "master" ]
then
    echo "Skipping deployment on branch=$TRAVIS_BRANCH, PR=$TRAVIS_PULL_REQUEST"
    exit 0;
fi

docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD" registry.heroku.com
docker push registry.heroku.com/$STAGING_APP/web
