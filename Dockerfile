FROM centos:centos8

RUN useradd -s /sbin/nologin www && \
    yum -y install httpd httpd-devel

ADD ./public_html /var/www/html

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
