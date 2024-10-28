import requests
import datetime
import json
from credentials import credentials

# Get Access Token
token_response = requests.post(
    "https://api.amazon.com/auth/o2/token",
    data={
        "grant_type": "refresh_token",
        "refresh_token": credentials['refresh_token'],
        "client_id": credentials['lwa_app_id'],
        "client_secret": credentials['lwa_client_secret']
    },
)
access_token = token_response.json().get('access_token')
if not access_token:
    print("Error fetching access token:", token_response.json())
    exit()

# Setup
endpoint = "https://sellingpartnerapi-eu.amazon.com"
marketplace_id = "A21TJRUUN4KGV"
seller_id = credentials['sender_id']

headers = {
    "x-amz-access-token": access_token,
    "x-amz-date": datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
    "content-type": "application/json"
}

# Fetch valid product types if needed
product_type = "media"  # Verify this with Amazon
definitions_url = f"{endpoint}/productTypeDefinitions/2021-08-01/productTypes/{product_type}"
response = requests.get(definitions_url, headers=headers)
print("Product Type Definitions:", json.dumps(response.json(), indent=2))

# Update Product Data (Adjust product_type if needed)
product_data = {
    "productType": product_type,
    "sku": "SKU12345BOOK",
    "requirements": "LISTING",
    "attributes": {
        "author": [{"value": "James Clear"}],
        "isbn_10": [{"value": "0735211299"}],
        "language": [{"value": "English"}]
    }
}
create_listing_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/SKU12345BOOK?marketplaceIds={marketplace_id}"
response = requests.put(create_listing_url, headers=headers, json=product_data)

if response.status_code == 200:
    print("Product created/updated successfully:", json.dumps(response.json(), indent=2))
else:
    print("Error in creating/updating product:", response.status_code, response.text)

# Fetch listing status
listing_status_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}?marketplaceIds={marketplace_id}"
response = requests.get(listing_status_url, headers=headers)

if response.status_code == 200:
    print("Listing status response:", json.dumps(response.json(), indent=2))
else:
    print("Error fetching listing status:", response.status_code, response.text)

# Fetch orders from the past 30 days
request_params = {
    "MarketplaceIds": [marketplace_id],
    "CreatedAfter": (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
}
orders = requests.get(endpoint + "/orders/v0/orders", headers=headers, params=request_params)

if orders.status_code == 200:
    print("Orders fetched successfully:", json.dumps(orders.json(), indent=2))
else:
    print("Error fetching orders:", orders.status_code, orders.text)



# Sample data from the listing status response (replace with actual fetched data)
existing_products = [
    {
        "sku": "VU-NHKF-JN3Q",
        "summaries": [
            {
                "marketplaceId": "A21TJRUUN4KGV",
                "asin": "B0DJ36MH8Z",
                "productType": "TOY_FIGURE",
                "itemName": "German Shepherd Dog Figurine, 25 cm, Brown and Black",
                # Additional attributes if necessary
            }
        ]
    },
    {
        "sku": "S5-WXTK-TY1W",
        "summaries": [
            {
                "marketplaceId": "A21TJRUUN4KGV",
                "asin": "B0DJ34CYJ8",
                "productType": "TOY_FIGURE",
                "itemName": "Cute Dog Toy",
                # Additional attributes if necessary
            }
        ]
    }
]

# Select an existing product to use as a template
selected_product = existing_products[0]['summaries'][0]  # Using the first product as an example

# Prepare new product data based on the existing product
product_data = {
    "productType": selected_product["productType"],  # Use the same product type
    "sku": "SKU12345NEWBOOK",  # New SKU for the new product
    "requirements": "LISTING",
    "summaries": [
        {
            "marketplaceId": selected_product["marketplaceId"],
            "asin": selected_product["asin"],  # Reusing ASIN for the new product
            "conditionType": "New",
            "status": ["ACTIVE"],  # Assuming you want this to be active
            "itemName": "New Item Name Here",  # Update as necessary
            "mainImage": {
                "link": "https://example.com/new_image.jpg",  # Update with a new image link
                "height": 1000,
                "width": 1000
            }
        }
    ],
    "attributes": {
        # Add relevant attributes or copy from the selected product
        "author": [{"value": "New Author"}],
        "isbn_10": [{"value": "NewISBN10"}],
        "language": [{"value": "English"}],
        # Include additional attributes as necessary
    },
    # Add offers, fulfillment availability, etc., as needed
}

# Example of adding offers and fulfillment availability
product_data["offers"] = [
    {
        "price": "19.99",  # Update with actual price
        "currency": "USD",
        "condition": "New",
        "quantity": 100,
        "shipping": {
            "shippingMethod": "Standard",
            "shippingCost": "0.00"
        }
    }
]

product_data["fulfillmentAvailability"] = [
    {
        "fulfillmentChannel": "AFN",
        "quantity": 100,
        "availability": "Available"
    }
]

# Proceed to create the new listing
create_listing_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/{product_data['sku']}?marketplaceIds={marketplace_id}"
response = requests.put(create_listing_url, headers=headers, json=product_data)

if response.status_code == 200:
    print("Product created/updated successfully:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in creating/updating product:", response.status_code, response.text)
