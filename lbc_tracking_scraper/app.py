from typing import Annotated

import cloudscraper
from fastapi import FastAPI, Path, Query
from lxml import html

from .utils import get_tracking_url

app = FastAPI()

scraper = cloudscraper.create_scraper()


@app.get("/{tracking_number}")
async def get_tracking_data(
    tracking_number: Annotated[
        str, Path(title="LBC Express tracking number", pattern="^\\d{14}$")
    ],
    latest_only: Annotated[bool | None, Query(alias="track-latest-only")] = None,
):
    tracking_page_url = get_tracking_url(tracking_number)
    response = scraper.get(tracking_page_url)

    tree = html.fromstring(response.content)

    tracking_data = []

    entries = tree.xpath('//div[@class="desktop-tracking-tt"]')
    for entry in entries:
        timestamp = entry.xpath('.//span[@class="date-track-a"]/text()')[0]
        message = entry.xpath(
            './/div[@class="track-side-2"]/span[@class="status-tracking"]/text()'
        )[0]
        tracking_data.append({"message": message, "timestamp": timestamp})

        if latest_only:
            break

    return {"data": tracking_data}
