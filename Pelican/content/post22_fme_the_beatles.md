title: Wrangling the Beatles song writing using Python in FME(Safe Software)
date: 2022-01-01 22:22
Authors: Alex



### Take a look at the input
I will use Python Caller to manipulate attributes in FME and as input I want to take data that make sense to me: the Beatles!

Below you se my input that I pulled from here: <https://ultimateclassicrock.com/who-wrote-the-most-beatles-songs/> 

```

| Song title                     | George Harrison  | John Lennon  | Paul McCartney  | Ringo Starr  |
|--------------------------------|------------------|--------------|-----------------|--------------|
| "Please Please Me"             |                  | 1            |                 |              |
| "Love Me Do"                   |                  |              | 1               |              |
| "Strawberry Fields Forever"    |                  | 1            |                 |              |
| "Octopus' Garden"              | 1                |              |                 | 1            |
| "Don't Pass Me By"             |                  |              |                 | 1            |
| "While My Guitar Gently Weeps" | 1                |              |                 |              |
| "I Want to Hold Your Hand      |                  | 1            | 1               |              |
```

First I use PythonCreator to instantiate FME objects that I then will be able to manipulate:

```
attr_names = ['Song title', 'George Harrison', 'John Lennon', 'Paul McCartney', 'Ringo Starr']
data_raw = '''"Please Please Me", None, 1, None, None
"Love Me Do", None, None, 1,None
"Strawberry Fields Forever", None, 1, None, None
"Octopus' Garden", 1,None, None, 1
"Don't Pass Me By", None, None, None, 1
"While My Guitar Gently Weeps", 1, None, None, None
"I Want to Hold Your Hand, None, 1,1, None'''

data_clean = [[ii 
          for ii in i.split(',')
          ] 
          for i in data_raw.split('\n')]
```

```python
where_beatles = r'C:\thisAKcode.github.io\Pelican\content\other\beatles_auth.csv'

```