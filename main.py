import argparse
import sys
import os
from dotenv import load_dotenv
from src.audit import SEOAuditor
from src.utils import setup_logger
from src.brain import Brain
from src.writer import Writer

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Elite SEO Toolkit & Autonomous Blogger")
    
    # Existing arguments
    parser.add_argument("--url", help="Target URL to audit")
    parser.add_argument("--sitemap", help="Sitemap URL for bulk audit")
    parser.add_argument("--db", action="store_true", help="Connect to database for deep audit")
    
    # New Autonomous Arguments
    parser.add_argument("--auto-blog", help="Start autonomous blogging engine for a specific niche")
    
    args = parser.parse_args()
    logger = setup_logger()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    # Autonomous Mode
    if args.auto_blog:
        niche = args.auto_blog
        logger.info(f"Starting Autonomous Blogging Engine for Niche: {niche}")
        
        # 1. Brain Phase
        brain = Brain()
        plan = brain.generate_content_plan(niche)
        
        if not plan:
            logger.error("No trending topics found. Try a broader niche.")
            return

        logger.info(f"Generated Content Plan: {len(plan)} articles")
        
        # 2. Writer Phase
        writer = Writer()
        for item in plan:
            logger.info(f"Drafting article: {item['title']}")
            content = writer.generate_article(item['topic'], item['keywords'])
            
            # Save draft locally for now (Publisher coming next)
            filename = f"draft_{item['topic'].replace(' ', '_')}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Draft saved to {filename}")

        return

    # Existing Audit Logic
    auditor = SEOAuditor()

    if args.url:
        logger.info(f"Starting audit for: {args.url}")
        report = auditor.audit_url(args.url)
        print(report)
    elif args.sitemap:
        logger.info(f"Starting bulk audit from sitemap: {args.sitemap}")
        # auditor.audit_sitemap(args.sitemap)
    
    if args.db:
        logger.info("Attempting database connection...")
        # db_connector.connect()

if __name__ == "__main__":
    main()
