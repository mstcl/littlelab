#! /bin/sh

BOT_TOKEN="{{ bot_token }}"
CHAT_ID="{{ chat_id }}"
FILENAME=$(echo $1 | tr " " +)
MESSAGE="<b>🎉+TORRENT+DOWNLOAD+COMPLETED</b>%0A${FILENAME}"

PAYLOAD="https://api.telegram.org/bot${BOT_TOKEN}/sendMessage?chat_id=${CHAT_ID}&text=${MESSAGE}&parse_mode=HTML"

curl -s -X POST "${PAYLOAD}"
