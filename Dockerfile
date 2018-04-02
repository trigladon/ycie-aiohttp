FROM ubuntu:16.04

# install python 3.6
RUN apt-get update && apt-get install -y wget gcc make zlib1g-dev libssl-dev && wget -P /tmp https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz && tar -xvzf /tmp/Python-3.6.3.tgz -C /tmp && /tmp/Python-3.6.3/configure && make altinstall && rm -r /tmp/Python-3.6.3 && rm /tmp/Python-3.6.3.tgz && mkdir -p /home/projects/ycie-aiohttp
ADD requirements.txt /home/projects/ycie-aiohttp/requirements.txt
RUN pip3.6 install -r /home/projects/ycie-aiohttp/requirements.txt

EXPOSE 8080