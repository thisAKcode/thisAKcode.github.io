title: Configure Custom Domain
date: 2021-03-01 11:09
author: Alex

# Set a custom domain for my GitHub Pages site

I have pelican powered static site and world can acces it at my github pages : `thisAKcode.github.io`.  
What if I want to be a fancy and get my own custom domain name and assign it to my GitHub Pages website.


I purchased a domain name from Route 53 by aws and gave it name: `www.prettylagom.me`

I followed those steps to set it up properly:
<steps_to_setup_custom_domain>

Go to your-user-name.github.io.
`cd C:\thisAKcode.github.io`
Create file there you want to hold CNAME (Canonical Name).
`touch CNAME`
 Open CNAME in editor.
`vi CNAME`
Add your custom domain inside CNAME
`www.prettylagom.me`
Run git commands to push this file to remote. 
