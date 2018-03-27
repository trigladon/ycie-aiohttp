FROM ubuntu:16.04

# install python 3.6
# docker run -d -v /mnt/python/ycie-data:/home/projects/ycie-data -p 8080:8080 -i -t e534fa9a27b9
RUN apt-get update && apt-get install -y wget gcc make zlib1g-dev libssl-dev && wget -P /tmp https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz && tar -xvzf /tmp/Python-3.6.3.tgz -C /tmp && /tmp/Python-3.6.3/configure && make altinstall && rm -r /tmp/Python-3.6.3 && rm /tmp/Python-3.6.3.tgz && mkdir -p /home/projects/credit-fair-e
ADD requirements.txt /home/projects/credit-fair-e/requirements.txt
RUN pip3.6 install -r /home/projects/credit-fair-e/requirements.txt

EXPOSE 8080