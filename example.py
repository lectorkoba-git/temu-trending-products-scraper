"""
Example: trending Temu products (lightning deals, 5-star, local warehouse, homepage) via the Apify Python client.
Requires: pip install apify-client   and   APIFY_TOKEN in the environment.
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "sources": ["lightning_deals", "five_star", "local_warehouse", "homepage"],
    "maxResults": 100,
    "minSold": 1000,
    "minRating": 4.5,
    "excludeAds": False,
}

print("Running magic-scraper/temu-trending-products-scraper on Apify...")
run = client.actor("magic-scraper/temu-trending-products-scraper").call(run_input=run_input)
print(f"Run finished: {run['status']}\n")

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    rank = f"{item['rankingType']} #{item['rankingNumber']} in {item['rankingCategory']}" if item.get("rankingType") else "-"
    print(item["title"][:80])
    print(f"  Price: {item['price']} {item['currency']} (market {item.get('originalPrice')}) | discount: {item.get('discountPercentage')}%")
    print(f"  Sold:  {item.get('soldCountText')} | est. revenue: {item.get('estimatedRevenue')} | rating: {item.get('rating')} ({item.get('reviewsCount')})")
    print(f"  Rank:  {rank} | source: {item['source']} | ad: {item['isAd']}")
    print(f"  URL:   {item['productUrl']}\n")
