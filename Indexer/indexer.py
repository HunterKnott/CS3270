'''Hunter Knott, CS 3270, Utah Valley University'''
import os
import sys
import webbrowser
import urllib.parse

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

page_end = """
</body>
</html>
"""

title_tmplt = """
<h2>
{0}
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
{0}
<br>
{1}
<br>
{2}
</div>
"""

def main():
    if len(sys.argv) > 1:
        current_directory = sys.argv[1]
    else:
        current_directory = os.getcwd()

    html_content = page_start
    for item in os.scandir(current_directory):
        if item.is_file() and item.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            img_info = img_tmplt.format(item.path, item.name, item.stat().st_size)
            html_content += img_info
        else:
            link_info = link_tmplt.format(item.path, item.name)
            html_content += link_info
    html_content += page_end

    with open('display.html', 'w') as html_file:
        html_file.write(html_content)
    
    webbrowser.open('display.html', new=2)

    # Regular Expressions may be used for exif data

if __name__ == '__main__':
    main()