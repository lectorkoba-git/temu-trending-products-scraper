# ⚡ Temu Trending Products & Lightning Deals Tracker

[![Temu Trending Products](https://apify.com/actor-badge?actor=magic-scraper/temu-trending-products-scraper)](https://apify.com/magic-scraper/temu-trending-products-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$1.80%20%2F%201K%20results-blue?style=flat-square)
![No Login](https://img.shields.io/badge/Login-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python examples and API reference for the **[Temu Trending Products & Lightning Deals Tracker](https://apify.com/magic-scraper/temu-trending-products-scraper)** on Apify: products from the feeds Temu itself promotes — **Lightning Deals, 5-Star Rated, Local Warehouse (US) and Homepage trends** — with units sold, estimated revenue, prices, discounts, ratings and Temu's category ranks.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/temu-trending-products-scraper)**

---

## 🎯 Who is this for?

- **Dropshippers & Shopify/Amazon sellers** — see which products Temu is pushing and how many units they sold.
- **Product researchers** — collect Temu's own *Best sellers #N* / *Top rated #N* category ranks.
- **Deal trackers** — schedule hourly runs on Lightning Deals and follow `dealEndsAt` / `dealSoldPercent`.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $1.80 per 1,000 products + $0.00005 start fee; filters are applied before saving, so you pay only for kept products |
| **Run time (measured)** | ~7–25 s per run, ~200–250 unique products with all four feeds |
| **Sales data** | `soldCount` parsed from Temu badges (`13K+ sold` → 13000); `estimatedRevenue` = price × units sold (lower bound) |
| **Unknown values** | `null` — nothing is guessed or filled with placeholders |
| **Login / cookies** | Not required |

### ⚠️ Limitations

Temu shows **keyword search results and individual product pages only to logged-in users**. This actor therefore does **not** run Temu site searches or scrape arbitrary product URLs. The `keywords` input filters the trending feeds by title — it is not a site search.

---

## 🚀 Quickstart (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/temu-trending-products-scraper").call(run_input={
    "sources": ["lightning_deals", "five_star"],
    "minSold": 1000,
    "minRating": 4.5,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["soldCountText"], item["price"], item["rankingType"], item["rankingNumber"], item["title"][:60])
```

---

## 📥 Input

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `sources` | `array[string]` | all four | `lightning_deals`, `five_star`, `local_warehouse`, `homepage` |
| `keywords` | `array[string]` | `[]` | Keep products whose title contains all words of any keyword |
| `maxResults` | `integer` | `200` | Max products saved per run |
| `minSold` | `integer` | `0` | Minimum units sold |
| `minRating` | `number` | `0` | Minimum star rating |
| `onSaleOnly` | `boolean` | `false` | Only products priced below market price |
| `excludeAds` | `boolean` | `false` | Skip sponsored products |
| `proxyConfiguration` | `object` | off | Direct connection first; if Temu redirects the guest session to a login wall, the actor retries once through Apify Proxy (US) |

---

## 📤 Output Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `goodsId` | `string` | Temu product ID |
| `title` | `string` | Product title |
| `price` | `number` | Current price |
| `originalPrice` | `number \| null` | Temu's listed market price |
| `currency` | `string` | Currency code |
| `discountPercentage` | `number \| null` | Discount in percent |
| `isOnSale` | `boolean` | Price below market price |
| `soldCount` | `integer \| null` | Units sold (parsed from the badge) |
| `soldCountText` | `string \| null` | Badge text, e.g. `13K+ sold` |
| `estimatedRevenue` | `number \| null` | price × soldCount |
| `rating` | `number \| null` | Star rating |
| `reviewsCount` | `integer \| null` | Review count |
| `rankingType` | `string \| null` | `Best sellers` / `Top rated` |
| `rankingNumber` | `integer \| null` | Rank in the category |
| `rankingCategory` | `string \| null` | Category of the rank |
| `brand` | `string \| null` | Brand when shown |
| `isAd` | `boolean` | Sponsored product |
| `isLocalWarehouse` | `boolean` | Ships from a local (US) warehouse |
| `dealEndsAt` | `string \| null` | Lightning-deal end time (ISO 8601) |
| `dealSoldPercent` | `integer \| null` | Lightning-deal sold-through % |
| `mallId` / `mallUrl` | `string` | Seller store ID and URL |
| `productUrl` / `imageUrl` | `string` | Canonical product URL and image |
| `tags` | `array[string]` | Temu labels, e.g. `Local Warehouse` |
| `source` | `string` | Feed the product came from |
| `matchedKeyword` | `string \| null` | Keyword that matched, if `keywords` was set |
| `scrapedAt` | `string` | ISO 8601 timestamp |

### Sample record (real run)

```json
{
  "goodsId": "607295605976896",
  "title": "Portable Tire Inflator Air Compressor, Cordless Electric Bike Pump, 200PSI ...",
  "price": 12.24,
  "originalPrice": 99.99,
  "currency": "USD",
  "discountPercentage": 87.8,
  "isOnSale": true,
  "soldCount": 13000,
  "soldCountText": "13K+ sold",
  "estimatedRevenue": 159120.0,
  "rating": 4.8,
  "reviewsCount": 694,
  "rankingType": "Top rated",
  "rankingNumber": 1,
  "rankingCategory": "Camping & Hiking",
  "brand": null,
  "isAd": true,
  "isLocalWarehouse": true,
  "dealEndsAt": "2026-10-31T06:59:59+00:00",
  "dealSoldPercent": 54,
  "mallId": "634418224400766",
  "mallUrl": "https://www.temu.com/mall.html?mall_id=634418224400766",
  "productUrl": "https://www.temu.com/portable-tire-inflator-air-compressor-...-g-607295605976896.html",
  "imageUrl": "https://img.kwcdn.com/product/fancy/02607298-897d-47fb-95d9-b1af4058b7eb.jpg",
  "tags": ["Local Warehouse"],
  "source": "local_warehouse",
  "matchedKeyword": null,
  "scrapedAt": "2026-10-29T08:35:51+00:00"
}
```

---

## 🔗 Related Scrapers

- [Etsy Bestsellers & Tags Scraper](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)
- [TikTok Shop Search Scraper](https://apify.com/magic-scraper/tiktok-shop-search-scraper)
- [eBay Seller Contact Scraper](https://apify.com/magic-scraper/ebay-seller-contact-scraper)

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/temu-trending-products-scraper).
