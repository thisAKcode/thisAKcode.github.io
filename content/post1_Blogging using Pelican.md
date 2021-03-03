title: How-to 1:  Blogging using Pelican.
date: 2020-03-21 22:22
Tags: Pelican, static site, markdown
Authors: Alex
Summary: Steps to follow in order to publish the first page on my blog using static site generator -Pelican.

## Create a blog on GitHub Pages with Pelican
This very first page took me many attempts and hours before I got this to work. The post you read is actually my second page on that blog and the second attempt to publish pages. If you are new to Pelican, that is for you. My post was inpsired by the great article by  Erik O'Shaughnessy. [Run your blog on GitHub Pages with Python][1]
[1]: https://opensource.com/article/19/5/run-your-blog-github-pages-python

## Everything in that howto were done using Cmder <https://cmder.net/>

# Steps: 
+ venv setup 
+ installing dependencies
+ creating github pages repo 
+ pelican-quickstart
+ push pelican genereated files to repo
+ writing content on local machine
+ Run Pelican and ghp-import in order to format content as html
+ Publish

# Step one: venv setup

    # create venv
    $ python -m virtualenv 'c:\blog_depend'
    # activate venv (notice 'c'  lowercased in path)
    $ cd 'c:\blog_depend\venv\Scripts'
    $. activate

# Step two: Installing pelican, Markdown and ghp-import into venv

    $ pip install pelican ghp-import Markdown
    # activate venv again
    $ cd 'c:\blog_depend\venv\Scripts'
    $ . activate

# Step three: creating github pages repo

    # create github repo on github.io
    # go to github.com, click on create a repo, create a repo named username.github.io

Github instructon apears. I ignore them. <br />
I left my repo empty, which is fine for that usecase. <br />
	
    # clone your empty Git repository to your local machine
    $ git clone https://github.com/thisAKcode/thisAKcode.github.io 'c:\blog_v2'
    # cd out of pwd back to your project folder e.g. to blog  directory
    $ cd 'c:\blog_v2'

# A tip from Erik O'Shaughnessy 
"...For user pages (pages hosted in repos named username.github.io), the content is 
served from the master branch.
I strongly prefer not to keep all the Pelican configuration files and raw Markdown 
files in master, rather just the web content. So I keep the Pelican configuration 
and the raw content in a separate branch I like to call content. (You can call it 
whatever you want, but the following instructions will call it content.) I like 
	this structure since I can throw away all the files in master and re-populate it 
	with the content branch." [Run your blog on GitHub Pages with Python][1]<br />
	[1]: https://opensource.com/article/19/5/run-your-blog-github-pages-python

    # Separate content from the output	
    # Following command both creates the brach 'content' and check out(goes) to that branch
    $ git checkout -b content
    # Switched to a new branch 'content' 

# Step four : pelican-quickstart

    # launch pelican-quickstart
    $ pelican-quickstart
    # After a set of questions, Pelican creates a bunch of files in current directory
    # Of course you need to read the docs to understand that step... <https://docs.getpelican.com/en/stable/>

# Step five: add files to repo.

    # Add all the Pelican-generated files to the content branch of the local Git repo.
    # While on content branch, commit and push the local changes to the remote to content branch:
    $ git add .
    $ git commit -m 'initial pelican commit to content'
    $ git push origin content

# Step six: Writing about.md and first-post.md

    $ cd content
    $ mkdir pages images
    # copy picture from location on \c\ into images
    $ cp 'c:\Users\Aleks\Pictures\profile.jpg' images
    $ touch first-post.md
    $ touch pages/about.md
    # first-post.md and about.md  has been created. Open and edit files using your favorite code editor.

# Step seven: Run Pelican and ghp-import

    # change dir to one containing publishconf.py
    $ cd 'c:\blog_v2'
    # Run Pelican to generate the static HTML files in output folder of project:
    $ pelican content -o output -s publishconf.py

