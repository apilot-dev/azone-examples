"""
influencer_profile
 
Influencer Profile
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/influencer-profile"

querystring = {"influencer_name":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
seller_products
 
Seller Products
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/seller-products"

querystring = {"seller_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
seller_reviews
 
Seller Reviews
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/seller-reviews"

querystring = {"seller_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
endpoints
 
List Endpoints
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/endpoints"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
influencer_post_products
 
Influencer Post Products
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/influencer-post-products"

querystring = {"influencer_name":"","post_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
deals
 
Deals
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/deals"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
promo_code_details
 
Promo Code Details
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/promo-code-details"

querystring = {"promo_code":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
top_product_reviews
 
Top Product Reviews
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/top-product-reviews"

querystring = {"asin":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
health
 
Health Check
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/health"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
haul_search
 
Haul Search
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/haul-search"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
seller_profile
 
Seller Profile
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/seller-profile"

querystring = {"seller_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
product_details
 
Product Details
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-details"

querystring = {"asin":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
deal_products
 
Deal Products
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/deal-products"

querystring = {"deal_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
asin_to_gtin
 
Asin To Gtin
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/asin-to-gtin"

querystring = {"asin":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
product_offers
 
Product Offers
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-offers"

querystring = {"asin":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
product_category_list
 
Product Category List
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-category-list"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
product_reviews
 
Product Reviews
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-reviews"

querystring = {"asin":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
best_sellers
 
Best Sellers
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/best-sellers"

querystring = {"category":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
product_by_category
 
Product By Category
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-by-category"

querystring = {"node_id":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
root
 
Root
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
haul_categories
 
Haul Categories
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/haul-categories"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)




"""
search
 
Search Products
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/search"

querystring = {"query":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




"""
influencer_posts
 
Influencer Posts
"""

import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/influencer-posts"

querystring = {"influencer_name":""}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


