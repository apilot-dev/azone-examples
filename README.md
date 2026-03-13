# Azone API Examples

Code examples showing how to use the Azone Amazon Data API.

Get API access on RapidAPI:

https://rapidapi.com/apilot-apilot-default/api/azone-real-time-amazon-data-api

## Features

- product details
- product reviews
- seller data
- best sellers
- deals
- Amazon Haul search

## Documentation

https://www.apilot.net/azone-docs/

## RapidAPI

https://rapidapi.com/apilot-apilot-default/api/azone-real-time-amazon-data-api

## Examples

### Python

python/product_details.py

https://github.com/apilot-dev/azone-examples/blob/main/python/product_details.py

### NodeJS

node/product_details.js

https://github.com/apilot-dev/azone-examples/blob/main/node/product_details.js

### Curl
curl/product_details.sh

https://github.com/apilot-dev/azone-examples/blob/main/curl/product_details.sh


## How to run the examples

Clone the repository:
```bash
git clone https://github.com/apilot-dev/azone-examples.git
cd azone-examples

### Python example
```bash
cd python
pip install -r requirements.txt
python product_details.py

### NodeJS example
```bash
cd node
npm install
node product_details.js
```

## Example Request
```bash
curl --request GET \
	--url 'https://azone-real-time-amazon-data-api.p.rapidapi.com/product-offers?asin=B0C2JXSHSK&product_condition=NEW%2C%20USED_LIKE_NEW%2C%20USED_VERY_GOOD%2C%20USED_GOOD%2C%20USED_ACCEPTABLE&page=1&limit=100&mode=offers_only&country=US' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: azone-real-time-amazon-data-api.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_API_KEY'
```

