
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
