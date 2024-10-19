import requests
import urllib.parse
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
print("Access Token:", access_token)

# Define SP-API endpoint and necessary parameters
endpoint = "https://sellingpartnerapi-eu.amazon.com"
marketplace_id = "A21TJRUUN4KGV"  # Your marketplace ID
seller_id = credentials['sender_id']  # Replace with actual seller ID


headers = {
    "x-amz-access-token": access_token,
    "x-amz-date": datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
    "content-type": "application/json"
}


# product_type = "BOOK"  # Replace with your product type
# definitions_url = f"{endpoint}/productTypeDefinitions/2021-08-01/productTypes/{product_type}"

# response = requests.get(definitions_url, headers=headers)
# print(json.dumps(response.json(), indent=2))


# Step 1: Discovery - Check if item exists using ASIN
# asin_to_check = "B08N5W4NNB"  # Replace with a valid ASIN
# search_url = f"{endpoint}/catalog/v0/items/{asin_to_check}?MarketplaceId={marketplace_id}"


# response = requests.get(search_url, headers=headers)

# if response.status_code == 200:
#     print("Item discovery response:", json.dumps(response.json(), indent=2))
# else:
#     print("Error during item discovery:", response.status_code, response.text)
#     exit()  # Exit if discovery fails

# # Check if item was discovered
# item_data = response.json().get('payload', {}).get('Identifiers', {})
# if not item_data:
#     print("Item not found. Please verify the ASIN.")
#     exit()
product_data = {
  "productType": "SHOES",
  "sku": "SKU12345",
  "requirements": "LISTING",
  "summaries": [
    {
      "marketplaceId": "A1PA6795UKMFR9",
      "asin": "B09XYZ1234",
      "productType": "Shoes",
      "conditionType": "New",
      "status": ["ACTIVE"],
      "fnSku": "FNSKU12345",
      "itemName": "Nike Air Zoom Pegasus 39",
      "createdDate": "2024-10-17T12:00:00Z",
      "lastUpdatedDate": "2024-10-17T12:00:00Z",
      "mainImage": {
        "link": "https://example.com/image.jpg",
        "height": 1000,
        "width": 1000
      }
    }
  ],
"attributes": {
"rtip_manufacturer_contact_information": {
    "contact_name": "Nike, Inc.",
    "phone_number": "+1-800-806-6453",
    "email": "support@nike.com",
    "address": "One Bowerman Drive, Beaverton, OR 97005, USA"
}
,
    "item_package_dimensions": [
      {"height": "10 cm"},
      {"length": "30 cm"},
      {"width": "20 cm"}
    ],
    "item_package_weight": [
      {"unit": "KILOGRAM", "value": "1.5"}
    ],
    "item_dimensions": [
      {"height": "15 cm"},
      {"length": "35 cm"},
      {"width": "25 cm"}
    ],
    "item_weight": [
      {"unit": "KILOGRAM", "value": "1.2"}
    ],
"importer_contact_information": {
    "contact_name": "XYZ Imports Pvt. Ltd.",
    "phone_number": "+91-1234567890",
    "email": "info@xyzimports.in",
    "address": "123 Market Street, Mumbai, Maharashtra, India"
}
,
    "outer": [{"value": "Synthetic"}],
    "water_resistance_level": [{"value": "Not Water Resistant"}],
    "merchant_suggested_asin": "B08N5WRWNW",
    "style": [{"value": "Athletic"}],
    "condition_type": [{"value": "New"}],
    "footwear_size": [
      {"size_system": "US", "size_class": "Adult", "size": "10"}
    ],
    "model_name": [{"value": "Air Zoom Pegasus 39"}],
    "model_number": [{"value": "PE39-2024"}],
    "age_range_description": [{"value": "Adult"}],
    "recommended_browse_nodes": [{"value": "Athletic Shoes"}],
    "height_map": [{"value": "Low"}],
    "external_product_information": [
      {"entity": "EAN", "value": "1234567890123"}
    ],
    "batteries_required": [{"value": "false"}],
    "target_gender": [{"value": "MALE"}],
    "closure": [{"value": "Lace-Up"}],
    "heel": [{"value": "Low"}],
    "unit_count": [{"value": "1"}],
    "bullet_point": [
      {"value": "Breathable upper material"},
      {"value": "Cushioned sole for extra comfort"}
    ]
  },
  "issues": [],
  "offers": [
    {
      "price": "120.00",
      "condition": "New",
      "quantity": 50,
      "shipping": {
        "shippingMethod": "Standard",
        "shippingCost": "0.00"
      }
    }
  ],
  "fulfillmentAvailability": [
    {
      "fulfillmentChannel": "AFN",
      "quantity": 50,
      "availability": "Available"
    }
  ],
  "procurement": []
}

create_listing_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/SKU12345BOOK?marketplaceIds={marketplace_id}"

response = requests.put(create_listing_url, headers=headers, json=product_data)

if response.status_code == 200:
    print("Product created/updated successfully:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in creating/updating product:", response.status_code, response.text)

# Step 3: Maintenance - Fetch listing status
listing_status_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/SKU12345BOOK?marketplaceIds={marketplace_id}"

response = requests.get(listing_status_url, headers=headers)

if response.status_code == 200:
    print("Listing status response:", json.dumps(response.json(), indent=2))
else:
    print("Error fetching listing status:", response.status_code, response.text)

# Step 4: Fetch orders created in the last 30 days
request_params = {
    "MarketplaceIds": marketplace_id,
    "CreatedAfter": (
        datetime.datetime.now() - datetime.timedelta(days=30)
    ).isoformat(),
}
orders = requests.get(
    endpoint + "/orders/v0/orders" + "?" + urllib.parse.urlencode(request_params),
    headers={
        "x-amz-access-token": access_token
    }
)

if orders.status_code == 200:
    print("Orders fetched successfully:")
    print(json.dumps(orders.json(), indent=2))
else:
    print("Error fetching orders:", orders.status_code, orders.text)
