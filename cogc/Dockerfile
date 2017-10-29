FROM ubuntu:16.04
MAINTAINER Tony Butzer
ENV REFRESHED_AT 2017-10-02

RUN apt-get -yqq update && \
   apt-get install -y python3 python3-dev python3-pip && \
   pip3 install rq

CMD ["bash"]

