import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("DEVTO_API_KEY")
ARTICLE_FILE = "generated_article.md"

def publish_article():
    if not API_KEY:
        print("Error: DEVTO_API_KEY not found in environment.")
        return

    try:
        with open(ARTICLE_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {ARTICLE_FILE} not found.")
        return

    # Extract title from the first header
    title = "Location Intelligence: Building an Autonomous Site Selection Engine with Geospatial AI"
    
    # Dev.to API endpoint
    url = "https://dev.to/api/articles"
    
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    # Prepare payload
    # Dev.to expects markdown with frontmatter, but we can also send it in the body
    # We will strip the title from the content to avoid duplication if needed, 
    # but Dev.to usually handles the primary title separately.
    
    article_data = {
        "article": {
            "title": title,
            "published": True,
            "body_markdown": content,
            "tags": ["python", "geospatial", "datascience", "visualization"],
            "series": "Autonomous Intelligence Experiments"
        }
    }

    print(f"Publishing '{title}' to Dev.to...")
    response = requests.post(url, headers=headers, json=article_data)

    if response.status_code == 201:
        data = response.json()
        print(f"Successfully published!")
        print(f"URL: {data.get('url')}")
    else:
        print(f"Failed to publish. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    publish_article()
