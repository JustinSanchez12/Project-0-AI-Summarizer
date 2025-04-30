from langchain.tools import tool
from web_scraper.scraper import scrape_with_bs4

def make_summarize_paragraph_tool(llm):
    @tool
    def summarize_paragraph(prompt: str) -> str:
        """
        Summarize text from a URL or raw source text that the user has provided.

        Input:
        - prompt: Insert URL Link or Raw Text

        Output:
        - A concise summary in 1–2 paragraphs
        """
        full_prompt = f"Summarize the following text in 1–2 paragraphs:\n\n{prompt}"
        return llm.invoke(full_prompt)
    return summarize_paragraph

def highlight_text_tool(llm):
    @tool
    def highlight_text(prompt: str) -> str:
        """
        Extracts and returns the main points from a block of text as bullet points.

        Input:
        - prompt: Raw text from a page or document

        Output:
        - A list of the most important bullet points extracted from the input
        """
        query = f"List the main points from the following text in bullet points:\n\n{prompt}"
        output = llm.invoke(query)

        # Split into bullet points (handle both "-" and "•")
        lines = output.splitlines()
        bullets = [line.strip("•- ").strip() for line in lines if line.strip()]
        return bullets
    return highlight_text

def scrape_and_summarize_tool(llm):
    @tool
    def summarize_url(url: str) -> str:
        """Scrapes a URL and summarizes the content using the LLM."""
        try:
            raw_text = scrape_with_bs4(url)
        except Exception as e:
            return f"Error scraping URL: {e}"
        full_prompt = f"Summarize the following webpage content in 1–2 paragraphs:\n\n{raw_text}"
        return llm.invoke(full_prompt)
    return summarize_url
    
tools = [make_summarize_paragraph_tool, highlight_text_tool, scrape_and_summarize_tool]