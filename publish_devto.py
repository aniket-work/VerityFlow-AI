import requests
import os
from dotenv import load_dotenv

load_dotenv()

def publish_to_devto(filepath):
    api_key = os.getenv("DEVTO_API_KEY")
    if not api_key:
        print("Error: DEVTO_API_KEY not found in .env")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Extract frontmatter (simple version)
    lines = content.split('\n')
    title = ""
    tags = []
    body_lines = []
    in_frontmatter = False
    
    for line in lines:
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            if line.startswith("title:"):
                title = line.replace("title:", "").strip().strip('"')
            elif line.startswith("tags:"):
                tags = [t.strip() for t in line.replace("tags:", "").split(',')]
        else:
            body_lines.append(line)

    body = '\n'.join(body_lines)

    # Dev.to API is maximum 4 tags
    if len(tags) > 4:
        tags = tags[:4]

    payload = {
        "article": {
            "title": title,
            "published": True,
            "body_markdown": content, # Dev.to can parse frontmatter if included in body
            "tags": tags
        }
    }

    url = "https://dev.to/api/articles"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    print(f"Publishing article: {title}...")
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        data = response.json()
        print(f"Successfully published! URL: {data['url']}")
    else:
        print(f"Failed to publish: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    publish_to_devto("article.md")
