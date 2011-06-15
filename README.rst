===================
Competition Manager
===================

--------
Overview 
--------

::

   |-apps               # All the custom apps go in the apps directory 
   |---sample_app       # A sample django app
   |-docs               # Any documentation, preferrable in managed with Sphinx
   |-media              # All media files
   |---css              # Project wide css file, css not specific to any app
   |-----sample_app     # Any css files specific to sample_app
   |---img              # Project wide images, images not specific to any app
   |-----sample_app     # Images specific to sample_app
   |---js               # Project wide JavaScript files, or JavaScript not specific to any app
   |-----sample_app     # JavaScript specific to sample_app
   |-templates          # Temlates
   |---sample_app       # Temlates specific to sample_app
   |-vendors            # Any third party app not installable from pip or modified to fit project needs


---------------
Getting started
---------------

1. Create a virtualenv environment
2. Switch to the environment
3. Run::

   pip install -r requirements.txt

4. Enjoy
