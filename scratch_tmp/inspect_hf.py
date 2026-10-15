import glob, re

for f in ['index.html', 'booking.html', 'search-results.html', 'contact.html', 'blog.html']:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        header = re.search(r'<header[^>]*>.*?</header>', content, re.DOTALL)
        footer = re.search(r'<footer[^>]*>.*?</footer>', content, re.DOTALL)
        print(f'=== {f} ===')
        if header:
            h_text = header.group(0)
            m = re.search(r'<header[^>]*class=["\']([^"\']*)["\']', h_text)
            print('Header class:', m.group(1) if m else 'none')
            print('Header length:', len(h_text))
            print('Header snippet:\n', h_text[:300])
        else:
            print('No header found')
            
        if footer:
            f_text = footer.group(0)
            m = re.search(r'<footer[^>]*class=["\']([^"\']*)["\']', f_text)
            print('Footer class:', m.group(1) if m else 'none')
            print('Footer length:', len(f_text))
            print('Footer snippet:\n', f_text[:300])
        else:
            print('No footer found')
    except Exception as e:
        print(f'{f}: {e}')
