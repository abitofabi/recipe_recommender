import requests
from bs4 import BeautifulSoup
import json

# Target website
URL = "https://www.sharmispassions.com/recipes/breakfast-ideas/idli-recipes/"
headers = {"User-Agent": "Mozilla/5.0"}

# Send request and parse HTML
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all recipe entries
recipe_links = soup.select('a.entry-image-link')

# Extract details
recipes = []
for link in recipe_links:
    recipe_url = link.get("href")
    image_tag = link.find("img")  # Find the image inside <a>

    if image_tag:
        recipe_name = image_tag.get("alt", "No Title")  # Some images may not have alt text
        recipe_image = image_tag.get("data-src", image_tag.get("src"))  # Get image URL

        recipes.append({
            "name": recipe_name.strip(),
            "url": recipe_url,
            "image": recipe_image
        })

# Save to JSON file
with open("recipes.json", "w", encoding="utf-8") as f:
    json.dump(recipes, f, indent=4, ensure_ascii=False)

print("✅ Recipes saved to recipes.json!")
