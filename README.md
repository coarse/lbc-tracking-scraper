# LBC Tracking Scraper

A web server that scrapes data from LBC Express tracking pages. Built with FastAPI, cloud-scraper, and lxml

## About

I built this scraper in order to create an API to be used for a discord bot. Eventually, I found out LBC has a public API with more data available so I didn't push through with setting it up for deployment. The scraper works 100% though I will be using their public API for the discord bot instead.

## Notes

- I initially used `httpx` library for fetching the tracking page, unforunately LBC uses Cloudflare for their site hence the need to use `cloud-scraper`.
