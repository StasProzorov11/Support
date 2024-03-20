import random
import string
import time
from typing import Callable

import httpx
from django.http import HttpRequest, JsonResponse
from django.urls import path

create_random_string: Callable[[int], str] = lambda size: "".join(# NOQA
    [random.choice(string.ascii_letters) for _ in range(size)]
)

cached_exchange_rate = ""
last_cached_time = 0


async def get_exchange_rate(request: HttpRequest) -> JsonResponse:
    global cached_exchange_rate
    global last_cached_time

    current_time = time.time()
    if current_time - last_cached_time < 10:
        return JsonResponse({"rate": cached_exchange_rate})

    source_currency = request.POST.get("source_currency")
    destination_currency = request.POST.get("destination_currency")

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source_currency}&to_currency={destination_currency}&apikey=V2V43QAQ8RILGBOW"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    rate = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    cached_exchange_rate = rate
    last_cached_time = current_time

    return JsonResponse({"rate": rate})


urlpatterns = [
    path(route="exchange-rate", view=get_exchange_rate),
]
