FROM python:3.10-bookworm

COPY venv /venv
RUN useradd -s /sbin/nologin word
RUN pip3 install gevent
ENV PATH="/venv/bin:$PATH"
ENV PYTHONUSERBASE=/venv
COPY app /usr/src
WORKDIR /usr/src/
USER word
EXPOSE 8000
CMD ["python", "server.py"]