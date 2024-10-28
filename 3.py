import requests
import datetime
import json
from credentials import credentials

# Sample data for existing products fetched (replace with actual fetched data)
existing_products = [
    {
        "sku": "VU-NHKF-JN3Q",
        "summaries": [
            {
                "marketplaceId": "A21TJRUUN4KGV",
                "asin": "B0DJ36MH8Z",
                "productType": "TOY_FIGURE",
                "itemName": "German Shepherd Dog Figurine, 25 cm, Brown and Black",
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
            }
        ]
    }
]

# Select an existing product as a template
selected_product = existing_products[0]['summaries'][0]

# Prepare new product data based on the existing product
product_data = {
    "productType": selected_product["productType"],
    "sku": "SKU12345NEWBOOK",
    "requirements": "LISTING",
    "summaries": [
        {
            "marketplaceId": selected_product["marketplaceId"],
            "asin": selected_product["asin"],
            "conditionType": "New",
            "status": ["ACTIVE"],
            "itemName": "New Item Name Here",
            "mainImage": {
                "link": "https://example.com/new_image.jpg",
                "height": 1000,
                "width": 1000
            }
        }
    ],
    "attributes": {
        "externally_assigned_product_identifier": [{"value": "9780743273565"}],
        "language": [{"value": "English"}],
        "importer_contact_information": {
            "name": "John Doe",
            "phone": "+1-555-555-5555",
            "email": "johndoe@example.com"
        },
        "merchant_suggested_asin": "B000123456",
        "material": "Plastic",
        "brand": "BrandName",
        "rtip_manufacturer_contact_information": {
            "name": "Manufacturer Inc.",
            "phone": "+1-555-123-4567",
            "email": "info@manufacturer.com"
        },
        "item_package_dimensions": {
            "length": "10",
            "width": "5",
            "height": "3",
            "unit": "cm"
        },
        "item_name": "Sample Product Name",
        "item_weight": {
            "value": 250,
            "unit": "g"
        },
        "target_audience_keyword": "Adults",
        "packer_contact_information": {
            "name": "Packing Company",
            "phone": "+1-555-765-4321",
            "email": "packing@company.com"
        },
        "bullet_point": [
            "High quality",
            "Durable material",
            "Easy to use"
        ],
        "country_of_origin": "China",
        "color": "Red",
        "item_length_width_height": {
            "length": "10",
            "width": "5",
            "height": "3",
            "unit": "cm"
        },
        "manufacturer_minimum_age": "12",
        "part_number": "PN123456",
        "product_description": "This is a sample product description.",
        "unit_count": "1",
        "manufacturer_maximum_age": "99",
        "item_package_weight": {
            "value": "300",
            "unit": "g"
        },
        "condition_type": "New",
        "included_components": [
            "Item",
            "User Manual"
        ],
        "batteries_required": "No",
        "is_assembly_required": "No",
        "manufacturer": "Manufacturer Inc.",
        "safety_warning": "Keep away from fire.",
        "external_product_information": {
            "entity": "Product Details",
            "link": "http://example.com/product-details"
        },
        "recommended_browse_nodes": [
            "123456",
            "654321"
        ],
        "item_type_name": "Electronics",
        "language": [
            {"value": "en"}
        ]
    },
    "offers": [
        {
            "price": "19.99",
            "currency": "USD",
            "condition": "New",
            "quantity": 100,
            "shipping": {
                "shippingMethod": "Standard",
                "shippingCost": "0.00"
            }
        }
    ],
    "fulfillmentAvailability": [
        {
            "fulfillmentChannel": "AFN",
            "quantity": 100,
            "availability": "Available"
        }
    ]
}

# Get access token
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

# Create a new listing
endpoint = "https://sellingpartnerapi-eu.amazon.com"
seller_id = credentials['sender_id']
marketplace_id = "A21TJRUUN4KGV"
headers = {
    "x-amz-access-token": access_token,
    "x-amz-date": datetime.datetime.utcnow().isoformat(),
    "content-type": "application/json"
}

create_listing_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/{product_data['sku']}?marketplaceIds={marketplace_id}"
response = requests.put(create_listing_url, headers=headers, json=product_data)

if response.status_code == 200:
    print("Product created/updated successfully:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in creating/updating product:", response.status_code, response.text)

# Fetch product types
product_type_url = f"{endpoint}/definitions/2020-09-01/productTypes"
params = {
    "marketplaceIds": marketplace_id,
    "keywords": "LUGGAGE",
    "locale": "en_IN"
}

response = requests.get(product_type_url, headers=headers, params=params)

if response.status_code == 200:
    print("Product type:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in fetching product types:", response.status_code, response.text)



# Fetch product types
product_type_url = f"{endpoint}/definitions/2020-09-01/productTypes"
params = {
    "marketplaceIds": marketplace_id,
    "itemName": "Book",
    "locale": "en_IN"
}

response = requests.get(product_type_url, headers=headers, params=params)

if response.status_code == 200:
    print("Product type:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in fetching product types:", response.status_code, response.text)
