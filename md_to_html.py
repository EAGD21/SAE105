import markdown
import sys

def convert():
    with open('file.md', 'r') as f:
        text = f.read()
    html = markdown.markdown(text)

    with open('file.html', 'w') as f:
        f.write(html)

def convert2():
    with open('file2.md', 'r') as f:
        text = f.read()
    html = markdown.markdown(text)

    with open('file2.html', 'w') as f:
        f.write(html)