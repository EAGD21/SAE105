<p>import markdown
import sys</p>
<p>if <strong>name</strong> == '<strong>main</strong>':
    file_in = sys.argv[0]
    file_out = sys.argv[1]
    print(file_in,file_out)
    with open(file_in, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)</p>
<pre><code>with open(file_out, 'w') as f:
    f.write(html)
</code></pre>
<p>def convert():
    with open('file.md', 'r') as f:
        text = f.read()
    html = markdown.markdown(text)</p>
<pre><code>with open('file.html', 'w') as f:
    f.write(html)
</code></pre>
<p>def convert2():
    with open('file2.md', 'r') as f:
        text = f.read()
    html = markdown.markdown(text)</p>
<pre><code>with open('file2.html', 'w') as f:
    f.write(html)
</code></pre>