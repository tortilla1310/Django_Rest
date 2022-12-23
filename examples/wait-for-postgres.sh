#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
# shellcheck disable=SC2124
cmd="$@"

until PGPASSWORD="dante123456" psql -h "$host" -d "library" -U "dante" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
# shellcheck disable=SC2086
exec $cmd
