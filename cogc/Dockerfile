FROM ubuntu:16.04
MAINTAINER Tony Butzer
ENV REFRESHED_AT 2017-10-01

RUN apt-get -yqq update && \
   apt-get install -y python python-dev python-pip python-virtualenv  && \
   pip install rq


CMD ["bash"]

