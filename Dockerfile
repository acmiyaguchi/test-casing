FROM centos:7
LABEL maintainer="amiyaguchi@mozilla.com"

ENV LANG en_US.utf8

RUN curl https://bintray.com/sbt/rpm/rpm \
    | tee /etc/yum.repos.d/bintray-sbt-rpm.repo

RUN yum install -y epel-release \
        && yum install -y \
                java-1.8.0-openjdk \
                cargo \
                sbt \
                python36 \
        && yum clean all \
        && rm -rf /var/cache/yum

ENV PATH="$PATH:~/.local/bin"
RUN python3 -m ensurepip

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN cargo build
RUN sbt compile
