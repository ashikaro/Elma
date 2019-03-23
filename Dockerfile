FROM python:alpine3.7

MAINTAINER Ashika Rohit "ashikaro@uw.edu"

# UPGRADE PIP AND INSTALL PACKAGES

RUN pip3 install --upgrade pip && \
    apk update && \
    apk add bash && \
    apk add doxygen && \
    apk add bash


# COPY PROJECT FILES
COPY ./ /usr/src

# COPY bash file
COPY bashrc /root/.bashrc

