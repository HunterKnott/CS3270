'''Hunter Knott, CS 3270, Utah Valley University'''
import os
import sys
import webbrowser

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
{0}
<br>
{1}
<br>
{2}
</div>
"""

def make_html(directory):
    html_content = page_start
    dir_sec = dir_section
    img_sec = img_section
    html_content += title_tmplt.format(directory)
    for item in os.scandir(directory):
        if item.is_dir():
            link_info = link_tmplt.format(item.path, item.name)
            dir_sec += link_info
        elif item.is_file() and item.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            img_info = img_tmplt.format(item.path, item.name, item.stat().st_size)
            img_sec += img_info
    html_content += dir_sec + img_sec + page_end

    with open(os.path.join(directory, 'index.html'), 'w') as html_file:
        html_file.write(html_content)
    
    for item in os.scandir(directory):
        if item.is_dir():
            make_html(item.path)

def main():
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()
    
    make_html(root_directory)
    webbrowser.open(os.path.join(root_directory, 'index.html'), new=2)

    # Regular Expressions may be used for exif data

if __name__ == '__main__':
    main()