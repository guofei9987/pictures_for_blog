# 层级格式转换：markdown 的列表，转 html 格式的 ul/li ，并满足 litree 格式


file = '西方哲学.md'

content_html = ['<ul class="litree">',
                '<li>']
with open(file, 'r') as f:
    md = f.readlines()

# %%
last_level = now_level = 0
for line in md:
    # TODO:这里应当考虑有换行的情况
    now_level = line.find('- ') / 4
    lin = line.strip().replace('- ', '')
    assert now_level % 1 == 0

    if now_level > last_level:
        content_html.append('<ul>')
        content_html.append('<li>')
        content_html.append('<div{}>{}</div>'.format(' class="sticky"' if now_level <= 1 else '', lin))

    while now_level < last_level:
        content_html.append('</li>')
        content_html.append('</ul>')
        last_level -= 1

    if now_level == last_level:
        content_html.append('</li>')
        content_html.append('<li>')
        content_html.append('<div{}>{}</div>'.format(' class="sticky"' if now_level <= 1 else '', lin))

    last_level = now_level

content_html.append('</li>')

for _ in range(int(last_level)):
    content_html.append('</ul>')
    content_html.append('</li>')

content_html.append('</ul>')

# %%

with open(file + '.html', 'w') as f:
    f.write('\n'.join(content_html))
