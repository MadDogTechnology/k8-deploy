This app deploys services to kubernetes

SETUP
-------
* Install docker

How to deploy services?
---------------------
This directory shares a volume with the docker container, so you can develop locally without having to update the image.
So running deploying is as easy as running: 

$ ./run 

Development
-----------
make changes then run ./build to build a new image that contains them.


TODOS
-------------
* Move the todos to jira.
* Probably shouldn't use FROM onbuild in the docker file. see (docs)[https://hub.docker.com/_/python/]
  Instead we should build our own image and freeze the version of kubectl and upgrade it alongside our kubernetes cluster
* Add Logging to datadog
* capture output and display it on command line

#DEBUG
-----------

you have all the standard methods of python to debug. 
The debug script is the run script with a interactive terminal so you can drop a `import pdb;pdb.set_trace()` in your code to debug.
