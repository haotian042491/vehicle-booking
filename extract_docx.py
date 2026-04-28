import zipfile, re, sys

docx_path = '/tmp/feishu_doc.docx'
with zipfile.ZipFile(docx_path, 'r') as z:
    with z.open('word/document.xml') as f:
        xml = f.read().decode('utf-8')

# Remove XML tags
text = re.sub(r'<[^>]+>', ' ', xml)
# Collapse whitespace
text = re.sub(r'[ \t]+', ' ', text)
# Clean up blank lines
lines = [l.strip() for l in text.split('\n') if l.strip()]
print('\n'.join(lines))
