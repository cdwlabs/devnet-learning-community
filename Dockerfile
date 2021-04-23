FROM registry.access.redhat.com/ubi8/ubi:8.3

RUN dnf module install -y python38 && \
    dnf install -y httpd

COPY . /training

CMD [ "/usr/bin/bash" ]