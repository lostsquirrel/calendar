FROM python:3.10-bookworm

ADD venv /
RUN useradd -s /sbin/nologin word

COPY app /usr/src
WORKDIR /usr/src/
USER word
EXPOSE 8000
CMD ["/venv/bin/python", "server.py"]