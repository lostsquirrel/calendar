FROM python:3.10-bookworm

COPY venv /venv
RUN useradd -s /sbin/nologin word
RUN pip install gevent

COPY app /usr/src
WORKDIR /usr/src/
USER word
EXPOSE 8000
CMD ["/venv/bin/python", "server.py"]