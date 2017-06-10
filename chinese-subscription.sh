#!/usr/bin/env bash
set -e

TMP=chinese-subscription.tmp
OUTPUT=chinese-subscription.json

rm -rf ${OUTPUT}
rm -rf ${TMP}

#function fetch_json2 {
#    curl --silent $1 | jq '.items[] | {title, date:.pubDate, link:.guid, summary:.description}' >> ${TMP}
#}

function fetch_json {
    curl --silent $1 | jq '{ feed_name: .feed.title, content: .items[0,1] | {title: .title, date:.pubDate, link:.guid, summary:.description }}' >> ${TMP}
}

fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.jiqizhixin.com%2Frss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fdataunion.org%2Ffeed
fetch_json https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2F36kr.com%2Ffeed

cat ${TMP} | jq --slurp '.|unique_by(.content.date)|sort_by(.content.date)|reverse' > ${OUTPUT}

