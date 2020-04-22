FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
           build-essential \
           gettext \
           binutils \
           libproj-dev \
           gdal-bin \
           netcat \
           libgettextpo-dev \
    && pip install --upgrade pip

WORKDIR /apps/djtest
COPY ./requirements/ requirements/
COPY ./scripts/docker/ /scripts/
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD uwsgi --plugins=python3 --socket :8000 --processes 4 --threads 2 --master --uid=uwsgi --gid=uwsgi --module djtest.wsgi
