## Installation

To set up the project, follow these steps:

1. Create a virtual environment:

   ```
   python -m venv venv
   ```

2. Activate the virtual environment:

   On Windows:

   ```
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```
   source venv/bin/activate
   ```

## Proxy Usage

This scraper uses a list of proxies to rotate requests. The proxies are:

- 196.51.200.84:8800
- 196.51.202.192:8800
- 196.51.200.234:8800
- 196.51.202.134:8800
- 196.51.202.138:8800

The scraper will randomly choose one of these proxies for each request. If a request fails, it will be retried up to 10 times with different proxies.

To modify the proxy list, edit the `PROXY_LIST` setting in `trip_scraper/settings.py`.
