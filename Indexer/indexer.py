'''Hunter Knott, CS 3270, Utah Valley University'''
import os
import sys
import webbrowser
import http.server
import socketserver

page_start = """
<html>
<head>
<style>
.dirlink_el {font-size: 125%;}
.sm_img {max-height: 200px; max-width: 200px;}
.img_el {display: inline-block; padding-bottom: 15px; padding-right: 10px;}
</style>
</head>
<body>
"""

dir_section = """
<div>
"""

img_section = """
</div>
<br>
<div>
"""

page_end = """
</div>
</body>
</html>
"""

title_tmplt = """
<h2>
Current Directory: {0}
</h2>
"""

link_tmplt = """
<div class="dirlink_el">
<a href="{0}">{1}</a>
</div>
"""

img_tmplt = """
<div class="img_el">
<a href={0}><img src="{0}" class="sm_img"></a>
<br>
{1}
<br>
{2}
</div>
"""

PORT = 8000  # You can choose any available port

class DirectoryViewer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

def make_html(directory):
    html_content = page_start
    dir_sec = dir_section
    img_sec = img_section
    html_content += title_tmplt.format(directory)
    for item in os.scandir(directory):
        if item.is_dir():
            link_info = link_tmplt.format(item.name, item.name)
            dir_sec += link_info
        elif item.is_file() and item.name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG', '.JPEG')):
            img_info = img_tmplt.format(item.name, item.name, item.stat().st_size)
            img_sec += img_info
    html_content += dir_sec + img_sec + page_end

    with open(os.path.join(directory, 'index.html'), 'w') as html_file:
        html_file.write(html_content)

def main():
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()

    os.chdir(root_directory)
    
    make_html(root_directory)

    with socketserver.TCPServer(("", PORT), DirectoryViewer) as httpd:
        print(f"Serving at port {PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    main()