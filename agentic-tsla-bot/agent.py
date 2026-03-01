import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
BASE_URL = "https://finnhub.io/api/v1"

class StockAgent:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch_quote(self):
        url = f"{BASE_URL}/quote"
        params = {
            "symbol": self.ticker,
            "token": FINNHUB_API_KEY
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_last_close_price(self):
        data = self.fetch_quote()
        # Finnhub field:
        # c = current price
        # pc = previous close
        return data.get("pc")

    def run(self):
        print(f"Running Agent for {self.ticker} at {datetime.now()}")
        price = self.get_last_close_price()
        print(f"Last Closing Price of {self.ticker}: ${price}")


if __name__ == "__main__":
    agent = StockAgent("TSLA")
    agent.run()