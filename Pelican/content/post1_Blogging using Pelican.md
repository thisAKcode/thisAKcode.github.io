title: How-to 1:  Blogging using Pelican.
date: 2020-03-21 22:22
Authors: Alex



### Create a blog on GitHub Pages with Pelican
Steps to follow in order to publish the first page on my blog using static site generator - Pelican.
This very first page took me many attempts and hours before I got this to work. The post you read is actually my second page on that blog and the second attempt to publish pages. If you are new to Pelican, this article is for you.

I use windows everything was done by typing commands in Cmder <https://cmder.net/>

### Steps: 
+ venv setup 
+ installing dependencies
+ creating github pages repo 
+ pelican-quickstart
+ push pelican genereated files to repo
+ writing content on local machine
+ Run Pelican and ghp-import in order to format content as html
+ Publish

### Venv Setup
```bash
cd c:\blog_depend
python -m venv venv
venv\Scripts\activate
```
### Installing pelican, Markdown and ghp-import
```bash
$ pip install pelican ghp-import Markdown
```
### Create github pages repo

Sign in to github.com, click create a repo, give it a name thisAKcode.github.io
I left this repo empty, which is fine for that usecase.
Clone your empty Git repository to your local macine
```
$ git clone https://github.com/thisAKcode/thisAKcode.github.io c:\
```

### Run `pelican-quickstart`.

While venv activates launch pelican-quickstart
```
pelican-quickstart
```
After a set of questions, Pelican creates a bunch of files in current directory. Pelican documentation is well written. Of course you need to read the docs to understand that step... <https://docs.getpelican.com/en/stable/>

### Add Pelican setup files to repo.

Add all the Pelican-generated files to master branch of the local Git repo.
Commit and push the local changes to the remote by default master branch.
```bash
git add .
git commit -m 'initial pelican commit to content'
git push origin content
```
##### Note on User pages 
For user pages (pages hosted in repos named username.github.io), the content is served from the master branch.
I found it very convenient to go with the following approach as per tip from official documentation. <https://docs.getpelican.com/en/latest/tips.html#user-pages>
> "For example, your main project folder is thisAKcode.github.io and you can create the Pelican project in a subdirectory called Pelican. Then from inside the Pelican folder you can run: `$ pelican content -o .. -s pelicanconf.py`"

So now you just execute the following:
```bash
mkdir Pelican\content
cd Pelican\content
mkdir pages images
cp 'c:\Users\Aleks\Pictures\profile.jpg' images
touch first-post.md
touch pages/about.md
```

### Writing content 'about.md' and 'first-post.md'
first-post.md and about.md  has been created. Open and edit files using your favorite code editor which is done using markdown syntax.

### Run Pelican 
Once content of first article is written, run Pelican to generate the static HTML files in root folder of the project.

```bash
cd Pelican\content
pelican content -o .. -s pelicanconf.py
```
### Push Pelican-created html files to master branch of the repo
Push content to remote.
```
git add
git commit -m "ok"                                                    
git push origin master
```    
Your very own blog is available at `thisAKcode.github.io`! 

# Sources:
+ <https://docs.getpelican.com/en/3.0/getting_started.html>
+ <https://opensource.com/article/19/5/run-your-blog-github-pages-python>