#!/bin/bash

jsonmsg="{}"

merge() {
    jsonmsg="$(jq -c -n "$jsonmsg + $1")"
}

for line in $(env | grep APP_); do
  x="${line#APP_}"
  key="${x%%=*}"
  val="${x#*=}"

  echo "{$key: $val}"
  merge "{$key: \"$val\"}"
done

mkdir -p /var/www/config

echo "$jsonmsg" | jq . > /var/www/config/config.json