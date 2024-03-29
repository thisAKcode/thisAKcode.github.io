title: May JS be understood through Python
date: 2022-01-29 23:00
author: Alex

#  How I Learn JS 
* codecademy.com
* 100 days of web with Python

### Shrotly about problem

I once read a great article about JavaScript on realpython.com 
While learning JS you often think about how this portion of JS code could be written in Python. So I decided to white chunks that are comparable.
### some focus on itertools among others
[IMPORTANT!] BEWARE THE FOLLOWING LINES IN QUOTES ARE CUT FROM CODECADEMY.COM!!!
'''
>.forEach() is used to execute the same code on every element in an array but does not change the array and returns undefined.
.map() executes the same code on every element in an array and returns a new array with the updated elements.
.filter() checks every element in an array to see if it meets certain criteria and returns a new array with the elements that return truthy for the criteria.
.findIndex() returns the index of the first element of an array that satisfies a condition in the callback function. It returns -1 if none of the elements in the array satisfies the condition.
.reduce() iterates through an array and takes the values of the elements and returns a single value.
All iterator methods take a callback function, which can be a pre-defined function, a function expression, or an arrow function.
'''

### If you want to play with JS
Install node.js and enjoy this awesome tool which ressembles Python interpreter.

### Filter out items from sequence based on condition
```python
letter_sequence = [
  'a', 'b', 'c',
  'd', 'e', 'f',
  'g'
]
unnecessary_letters =  ['e', 'f', 'g' ]
shorter_sequence = [i for i in letter_sequence 
    if i not in unnecessary_letters]
print(shorter_sequence)

```
Same in js 
```js
//
letterSequence = [
  'a', 'b', 'c',
  'd', 'e', 'f',
  'g'
]
let unnecessaryLetters = ['e', 'f', 'g' ];
let shorterSequence = letterSequence.filter(letter => {return !unnecessaryLetters.includes(letter)})
console.log(shorterSequence); // [ 'a', 'b', 'c', 'd' ]
```
### create JavaScript object / Python dictionary to count words
```js
let story = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl tincidunt eget nullam non. Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Volutpat odio facilisis mauris sit amet massa. Commodo odio aenean sed adipiscing diam donec adipiscing tristique. Mi eget mauris pharetra et. Non tellus orci ac auctor augue. Elit at imperdiet dui accumsan sit. Ornare arcu dui vivamus arcu felis. Egestas integer eget aliquet nibh praesent. In hac habitasse platea dictumst quisque sagittis purus. Pulvinar elementum integer enim neque volutpat ac.';
let loremWords = story.split(' ');
let overusedWords = ['lorem', 'ipsum', 'dolor'];

const getWordCount = (loremWords, overusedWords) => {word_cnt = {};
  for (let i = 0; i <overusedWords.length; i++){
  console.log('Word ' + i + overusedWords[i]);
  const occurences = betterWords.filter(word => word === overusedWords[i]);
  word_cnt[overusedWords[i]] = occurences.length;
  };
  return word_cnt;
};
const wordCount = getWordCount(loremWords, overusedWords)
console.log(wordCount)
```
Same result can be achived in Python as follows:
```python
from collections import Counter
story = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl tincidunt eget nullam non. Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Volutpat odio facilisis mauris sit amet massa. Commodo odio aenean sed adipiscing diam donec adipiscing tristique. Mi eget mauris pharetra et. Non tellus orci ac auctor augue. Elit at imperdiet dui accumsan sit. Ornare arcu dui vivamus arcu felis. Egestas integer eget aliquet nibh praesent. In hac habitasse platea dictumst quisque sagittis purus. Pulvinar elementum integer enim neque volutpat ac.'
overusedWords = ['lorem', 'ipsum', 'dolor']
c = Counter(story.split(' '))
word_count = {c[over_word]: overword 
              for over_word in overusedWords}

```
### All or Any 
In JavaScript to check wheter at least one element passes some condition `.some()` method is used on array.

