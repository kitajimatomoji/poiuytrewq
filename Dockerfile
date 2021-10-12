FROM centos:7

# RUN yum update -y && yum clean all
RUN yum install -y httpd

ADD var_www /var/www

EXPOSE 80
EXPOSE 8080

ENTRYPOINT ["/usr/sbin/httpd", "-DFOREGROUND"]
