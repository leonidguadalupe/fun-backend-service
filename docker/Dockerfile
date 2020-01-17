FROM python:3.8-alpine

ADD . /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
    # install what's needed
    alpine-sdk ca-certificates openssl-dev linux-headers\
    libffi-dev jpeg-dev zlib-dev \
    # create groups and users
    && addgroup -S _uwsgi && adduser _uwsgi -G _uwsgi -D \
    # install poetry
    && python3 -m pip install uwsgi poetry --no-cache-dir \
    # configure and create virtualenv with poetry
    && poetry config settings.virtualenvs.create false \
    # remove pip wheel metadata and .venv
    && rm -rf /app/lib/*/pip-wheel-metadata .venv \
    # run make
    && make \
    # remove configuration files to make image smalleer
    && apk --purge del .build-deps \
    # find __pycache__ folders and remove them
    && find / -type d -name __pycache__ -exec rm -r {} + \
    # remove other cached items as well from these directories
    && rm -rf /root/.cache /var/cache

USER _uwsgi

ENTRYPOINT ["uwsgi", \
    "--master", \
    "--die-on-term", \
    "--plugin", "python3"]

# point to port 8080 inside container
CMD ["--http-socket", "0.0.0.0:8080", \
    "--processes", "1", \
    "--chdir", "/app", \
    "--py-auto-reload", "1", \
    "--module", "3mw_backend_service.app.wsgi:application"]