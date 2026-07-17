import re

products = [
    "Apple iPhone",
    "Samsung Mobile",
    "Dell Laptop",
    "HP Laptop",
    "Wireless Mouse",
    "Bluetooth Speaker",
    "Apple Watch"
]

keyword = input("Enter search keyword: ")
search_type = input(
    "Enter search type "
    "(exact/prefix/suffix/partial/case-insensitive): "
).lower()

escaped_keyword = re.escape(keyword)

if search_type == "exact":
    pattern = rf"\b{escaped_keyword}\b"
    flags = 0

elif search_type == "prefix":
    pattern = rf"^{escaped_keyword}"
    flags = 0

elif search_type == "suffix":
    pattern = rf"{escaped_keyword}$"
    flags = 0

elif search_type == "partial":
    pattern = escaped_keyword
    flags = 0

elif search_type == "case-insensitive":
    pattern = escaped_keyword
    flags = re.IGNORECASE

else:
    print("Invalid search type")
    exit()

matches = []

for product in products:
    if re.search(pattern, product, flags):
        matches.append(product)

print("\nMatching Products")

if matches:
    for product in matches:
        print(product)
else:
    print("No matching products found")

print("Total Matching Products:", len(matches))
