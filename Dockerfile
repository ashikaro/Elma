FROM python:alpine3.7

MAINTAINER Ashika Rohit "ashikaro@uw.edu"

# RUN apt-get update

# UPGRADE PIP AND INSTALL PACKAGES
COPY requirements.txt /usr/src/
WORKDIR /usr/src/
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt


# COPY PROJECT FILES
COPY ./ /usr/src

# COPY bash file
COPY bashrc /root/.bashrc

