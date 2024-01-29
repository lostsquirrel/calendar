FROM python:3.10-bookworm

COPY venv /usr/src/
RUN useradd -s /sbin/nologin word

COPY app /usr/src
WORKDIR /usr/src/
USER word
EXPOSE 8000
CMD ["/usr/src/venv/bin/python", "server.py"]