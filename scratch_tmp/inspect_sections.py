import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section([^>]*)>', text)
for s in sections:
    id_m = re.search(r'id=["\']([^"\']*)["\']', s)
    cls_m = re.search(r'class=["\']([^"\']*)["\']', s)
    print(f"id={id_m.group(1) if id_m else 'none'} | class={cls_m.group(1) if cls_m else 'none'}")
