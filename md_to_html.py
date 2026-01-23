import markdown
import sys

if __name__ == '__main__':
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    with open(file_in, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)

    with open(file_out, 'w') as f:
        f.write(html)

def convert(name_file):
    with open(name_file.md, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)

    with open(name_file.html, 'w') as f:
        f.write(html)