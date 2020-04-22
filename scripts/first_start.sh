#!/usr/bin/env bash

_c_path=$PWD
_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$(dirname "$_path")"

if [ ! -f .env ]; then
    cp .env.example .env
fi

docker-compose build
docker-compose up -d postgresql
docker-compose run project bash /scripts/init_project.sh

cd "$_c_path"
