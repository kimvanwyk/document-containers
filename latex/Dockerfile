FROM ubuntu:16.04

LABEL name=kimvanwyk/latex
MAINTAINER kimvanwyk

RUN apt-get update && apt-get -y install \
   software-properties-common \
   python3.6 \
   wget \
   perl \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

RUN wget http://leg.uct.ac.za/pub/packages/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz \
&& tar xf install-tl-unx.tar.gz \
&& rm install-tl-unx.tar.gz \
&& mv `echo /install-tl-*` /install-tl 

ADD texlive.profile /install-tl/texlive.profile

RUN cd /install-tl \
&& ./install-tl --profile=texlive.profile -repository http://leg.uct.ac.za/pub/packages/ctan/systems/texlive/tlnet/ \
&& cd ../

ENV PATH="/usr/local/texlive/2019/bin/x86_64-linux:${PATH}"
ADD setup.sh /tmp/setup.sh
RUN /tmp/setup.sh

WORKDIR /io
RUN chmod -R ugo+rwx /io

RUN adduser --disabled-password --gecos '' appuser
USER appuser

VOLUME ["/io"]

ENTRYPOINT ["pdflatex"]   
CMD ["--version"]
