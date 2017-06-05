#!/usr/bin/env bash

TMP=news.tmp
OUTPUT=news.json

rm -rf $OUTPUT

function fetch_json {
    curl --silent $1 | jq '.items[] | {title, date:.pubDate, link:.guid|capture("cluster=(?<a>[a-zA-Z0-9.:/\\-_]+)")|.a, summary:.description}' >> $TMP
}

fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%26output%3Drss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%26output%3Drss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E5%A4%A7%E6%95%B0%E6%8D%AE%26output%3Drss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%26output%3Drss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%26output%3Drss
fetch_json https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Fnews%2Fsection%3Fcf%3Dall%26ned%3Dus%26hl%3Den%26q%3D%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6%26output%3Drss

cat $TMP | jq --slurp '.|sort_by(.date)|reverse' > $OUTPUT