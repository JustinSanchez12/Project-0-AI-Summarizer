import requests
from bs4 import BeautifulSoup
import re

def scrape_with_bs4(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise ValueError(f"Request failed for {url}: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script, style, and irrelevant tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside", "form"]):
        tag.decompose()

    # Try to detect the main content section dynamically
    candidate_tags = soup.find_all(["article", "main", "section", "div"])
    
    best_section = max(
        candidate_tags,
        key=lambda tag: len(tag.find_all("p")),
        default=None
    )

    if not best_section:
        return "No substantial content found."

    # Extract text from all <p> tags
    paragraphs = best_section.find_all("p")
    cleaned = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

    # Optional: remove duplicates or very short lines
    unique_cleaned = list(dict.fromkeys(filter(lambda x: len(x) > 40, cleaned)))

    return "\n\n".join(unique_cleaned)
