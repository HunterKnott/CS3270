'''Hunter Knott, CS 3270, Utah Valley University'''
import os
import sys
import webbrowser
import http.server
import socketserver
import exifread
import geo

page_start = """
<html>
<head>
<style>
.dirlink_el {font-size: 125%;}
.sm_img {max-height: 200px; max-width: 200px;}
.img_container {
  display: flex;  /* Use Flexbox for side-by-side layout */
  align-items: center;  /* Vertically center the content in the containers */
}
.img_el {
  padding-right: 10px;
}
</style>
</head>
<body>
"""

dir_section = """
<div>
"""

img_section = """
</div>
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
<a href="{0}">{0}</a>
</div>
"""

img_tmplt = """
<div class="img_el">
  <a href={0}><img src="{0}" class="sm_img"></a>
  <p>
    {0}
    {1}
  </p>
</div>
"""

class DirectoryViewer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

# Generates HTML index files for directory and subdirectories
def make_html(directory):
    html_content = page_start
    dir_sec = dir_section
    img_sec = img_section
    html_content += title_tmplt.format(directory)

    # Determines if directory item is a subdirectory or an image to process
    for item in os.scandir(directory):
        if item.is_dir():
            link_info = link_tmplt.format(item.name)
            dir_sec += link_info
        elif item.is_file() and item.name.endswith((".jpg", ".jpeg", ".png", ".gif", ".JPG", ".JPEG")):
            exif_data = get_exif_data(item)
            exif_info = f"{exif_data[0]}<br>"
            if exif_data[1] in ["N", "S", "E", "W"]:
                location_string = geo.main((exif_data[2], exif_data[1]), (exif_data[4], exif_data[3]))
                exif_info += f"{location_string}"
            img_info = img_tmplt.format(item.name, exif_info)
            img_sec += img_info

    html_content += dir_sec + img_sec + page_end

    with open(os.path.join(directory, "index.html"), "w") as html_file:
        html_file.write(html_content)

# Retrieves exif info from an image file for processing
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

# Takes a command line argument to determine file path to generate
def main():
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = os.getcwd()

    os.chdir(root_directory)
    make_html(root_directory)

    # Opens a page in the browser to display the generated HTML
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

if __name__ == "__main__":
    main()