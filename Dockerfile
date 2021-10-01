FROM centos:centos8

RUN useradd -s /sbin/nologin www

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
