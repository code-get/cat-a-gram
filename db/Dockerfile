# cat-a-gram model
# by: Christopher Landry
# date: 13-Oct-2017
#
# VERSION	0.0.1

# Start from a base Linux OS
FROM centos:latest

# Update latest patches
RUN yum update -y

# Install PostgreSQL
RUN yum install postgresql-libs -y
RUN yum install postgresql -y
RUN yum install postgresql-server -y
RUN yum install initscripts -y

COPY postgresqlstartup.sh /var/lib/pgsql/scripts/postgresqlstartup.sh
RUN chmod 755 /var/lib/pgsql/scripts/postgresqlstartup.sh
RUN chown -R postgres:postgres /var/lib/pgsql/scripts

# Switch to postgres user
USER postgres

# Copy and Run PostgreSQL Start-up Script on startup
RUN initdb -D /var/lib/pgsql/data
RUN echo "host all  all     0.0.0.0/0 md5" >> /var/lib/pgsql/data/pg_hba.conf
RUN echo "listen_addresses='*'" >> /var/lib/pgsql/data/postgresql.conf
RUN echo "source ~/scripts/postgresqlstartup.sh" >> ~/.bashrc

WORKDIR /var/lib/pgsql

# Open PostgreSQL Port
EXPOSE 5432

CMD ["/bin/bash"]
