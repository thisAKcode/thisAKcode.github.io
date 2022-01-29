title: May JS be understood through Python
date: 2022-01-29 23:00
author: Alex

#  How I Learn JS 

### Shrotly about problem

I once read a great article about JavaScript on realpython.com 
While learning JS you often think about how this portion of JS code could be written in Python. So I decided to white chunks that are comparable.

### some focus on itertools among others
[IMPORTANT!] BEWARE THE FOLLOWING LINES IN QUOTES ARE CUT FROM CODECADEMY.COM!!!
'''
.forEach() is used to execute the same code on every element in an array but does not change the array and returns undefined.
.map() executes the same code on every element in an array and returns a new array with the updated elements.
.filter() checks every element in an array to see if it meets certain criteria and returns a new array with the elements that return truthy for the criteria.
.findIndex() returns the index of the first element of an array that satisfies a condition in the callback function. It returns -1 if none of the elements in the array satisfies the condition.
.reduce() iterates through an array and takes the values of the elements and returns a single value.
All iterator methods take a callback function, which can be a pre-defined function, a function expression, or an arrow function.
'''

### If you want to play with JS
Install node.js and enjoy this awesome tool which feels like Python interpreter but for JavaScript.

### snippet 1:
```python

import itertools
```
same in js 
```js
// lala
```
### f strings are like template literals
```js
var name = 'Alex Kupiakov';
var message = `Hi ${name.split(' ')[0]}`;

```

ressources 
<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>
<https://realpython.com/python-vs-javascript/>