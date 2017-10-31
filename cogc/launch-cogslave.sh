#! /bin/bash -x

serial=$1
sudo docker run --rm -it -v /home/ubuntu:/root --name cog_contain${serial} tbutzer/cogc
