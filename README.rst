Deal App
========

Application for analyzing real estate deals and monitoring portfolio performance.



Settings
--------

The settings module for the project is located at /config/settings/base.

The project relies heavily on environment variables for configuration.

This include a minimum:

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DATABASE_URL=
CELERY_BROKER_URL=
SEKRETKEY=



Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go. At this stage

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy deal_app

Test coverage
^^^^^^^^^^^^^
Unit tests are inplace for account features and authorization.


To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd deal_app
    celery -A config.celery_app worker -l info






Email Server
^^^^^^^^^^^^

The project uses AllAuth for authentication so it require it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`_ when generating the project a local SMTP server with a web interface will be available.

#. `Download the latest MailHog release`_ for your OS.

#. Rename the build to ``MailHog``.

#. Copy the file to the project root.

#. Make it executable: ::

    $ chmod +x MailHog

#. Spin up another terminal window and start it there: ::

    ./MailHog

#. Check out `<http://127.0.0.1:8025/>`_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

.. _`Download the latest MailHog release`: https://github.com/mailhog/MailHog/releases

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.