\# Something happend while running Pelican. This was because Iforced it run script to convert <br>
\# unproperly formatted path inside first-post.md into html: <br>

    tips : use \blog_folder\etcetera formatting to format path to files. otherwise you get
    WARNING: Cannot get modification stamp. The filename, directory name, or volume label syntax is incorrect:
    CRITICAL: OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect:

    # run ghp-import ( stands for GitHub-pages)
    $ ghp-import -m "Generate Pelican site" --no-jekyll -b master output

#  Step eight:Push Pelican-created html files to master branch of the repo

    $ git push origin master

    # push content to the content branch
    $ git add content
    $ git commit -m 'added a first post, a photo and an about page'
    $ git push origin content
    
# Your new project is available at `thisAKcode.github.io`


# Main Project folder file and directory tree.
```
C:.
¦   Makefile
¦   pelicanconf.py
¦   publishconf.py
¦   README.md
¦   tasks.py
¦   
+---content
¦   ¦   d2_post.md
¦   ¦   fifth-post.md
¦   ¦   first-post.md
¦   ¦   second-post.md
¦   ¦   tsd892_main.ipynb
¦   ¦   tsd892_main.md
¦   ¦   
¦   +---images
¦   ¦       profile.jpg
¦   ¦       
¦   +---pages
¦   ¦       about.md
¦   ¦       
¦   +---tsd892_main_files
¦           tsd892_main_2_0.png
¦           tsd892_main_2_1.png
¦           tsd892_main_2_2.png
¦           tsd892_main_2_3.png
¦           tsd892_main_2_4.png
¦           tsd892_main_2_5.png
¦           
+---output
¦   ¦   archives.html
¦   ¦   authors.html
¦   ¦   categories.html
¦   ¦   fme-pythoncaller-combo.html
¦   ¦   hello-world.html
¦   ¦   how-to-1-blogging-using-pelican.html
¦   ¦   how-to-12-editing-blog-post-using-pelican.html
¦   ¦   index.html
¦   ¦   md-converted-thing.html
¦   ¦   tags.html
¦   ¦   
¦   +---author
¦   ¦       alex.html
¦   ¦       
¦   +---category
¦   ¦       misc.html
¦   ¦       
¦   +---feeds
¦   ¦       all.atom.xml
¦   ¦       misc.atom.xml
¦   ¦       
¦   +---images
¦   ¦       profile.jpg
¦   ¦       
¦   +---pages
¦   ¦       about.html
¦   ¦       
¦   +---theme
¦       +---css
¦       ¦       fonts.css
¦       ¦       main.css
¦       ¦       pygment.css
¦       ¦       reset.css
¦       ¦       typogrify.css
¦       ¦       wide.css
¦       ¦       
¦       +---fonts
¦       ¦       font.css
¦       ¦       Yanone_Kaffeesatz_400.eot
¦       ¦       Yanone_Kaffeesatz_400.svg
¦       ¦       Yanone_Kaffeesatz_400.ttf
¦       ¦       Yanone_Kaffeesatz_400.woff
¦       ¦       Yanone_Kaffeesatz_400.woff2
¦       ¦       
¦       +---images
¦           +---icons
¦                   aboutme.png
¦                   bitbucket.png
¦                   delicious.png
¦                   facebook.png
¦                   github.png
¦                   gitorious.png
¦                   gittip.png
¦                   google-groups.png
¦                   google-plus.png
¦                   hackernews.png
¦                   lastfm.png
¦                   linkedin.png
¦                   reddit.png
¦                   rss.png
¦                   slideshare.png
¦                   speakerdeck.png
¦                   stackoverflow.png
¦                   twitter.png
¦                   vimeo.png
¦                   youtube.png
¦                   
+---__pycache__
        pelicanconf.cpython-37.pyc
        publishconf.cpython-37.pyc
```

# Sources:
+ <https://docs.getpelican.com/en/3.0/getting_started.html>
+ <https://opensource.com/article/19/5/run-your-blog-github-pages-python>