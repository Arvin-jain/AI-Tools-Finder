import os
from weaviate.auth import AuthApiKey
from weaviate.client import Client
import weaviate.exceptions
import weaviate
import json

def VectorOfImage(strURL):
    import requests
    from PIL import Image
    from imgbeddings import imgbeddings
    image = Image.open(requests.get(strURL, stream=True).raw)
    ibed = imgbeddings()
    embedding = ibed.to_embeddings(image)
    vector = embedding.flatten().tolist()
    return vector

URL = os.getenv("WEAVIATE_URL", "......")
APIKEY = os.getenv("WEAVIATE_APIKEY", "......")

print(f"WEAVIATE_URL: {URL}")
print(f"WEAVIATE_APIKEY: {APIKEY}")


try:
    client = Client(
        url=URL,
        auth_client_secret=AuthApiKey(APIKEY),
        timeout_config=(10, 10)
    )

    if client.is_ready():
        print("Connection to Weaviate is successful.")
    else:
        print("Failed to connect to Weaviate.")
except weaviate.exceptions.WeaviateBaseError as e:
    print(f"Error connecting to Weaviate: {e}")

image_class = {
    "class": "ImageSearch",
    "description": "A class to store image data and vectors",
    "properties": [
        {
            "name": "mpn",
            "dataType": ["text"],
            "description": "The Manufacturer Part Number"
        },
        {
            "name": "imgsource",
            "dataType": ["text"],
            "description": "The source URL of the image"
        }
    ],
    "vectorizer": "none", 
    "vectorIndexConfig": {
        "distance": "cosine"
    }
}

if "ImageSearch" in client.schema.get()['classes']:
    client.schema.delete_class("ImageSearch")
    print("Deleted existing 'ImageSearch' class.")

try:
    client.schema.create_class(image_class)
    print("Class 'ImageSearch' created successfully.")
except weaviate.exceptions.SchemaValidationError as e:
    print(f"Schema validation error: {e}")
except weaviate.exceptions.WeaviateBaseError as e:
    print(f"Error creating class: {e}")

import time
t0 = time.time()

data = [
    {
        "mpn": "2967-20",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/193046/328590/17682350-891d-45c2-8c2a-4a386c88d991_MLW-2967-20__80029.1730794290.jpg?c=1"
    },
    {
        "mpn": "2869-20",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280w/products/108904/17984/47ff43e7-0968-46fe-9d24-a7793ade7ee9__73614.1647922477.jpg?c=1"
    },
    {
        "mpn": "2175MAX",
        "imgsource": "https://mprtools.com/cdn/shop/files/Ingersoll-Rand-2175MAX-1-Pistol-Grip-Impact-Wrench.jpg?v=1724453495"
    },
    {
        "mpn": "2135QXPA",
        "imgsource": "https://mprtools.com/cdn/shop/files/Ingersoll-Rand-2135QXPA-Impactool_-12.jpg?v=1724406033"
    },
    {
        "mpn": "7803RA",
        "imgsource": "https://mprtools.com/cdn/shop/files/Ingersoll-Rand-7803RA-Heavy-Duty-12-Inch-Reversible-Pnuematic-Drill.jpg?v=1724406423"
    },
    {
        "mpn": "119MAXK",
        "imgsource": "https://mprtools.com/cdn/shop/files/Ingersoll-Rand-119MAXK-Long-Barrel-Air-Hammer-Kit.jpg?v=1724445778"
    },
    {
        "mpn": "DWP849X",
        "imgsource": "https://mprtools.com/cdn/shop/files/DeWalt-DWP849X-BufferPolisher-Variable-Speed-Soft-Start-7-Inch9-Inch.jpg?v=1724452712"
    },
    {
        "mpn": "DCF630B",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/41544/295467/34e43402-5036-4764-86f3-22e205a21de4_DEW-DCF630B__02936.1724056082.jpg?c=1"
    },
    {
        "mpn": "DCGG571B",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/41625/321901/83546487-f7df-44e7-a656-e011755d514b_DEW-DCGG571B__13486.1727789047.jpg?c=1"
    },
    {
        "mpn": "DW758",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/42837/322686/a8151ff8-21f5-475e-8d7c-eba2fc5bbfd6_DEW-DW758__50894.1727791418.jpg?c=1"
    },
    {
        "mpn": "DCCS623B",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/191446/322609/1d1919f3-806b-4b1d-a72b-d3d802864346_DEW-DCCS623B__39200.1727791202.jpg?c=1"
    },
    {
        "mpn": "4151",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280w/products/67244/317863/f7e3caad-a1da-42e9-8408-68d7cf839743_IRC-4151__86613.1727777363.jpg?c=1"
    },
    {
        "mpn": "36QMAX",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280w/products/67230/318614/69fc239c-ed11-40e3-a4f7-7c60ad7225f0_IRC-36QMAX__76858.1727779505.jpg?c=1"
    },
    {
        "mpn": "2850MAX",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280x1280/products/67147/300537/2c303082-9863-407d-8082-697fb15f44cf_IRC-2850MAX__65861.1724070307.jpg?c=1"
    },
    {
        "mpn": "285B-6",
        "imgsource": "https://cdn11.bigcommerce.com/s-8sp77pdf4a/images/stencil/1280w/products/67150/325990/dbec898e-4978-4850-b892-7d24e2810293_IRC-285B-6__20340.1728807161.jpg?c=1"
    },
    {
        "mpn": "261",
        "imgsource": "https://mprtools.com/cdn/shop/files/Ingersoll-Rand-261-34-Inch-Super-Duty-Air-Impact-Wrench.jpg?v=1724406127"
    }
]

with client.batch as batch:
    for item in data:
        properties = {
            "mpn": item['mpn'],
            "imgsource": item['imgsource']
        }
        vector = VectorOfImage(item['imgsource'])
        batch.add_data_object(properties, "ImageSearch", vector=vector)
        print(f"Added {item['mpn']} to Weaviate.")

t1 = time.time()
total = t1 - t0
print(f"Total time taken: {total} seconds")

def imageSearch(image_url):
    import weaviate.classes.query as wq
    query_vector = VectorOfImage(image_url)
    
    response = (
        client.query
        .get("ImageSearch", ["mpn", "imgsource"])
        .with_near_vector({"vector": query_vector})
        .with_limit(1)
        .with_additional("distance")
        .do()
    )
    
    for result in response['data']['Get']['ImageSearch']:
        mpn = result.get("mpn", "N/A")
        imgsource = result.get("imgsource", "N/A")
        distance = result['_additional']['distance']
        print(f"MPN: {mpn}")
        print(f"Image URL: {imgsource}")
        print(f"Distance to query: {distance:.3f}\n")
        return mpn, imgsource

imgSource = "https://i.ebayimg.com/images/g/hvYAAOSwQatlHbHx/s-l1600.webp"
t0 = time.time()

print("Searching for similar image...")
mpn_result, img_link_result = imageSearch(imgSource)

t1 = time.time()
total = t1 - t0
print('Time Taken:', total)
