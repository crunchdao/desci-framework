FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt -y install pandoc pandoc-citeproc texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

WORKDIR /paper
ENTRYPOINT ["pandoc"]
