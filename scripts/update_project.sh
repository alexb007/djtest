#!/usr/bin/env bash

_c_path=$PWD
_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$(dirname "$_path")"

docker-compose stop project
docker-compose build
docker-compose up -d postgresql project nginx
docker-compose run project bash /scripts/prepare_project.sh

cd "$_c_path"

