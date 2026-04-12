"""
Generate rename_mappings.json from rename_candidates.json.
Extracts author, year, title from PDF metadata and first-page text.
"""
import json, re, sys
from pathlib import Path

FILTER_TIDYING = Path("literature/automated_literature_searches/filter_tidying")

with open(FILTER_TIDYING / 'rename_candidates.json', encoding='utf-8') as f:
    candidates = json.load(f)

def extract_year(text):
    # Look for 4-digit year 2000-2026
    years = re.findall(r'\b(20[012]\d)\b', text)
    if years:
        # Prefer years from metadata/early text
        return years[0]
    return 'XXXX'

def clean_title(title):
    # Remove HTML tags, truncate at 60 chars, replace spaces with underscores
    title = re.sub(r'<[^>]+>', '', title)
    title = re.sub(r'[^\w\s-]', '', title)
    title = title.strip()
    # Truncate at ~7 words
    words = title.split()[:7]
    return '_'.join(w.capitalize() for w in words if w)

def clean_author(author):
    # Take first author surname only
    author = re.sub(r'<[^>]+>', '', author).strip()
    # Remove email, affiliations etc
    author = author.split('\n')[0].split(';')[0].split(',')[0]
    # Extract surname (last word before any comma/semicolon, or first word if simple)
    parts = author.strip().split()
    if parts:
        # If "Firstname Lastname" format, take last part
        surname = parts[-1]
        # Clean to alphanumeric
        surname = re.sub(r'[^\w]', '', surname)
        return surname if surname else 'Unknown'
    return 'Unknown'

def parse_candidate(rec):
    text = rec.get('text', '')

    # Extract metadata fields
    meta_author = ''
    meta_title = ''
    meta_year = ''

    for line in text.split('\n'):
        if line.startswith('[metadata:author]'):
            meta_author = line.replace('[metadata:author]', '').strip()
        elif line.startswith('[metadata:title]'):
            meta_title = line.replace('[metadata:title]', '').strip()
        elif line.startswith('[metadata:creationDate]'):
            date_str = line.replace('[metadata:creationDate]', '').strip()
            m = re.search(r'D:(\d{4})', date_str)
            if m:
                meta_year = m.group(1)

    # Get first page text (after [first_page_text] marker)
    first_page = ''
    if '[first_page_text]' in text:
        first_page = text.split('[first_page_text]')[1][:1000]

    # --- Author ---
    author = 'Unknown'
    multi = False
    if meta_author:
        # Check for multiple authors
        if any(sep in meta_author for sep in [';', ',', ' and ', ' & ']):
            multi = True
        author = clean_author(meta_author)
    else:
        # Try to extract from first page: look for author line patterns
        # Patterns like "John Smith1, Jane Doe2" near the top
        lines = first_page.split('\n')[:20]
        for line in lines:
            line = line.strip()
            # Skip title-like lines (all caps, very long)
            if len(line) > 10 and not line.isupper() and re.search(r'[A-Z][a-z]+ [A-Z][a-z]+', line):
                if any(sep in line for sep in [',', ' and ', ' & ']):
                    multi = True
                names = re.findall(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)+', line)
                if names:
                    # Take last name of first author
                    first_name = names[0]
                    author = first_name.split()[-1]
                    break

    # --- Year ---
    year = meta_year if meta_year and 2000 <= int(meta_year) <= 2026 else ''
    if not year:
        year = extract_year(first_page[:500])
    if not year or not year.isdigit() or not (2000 <= int(year) <= 2026):
        year = extract_year(text[:500])
    if not year:
        year = 'XXXX'

    # --- Title ---
    title = ''
    if meta_title:
        title = clean_title(meta_title)
    else:
        # Try first page: look for a prominent title line
        lines = first_page.split('\n')[:15]
        for line in lines:
            line = line.strip()
            if 20 < len(line) < 200 and not re.match(r'^\d', line):
                title = clean_title(line)
                break
    if not title:
        # Fall back to filename
        title = Path(rec['file']).stem[:40]

    return {
        'file': rec['file'],
        'author': author,
        'multi_author': multi,
        'year': year,
        'title': title
    }

mappings = [parse_candidate(r) for r in candidates]

# Generate new filenames
for m in mappings:
    suffix = '_etal' if m['multi_author'] else ''
    new_name = f"{m['author']}{suffix}_{m['year']}_{m['title']}.pdf"
    # Sanitize
    new_name = re.sub(r'[<>:"/\\|?*]', '_', new_name)
    m['new_name'] = new_name

out = FILTER_TIDYING / 'rename_mappings.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(mappings, f, ensure_ascii=False, indent=2)

print(f'Generated {len(mappings)} rename mappings -> {out}')
print()
print('Sample mappings:')
for m in mappings[:5]:
    print(f"  {Path(m['file']).name}")
    print(f"  -> {m['new_name']}")
    print()
