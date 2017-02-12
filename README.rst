===============================
MRR Website
===============================

Mini Robot Rumble Website


Quickstart
----------

Before running shell commands, set the ``FLASK_APP``, ``FLASK_DEBUG`` and ``MRR_WEBSITE_SECRET``
environment variables ::

    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1
    export mrr_website_SECRET=mysecret

Clone the repository
::
      git clone https://github.com/AucklandRobotics/mrr-website

Setup a virtual environment ::

      pip3 install virtualenv
      virtualenv env
      pip install -r requirements/dev.txt
      bower install
      flask run

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    flask run


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test

Deploying to Heroku
-------------

Deploys to Heroku are automated through travis ci. Three environment variables are required in your travis ci configuration to deploy:

$STAGING_APP - The app name in Heroku 
$DOCKER_USERNAME - Your Heroku username (email address)
$DOCKER_PASSWORD - Your Heroku API key, accessable in https://dashboard.heroku.com/account

The application is packaged as a docker image and is pushed to Herkou's docker repository. See .travis/after_success.sh


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
