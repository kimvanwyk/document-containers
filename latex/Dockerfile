FROM ubuntu:16.04

LABEL name=kimvanwyk/latex
MAINTAINER kimvanwyk

RUN apt-get update && apt-get -y install \
   software-properties-common \
   wget \
&& add-apt-repository -y -u ppa:jonathonf/texlive \
&& apt-get -y install \
   texlive \
   xzdec \
&& add-apt-repository -r ppa:jonathonf/texlive \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /io
RUN chmod -R ugo+rwx /io

RUN adduser --disabled-password --gecos '' appuser
USER appuser

ADD setup.sh /tmp/setup.sh
RUN /tmp/setup.sh

VOLUME ["/io"]

ENTRYPOINT ["pdflatex"]   
CMD ["--version"]
