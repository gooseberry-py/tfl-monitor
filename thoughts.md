Some thoughts for improvements, rather than adding these to a pull request:

## Use async requests

Some of the requests could be run asynchronously rather than all together, particularly where loops are involved:

```python
import httpx

# create the async client
client = httpx.AsyncClient(
    headers={"Accept": "application/json"},
    base_url="https://api.tfl.gov.uk/",
)
lines = ["northern", "victoria"]

# asynchronously run all requests at once
reqs = await gather(*[
        client.get(f"Line/{line}/Status")
        for line in lines
    ])
```



## Overground trains:

An overground trains API: https://www.realtimetrains.co.uk/about/developer/

Train station codes to use for this: http://www.railwaycodes.org.uk/crs/crsp.shtm


## Front end:

For running the web client locally, you could consider FastAPI: https://fastapi.tiangolo.com/


## Other changes:
- Removing the specific locations/routes to a separate file so that these can be substituted easily for different uses
- Renaming Borris to Boris
