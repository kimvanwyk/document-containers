FROM kimvanwyk/latex:1.0.0

LABEL name=kimvanwyk/pandoc
MAINTAINER kimvanwyk

RUN apt-get update && apt-get -y install \
   pandoc \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["pandoc"]   
CMD ["--help"]
