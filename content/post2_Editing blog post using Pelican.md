title: How-to 1.2:  Editing blog post using Pelican.
date: 2020-12-19 22:30
author: Alex

# Instructions about editing blog using Pelican

This post continues the theme of the previous post on that topic. 
<https://thisakcode.github.io/how-to-1-blogging-using-pelican.html>

```bash
cd C:\blog_depend\venv\Scripts
activate
cd c:\thisAKcode.github.io\content
```
## Edit existing file 
If I am interested in editing published post I do it as follows:
I had post_number_n.md in content folder, then I opened it using some editor and rewrited some of the content.  

```bash
pelican content -o output -s publishconf.py
ghp-import -m "Generate Pelican site" --no-jekyll -b main output
git push origin main
git add content
git commit -m "added a post"
git push origin content
```
[IMPORTANT] Sometimes I run into trouble that `git push origin main` is not working properly. 

## Convert Jupyter Notebook to md and publish that as an article
Alternative for writing from scratch can be converting of an ipynb file into markdown file. Read HOWTO below to understand how to work with that stuff.

HOWTO
<https://github.com/jupyter/nbconvert>
from within cmder I run this:

```bash
jupyter nbconvert --to markdown notebook.ipynb
```

# Edit Site Configuration
To change some defaults from first setup you have to modify some of the variables in `pelicanconf.py` file.  

# Modify site theme
Create a new directory in `C:\thisAKcode.github.io` named `theme` in which you need to have `templates` directory.  Here Jinja2 to be stored if your goal is to override the default theme.

1. Choose Pelican theme you like here: <http://www.pelicanthemes.com/>.
2. Clone the repo of your favorite theme e.g. `https://github.com/getpelican/pelican-themes/tree/master/basic`
Clone the into this location: `C:\blog_depend\venv\Lib\site-packages\pelican\themes`
otherwise use this tool `https://kinolien.github.io/gitzip/`.


and register it inside your pelicanconf.py
`THEME = "elegant"` 
3. Now open pelicanconf.py file present in the Main Project folder and insert below line:
`THEME=’<path to your Theme Folder>’`

Your Pelican is ready to use the theme.

# Add search engine and add a comment plugin.
I found this great article <https://snipcart.com/blog/pelican-blog-tutorial-search-comments>. This walks through creating blog from scratch inclusive two features:
1. adding search engine.
2. adding comments.

# Adding a search engine.
## Pelican-specific search plugin "Tipue search" 

Tipue-search is one of the plugins:
<https://github.com/getpelican/pelican-plugins/tree/master/tipue_search>

Wasnt able to set it up. 
Istall requirements `pip install beautifulsoup4`.