## Example Response
```bash
{
  "status": "OK",
  "request_id": "49a4c260-ddb5-4ffa-8978-003314b8f533",
  "parameters": {
    "asin": "B0C2JXSHSK",
    "country": "US",
    "limit": 100,
    "page": 1,
    "product_condition": "NEW, USED_LIKE_NEW, USED_VERY_GOOD, USED_GOOD, USED_ACCEPTABLE",
    "mode": "offers_only"
  },
  "data": {
    "asin": "B0C2JXSHSK",
    "requested_asin": "B0C2JXSHSK",
    "product_title": "adidas Women’s VL Court 3.0 Sneaker",
    "brand": "Visit the adidas Store",
    "product_price": "59.99",
    "product_original_price": "75.00",
    "minimum_order_quantity": null,
    "currency": "USD",
    "country": "US",
    "domain": "www.amazon.com",
    "product_byline": null,
    "product_byline_link": null,
    "product_byline_links": null,
    "product_star_rating": "4.50",
    "product_num_ratings": 9903,
    "product_url": "https://www.amazon.com/dp/B0C2JXSHSK",
    "product_slug": null,
    "product_photo": null,
    "product_num_offers": 5,
    "product_availability": "In Stock",
    "product_condition": null,
    "coupon_discount_percentage": null,
    "is_best_seller": false,
    "is_amazon_choice": false,
    "is_prime": false,
    "climate_pledge_friendly": false,
    "sales_volume": 1000,
    "sales_volume_period": "past_month",
    "about_product": null,
    "product_description": null,
    "product_information": null,
    "rating_distribution": null,
    "product_photos": null,
    "product_videos": null,
    "user_uploaded_videos": null,
    "has_video": null,
    "product_details": null,
    "top_reviews": null,
    "top_reviews_global": null,
    "delivery": "FREE delivery Thursday, February 26",
    "primary_delivery_time": "FREE delivery Thursday, February 26",
    "delivery_free_days": null,
    "delivery_fastest_days": null,
    "delivery_paid_days": null,
    "category": null,
    "category_path": null,
    "product_variations_dimensions": null,
    "product_variations": null,
    "all_product_variations": null,
    "has_aplus": null,
    "aplus_images": null,
    "has_brandstory": null,
    "frequently_bought_together": null,
    "landing_asin": "B0C2JXSHSK",
    "canonical_asin": "B0C2JXSHSK",
    "parent_asin": null,
    "product_offers": [
      {
        "product_price": 59.99,
        "product_original_price": 75,
        "product_condition": "New",
        "product_condition_details": null,
        "ships_from": "Amazon.com",
        "seller": "Amazon.com",
        "seller_id": null,
        "seller_link": null,
        "seller_star_rating": "4.5",
        "seller_star_rating_info": null,
        "currency": "USD",
        "delivery_price": "FREE",
        "delivery_time": "FREE delivery Thursday, February 26 Or Prime members get FREE delivery Tomorrow, February 22. Order within 4 hrs 49 mins."
      },
      {
        "product_price": 53.99,
        "product_original_price": null,
        "product_condition": "Used - Very Good",
        "product_condition_details": null,
        "ships_from": "Amazon.com",
        "seller": "Amazon Resale",
        "seller_id": "HTTPS://WWW.AMAZON.COM/WAREHOUSE-DEALS/B?IE=UTF8&NODE=10158976011",
        "seller_link": "https://www.amazon.com/Warehouse-Deals/b?ie=UTF8&node=10158976011",
        "seller_star_rating": "5",
        "seller_star_rating_info": null,
        "currency": "USD",
        "delivery_price": "FREE",
        "delivery_time": "FREE delivery Thursday, February 26 Or fastest delivery Wednesday, February 25. Order within 5 hrs 59 mins"
      },
      {
        "product_price": 54.59,
        "product_original_price": null,
        "product_condition": "Used - Like New",
        "product_condition_details": null,
        "ships_from": "Amazon.com",
        "seller": "Amazon Resale",
        "seller_id": "HTTPS://WWW.AMAZON.COM/WAREHOUSE-DEALS/B?IE=UTF8&NODE=10158976011",
        "seller_link": "https://www.amazon.com/Warehouse-Deals/b?ie=UTF8&node=10158976011",
        "seller_star_rating": "5",
        "seller_star_rating_info": null,
        "currency": "USD",
        "delivery_price": "FREE",
        "delivery_time": "FREE delivery Thursday, February 26 Or Prime members get FREE delivery Monday, February 23. Order within 5 hrs 59 mins."
      },
      {
        "product_price": 74.95,
        "product_original_price": null,
        "product_condition": "New",
        "product_condition_details": null,
        "ships_from": "Amazon.com",
        "seller": "Zappos",
        "seller_id": "AH1YFAUS3NHX2",
        "seller_link": "https://amazon.com/gp/aag/main?ie=UTF8&seller=AH1YFAUS3NHX2&isAmazonFulfilled=1&asin=B0C2JXSHSK&ref_=olp_merch_name_3",
        "seller_star_rating": "5",
        "seller_star_rating_info": null,
        "currency": "USD",
        "delivery_price": "FREE",
        "delivery_time": "FREE delivery Thursday, February 26 Or Prime members get FREE delivery Monday, February 23. Order within 3 hrs 14 mins."
      },
      {
        "product_price": 74.99,
        "product_original_price": null,
        "product_condition": "New",
        "product_condition_details": null,
        "ships_from": "Shoe Sensation",
        "seller": "Shoe Sensation",
        "seller_id": "APMVYK5AMZ4PX",
        "seller_link": "https://amazon.com/gp/aag/main?ie=UTF8&seller=APMVYK5AMZ4PX&isAmazonFulfilled=0&asin=B0C2JXSHSK&ref_=olp_merch_name_4",
        "seller_star_rating": "4.5",
        "seller_star_rating_info": null,
        "currency": "USD",
        "delivery_price": "FREE",
        "delivery_time": "FREE delivery February 26 - 27. Details"
      }
    ],
    "filled_from_catalog_fields": [
      "brand",
      "product_title",
      "product_price",
      "product_original_price",
      "product_star_rating",
      "product_num_ratings",
      "sales_volume",
      "sales_volume_period",
      "product_availability",
      "is_prime",
      "is_best_seller",
      "is_amazon_choice",
      "climate_pledge_friendly"
    ],
    "catalog_last_seen_at": "2026-02-22T00:00:32.968209+00:00"
  },
  "debug": {
    "timing": {
      "offers_wait_ms": 2500,
      "direct_offer_nav_ms": 5437.32,
      "direct_offer_wait_ms": 2505.98,
      "aod_ajax_fast_ms": 4388.68,
      "offers_path": "aod_ajax",
      "total_ms": 14451.74
    }
  }
}
```

