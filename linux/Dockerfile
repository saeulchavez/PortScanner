
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    iproute2 \
    iputils-ping \
    traceroute \
    dnsutils \
    tcpdump \
    tshark \
    net-tools \
    curl \
    wget \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /lab

COPY check_port.sh /lab/check_port.sh

RUN chmod +x /lab/check_port.sh

ENTRYPOINT ["/bin/bash", "/lab/check_port.sh"]
