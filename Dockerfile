FROM ubuntu
MAINTAINER Simen Andresen <simena86@gmail.com>

# Setup application
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y python-mysqldb
COPY db.py /db.py

#RUN python /db.py
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server
#RUN service mysql start
CMD ["python", "/db.py" ] 
