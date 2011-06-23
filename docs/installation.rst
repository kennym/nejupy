Installation
============

Setting up a development environment
------------------------------------

.. note::

   Virtualenv and virtualenvwrapper are highly recommended for setting up
   a development environment for Competition Manager.

Steps for setting a development environment:

* Get the source code::

  $ cd ~/projects
  $ git clone git@github.com:kennym/Competition-Manager.git

* If you have virtualenv and virtualenvwrapper installed::

  $ mkvirtualenv competitionmanager
  $ workon competitionmanager

* Create your localsettings.py::

  $ mv localsettings.py.dist localsettings.py

* Fill the `SECRET_KEY` with random stuff in that file.
* Install all requirements::

  $ cd competitionmanager
  $ pip install -r requirements.txt  # This can take a while

* Finish! You should now be able to run Competition Manager
