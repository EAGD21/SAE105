import markdown
import sys

def convert():
    file_in = sys.argv[0]
    file_out = sys.argv[1]
    with open(file_in, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)

    with open(file_out, 'w') as f:
        f.write(html)