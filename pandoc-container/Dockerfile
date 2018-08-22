FROM kimvanwyk/latex:1.0.0

LABEL name=kimvanwyk/pandoc
MAINTAINER kimvanwyk

USER root
RUN apt-get update && apt-get -y install \
   pandoc \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

USER appuser
ENTRYPOINT ["pandoc"]   
CMD ["--help"]
