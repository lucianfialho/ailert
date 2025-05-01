from builder.builder import NewsletterBuilder

# Create daily newsletter
async def main():
    daily = NewsletterBuilder({
        "gh_url": "github_url",
        "gh_ftype": "daily"
    })
    daily.set_sections(["news"])
    content = await daily.section_generator()
    return content

# Run the async function
import asyncio
content = asyncio.run(main())
