title: Edit Text Productively in Vim 
date: 2022-08-09 22:22
Authors: Alex



### I would like to learn vim 
I am so frustrated that I don't know all the tricks. In attempt to learn more I try to list some that worked and it felt magic.
I omit some that I already get used to. 

### Editing
After escape do the following.
 `R` enter replace mode.
 `cw`to remove word in front and type new word instead cw. 
 `xp` transpose two letters. 

### SEarch and replace 
 `:%s/foo/bar/g` search and replace pattern 'foo' in an entire file with 'bar'
 `:%s/foo//g` search and replace pattern 'foo' in an entire file with ''