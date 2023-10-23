'''Hunter Knott, CS 3270, Utah Valley University'''
import os
import sys
import webbrowser
import http.server
import socketserver
import exifread
import reverse_geocoder

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

parent_link_tmplt = """
<div class="dirlink_el">
<a href="..">Parent Directory</a>
</div>
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
</div>
<br>
"""

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
            img_info = img_tmplt.format(item.name, item.name)

            exif_data = get_exif_data(item)
            if exif_data:
                exif_info = f"EXIF DateTime: {exif_data[0]}<br>"
                exif_info += f"GPS Latitude Ref: {exif_data[1]}<br>"
                exif_info += f"GPS Latitude: {exif_data[2]}<br>"
                exif_info += f"GPS Longitude Ref: {exif_data[3]}<br>"
                exif_info += f"GPS Longitude: {exif_data[4]}<br>"

                img_info += exif_info

            img_sec += img_info

    html_content += dir_sec + img_sec + page_end

    with open(os.path.join(directory, 'index.html'), 'w') as html_file:
        html_file.write(html_content)

def get_exif_data(image_file):
    exif_data = {}
    exif_tags = ["EXIF DateTimeOriginal", "GPS GPSLatitudeRef", "GPS GPSLatitude", "GPS GPSLongitudeRef", "GPS GPSLongitude"]
    
    with open(image_file, 'rb') as f:
        tags = exifread.process_file(f, details=False)
        for tag in exif_tags:
            if tag in tags:
                exif_data[tag] = str(tags[tag])
    
    exif_tuple = (
        exif_data.get("EXIF DateTimeOriginal", ""),
        exif_data.get("GPS GPSLatitudeRef", ""),
        exif_data.get("GPS GPSLatitude", ""),
        exif_data.get("GPS GPSLongitudeRef", ""),
        exif_data.get("GPS GPSLongitude", "")
    )
    
    return exif_tuple

def main():
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()

    os.chdir(root_directory)
    make_html(root_directory)

    PORT = 8000 
    with socketserver.TCPServer(("", PORT), DirectoryViewer) as httpd:
        print(f"Serving at port {PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print("Server stopped.")

if __name__ == '__main__':
    main()