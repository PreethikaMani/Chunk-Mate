import re

def parse_markdown_paragraphs(content):
    lines = content.split('\n')
    chunks = []
    heading_context = []
    inside_table = False
    table_lines = []

    for line in lines:
        if line.startswith('#'):
            heading_context.append(line.strip())
        elif line.strip().startswith('|') and '|' in line:
            inside_table = True
            table_lines.append(line)
        elif inside_table and not line.strip():
            # End of table
            parsed_table_chunks = parse_table(table_lines, heading_context)
            chunks.extend(parsed_table_chunks)
            table_lines = []
            inside_table = False
        elif line.strip():  # Paragraph
            chunk = {
                "heading_context": "\n".join(heading_context),
                "content": line.strip(),
                "links": extract_links(line)
            }
            chunks.append(chunk)

    # If file ends with a table
    if inside_table and table_lines:
        chunks.extend(parse_table(table_lines, heading_context))

    return chunks


def parse_table(table_lines, heading_context):
    # Remove pipes and split
    headers = [h.strip() for h in table_lines[0].strip().split('|') if h.strip()]
    rows = table_lines[2:]  # Skip headers + separator row
    table_chunks = []

    for row in rows:
        values = [v.strip() for v in row.strip().split('|') if v.strip()]
        data = [f"{headers[i]}: {values[i]}" for i in range(min(len(headers), len(values)))]
        table_chunks.append({
            "heading_context": "\n".join(heading_context),
            "content": "\n".join(data),
            "links": extract_links("\n".join(data))
        })

    return table_chunks

def extract_links(text):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return [{"text": match[0], "url": match[1]} for match in matches]