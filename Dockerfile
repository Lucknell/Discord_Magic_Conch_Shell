FROM ubuntu:latest
MAINTAINER lucknell <lucknell3@gmail.com>                                              
RUN mkdir -p /src/bot/
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /src/bot                                                                
COPY . /src/bot   
RUN pip3 install -U discord.py
CMD ["python3","-u", "conch.py"]