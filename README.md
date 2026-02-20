# Elite Python SEO Toolkit (Tier 1 Markets)

This toolkit provides high-performance SEO auditing and data analysis, tailored for USA/UK/Canada markets.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration**:
    - Copy `.env.example` to `.env`
    - Update `DB_*` credentials if you want to perform direct database auditing.

## Usage

### 1. Simple URL Audit
Crawl a single page and analyze Title, H1, Meta Description, and Content length.

```bash
python main.py --url https://example.com
```

### 2. Sitemap Audit (Coming Soon)
Bulk analyze all URLs in a sitemap.

```bash
python main.py --sitemap https://example.com/sitemap.xml
```

### 3. Database Deep Dive (Coming Soon)
Connect directly to your Laravel/Postgres DB to validate `pages` and `seos` table consistency.

```bash
python main.py --db
```

## Features
- **Speed**: Uses `lxml` for ultra-fast HTML parsing.
- **Data**: Exports to Pandas for complex analysis.
- **Flexibility**: Works with any website or directly with your database.
