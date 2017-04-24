FROM python:3-onbuild
MAINTAINER drew verlee "drew.verlee@gmail.com"
ENV PYTHONPATH $PYTHONPATH:/usr/src/app

ADD ["https://storage.googleapis.com/kubernetes-release/release/v1.6.1/bin/linux/amd64/kubectl", "/usr/local/bin/kubectl"]
# 555 is everyone can read and execute
RUN ["chmod", "555", "/usr/local/bin/kubectl"]