```js
const lorem = ['lorem', 'ipsum', 'dolor', 'sit', 'amet'];
let _every = lorem.every(token => token.length < 5);
let _some = lorem.some(token => token.length < 5);
```
In python this might be achieved by using list comprehension with  `all()`, `any()`.
```python 
lorem = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
_every = all([len(i) < 5 for i in lorem])
_some = any([len(i) < 5 for i in lorem])
```
### Python dictionary compared to non-advanced JS object
Python dict share some similarities with JS object. It is true when javascript objects key-value pair is not a function but simple items representing key-value pairs separated by comma and being surrounded by curly braces.
```js 
let dict0 = {
  'x': 1,
  'y': 2,
  'z': 3
}
for (const [key, value] of Object.entries(dict0)) {
  console.log(`${key}: ${value}`);
}
// Grab all entries as array of [key, value] pairs
const dict0Entries = Object.entries(robot);
// Grab property names
const dict0Keys = Object.keys(dict0);
dict0['x'] = 999;  // reassign new val to 'x'
delete dict0['z']; // delete item with key 'z'
```
Same functionality in python is achieved as follows:
```python
dict0 = {
    'x': 1,
    'y':2,
    'z':3
}
for key, value in dicto.items():
    print(f'{key}: {value}')
dict0_entries = dict0.items()
dict0_keys = dict0.keys()
dict0['x'] = 999
del dict0['z']
```

### Looping Through Objects 
Let's iterate through the band.members sample object simply printing some of it's properties.
```javascript
let band = {
    members: {
    'first guy': { 
        name: 'John', 
        instrument: 'guitar', 
        startSinging() { console.log('Let it be, ') } 
        },
    'second guy': { 
        name: 'Paul', 
        instrument: 'bass guitar', 
        continueSinging() { console.log('let it be, let it be, ') } 
        },
    'third guy': { 
        name: 'George', 
        instrument: 'sitar', 
        singingStill() { console.log(`yeah, `) } },
    'fourth guy': {
        name: 'Ringo', 
        instrument: 'drums', 
        alsoSing() { console.log('let it be!') } 
        }
    }
}; 
```

for (let bandMember in band.members) {
  console.log(`${band.members[bandMember].name}: ${band.members[bandMember].instrument}`)
};

### Looping pairwise
Here you can compare js and Python solution which both rely on quotient of division between item and 2:
```js
let arr1 = [ 1, 2, 3, 4, 5, 6, 7, 8]
let arr2 = []
for (let i=0; i<arr1.length; i++){
      arr2.push(Math.floor((arr1[i]-1)/2))}
// [0, 0, 1, 1, 2, 2, 3, 3]
```
Python
```python
y = [1,2,3,4,5,6,7,8]
yy = [(i-1)//2  for i in y]
```
### Functions 
Simple function with default arguments is defined as follows in js:
```js
function remindMe(i1='Python', i2='JavaScript', i3='SQL'){
  console.log(`Remember to learn ${i1}`);
  console.log(`Remember to learn ${i2}`);
  console.log(`Remember to learn ${i3}`);
}
```
Same thing in Python looks like that:

```python
def remind_me(i1 = "Python", i2 = "JavaScript", i3 = "SQL"):
   print(f'Remember to learn {i1}')
   print(f'Remember to learn {i2}')
   print(f'Remember to learn {i3}')
```
### Small pieces 
F strings are like template literals.
```js
var name = 'Alex Kupiakov';
var message = `Hi ${name.split(' ')[0]}`;
/* python
name = 'Alex Kupiakov'
message = f"Hi {name.split(' ')[0]}"
*/
```
Indexing string 
```js 
let lastChar = 'Alex'.slice(-1)  // python: last_char = 'Alex'[-1]
```
Random numbers in JS.
There are a few ways to get a random value using random().

```js
random() //  a value between 0 and 1.
random(max) //  a value between 0 and max value (excluding the max).
random(min, max) //  a value between min value and max value (excluding the max).
```
In python you random() function should be imported from built-ins.
``` pyhton
import random

random.random() # generate a float random number less than 1 and greater or equal to 0.
random.uniform(5,10) #  random floating number in range
```
### Pandas equivalent in JS
Danfo.js is a library that was inpired by pandas


### .map() in JS and in Python
Map is the function applied to each item of given iterable returnin another processed iterator. 
```python

numbers = (1, 2, 3)

# using function
def x_plus_x():
    return x + x

result = map(x_plus_x, numbers)

# using lambda 
result = map(lambda x: x + x, numbers)

```


ressources 
<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>
<https://realpython.com/python-vs-javascript/>
