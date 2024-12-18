import requests
import datetime
import json
from credentials import credentials
import urllib.parse

marketplace_id = "A21TJRUUN4KGV"


product_data = {
    "productType": "TOY_FIGURE",
    "sku": "S5-WXKK-TY1B",
    "requirements": "LISTING",
    "asin": "B0DJ34CYJ2",
    "conditionType": "new_new",

    "itemName": "Test",
    "mainImage": {
    "link": "https://m.media-amazon.com/images/I/21K8ZBPnKGL.jpg",
    "height": 248,
    "width": 300
    },
    "summaries": [
    {
        "marketplaceId": "A21TJRUUN4KGA",
        "asin": "B0DJ34CYJ2",
        "productType": "TOY_FIGURE",
        "conditionType": "new_new",

        "itemName": "Test",
        "mainImage": {
        "link": "https://m.media-amazon.com/images/I/21K8ZBPnKGL.jpg",
        "height": 248,
        "width": 300
        }
    }
    ],
    "attributes": {
    "color": [
        {
        "language_tag": "en_IN",
        "value": "black brown",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "item_type_name": [
        {
        "language_tag": "en_IN",
        "value": "Toy",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "included_components": [
        {
        "language_tag": "en_IN",
        "value": "none",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "item_length_width_height": [
        {
        "height": {
            "unit": "centimeters",
            "value": 9.0
        },
        "length": {
            "unit": "centimeters",
            "value": 15.0
        },
        "width": {
            "unit": "centimeters",
            "value": 12.0
        },
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "fulfillment_availability": [
        {
        "fulfillment_channel_code": "DEFAULT",
        "quantity": 10,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],

    "safety_warning": [
        {
        "language_tag": "en_IN",
        "value": "Safe for childrens",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "number_of_pieces": [
        {
        "value": 4,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "recommended_browse_nodes": [
        {
        "value": "1378446031",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "manufacturer_maximum_age": [
        {
        "value": 40.0,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "bullet_point": [
        {
        "language_tag": "en_IN",
        "value": "Soft toy, dog figure",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "product_description": [
        {
        "language_tag": "en_IN",
        "value": "A cute dog figuer that children can play with",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "brand": [
        {
        "language_tag": "en_IN",
        "value": "Generic",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "supplier_declared_has_product_identifier_exemption": [
        {
        "value": True,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "manufacturer_minimum_age": [
        {
        "value": 20.0,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "toy_figure_type": [
        {
        "value": "play_figure",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "country_of_origin": [
        {
        "value": "IN",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "rtip_manufacturer_contact_information": [
        {
        "value": "local store",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "merchant_shipping_group": [
        {
        "value": "legacy-template-id",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "item_name": [
        {
        "language_tag": "en_IN",
        "value": "Test",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "condition_type": [
        {
        "value": "new_new",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "target_audience_keyword": [
        {
        "language_tag": "en_IN",
        "value": "Unisex Children",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "material": [
        {
        "language_tag": "en_IN",
        "value": "Thermoplastic Rubber",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "is_assembly_required": [
        {
        "value": False,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "part_number": [
        {
        "value": "none",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "external_product_information": [
        {
        "entity": "HSN Code",
        "value": "610547",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "unit_count": [
        {
        "value": 18.0,
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "packer_contact_information": [
        {
        "language_tag": "en_IN",
        "value": "toy store, roorkee",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "other_product_image_locator_1": [
        {
        "media_location": "https://m.media-amazon.com/images/I/212aYVyVfzL.jpg",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "main_product_image_locator": [
        {
        "media_location": "https://m.media-amazon.com/images/I/21K8ZBPnKGL.jpg",
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ],
    "purchasable_offer": [
        {
        "currency": "INR",
        "audience": "ALL",
        "maximum_retail_price": [
            {
            "schedule": [
                {
                "value_with_tax": 70.0
                }
            ]
            }
        ],
        "our_price": [
            {
            "schedule": [
                {
                "value_with_tax": 50.0
                }
            ]
            }
        ],
        "minimum_seller_allowed_price": [
            {
            "schedule": [
                {
                "value_with_tax": 40.0
                }
            ]
            }
        ],
        "marketplace_id": "A21TJRUUN4KGV"
        }
    ]
    },

    "offers": [
    {
        "marketplaceId": "A21TJRUUN4KGV",
        "offerType": "B2C",
        "price": {
        "currency": "INR",
        "currencyCode": "INR",
        "amount": "50.0"
        },
        "audience": {
        "value": "ALL",
        "displayName": "Sell on Amazon"
        }
    }
    ],
    "fulfillmentAvailability": [
    {
        "fulfillmentChannelCode": "DEFAULT",
        "quantity": 10
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

if token_response.status_code == 200:
    access_token = token_response.json().get('access_token')
else:
    print("Error fetching access token:", token_response.json())
    exit()

# Create a new listing
endpoint = "https://sellingpartnerapi-eu.amazon.com"
seller_id = credentials['sender_id']

headers = {
    "x-amz-access-token": access_token,
    "x-amz-date": datetime.datetime.utcnow().isoformat(),
    "content-type": "application/json"
}


create_listing_url = f"{endpoint}/listings/2021-08-01/items/{seller_id}/{product_data['sku']}?marketplaceIds={marketplace_id}"
response = requests.put(create_listing_url, headers=headers, json=product_data)




if response.status_code in [200, 201]:
    print("Product created/updated successfully:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error in creating/updating product:", response.status_code, response.text)

