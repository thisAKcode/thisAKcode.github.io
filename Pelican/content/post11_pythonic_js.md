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
### Python dictionary compared to JS object
While syntax differs, Python dict share some similarities with JS object.
When assigning 
```js 
let dict0 = {
  'x': 1,
  'y':2,
  'z':3
}

dict0['x'] = 999;  // reassign new val to 'x'
delete dict0['z']; // delete item with key 'z'
```
Same thing in python is achived as follows:
```python
dict0 = {
    'x': 1,
    'y':2,
    'z':3
}

dict0['x'] = 999
del dict0['z']
```

### Small pieces 
1. f strings are like template literals.
```js
var name = 'Alex Kupiakov';
var message = `Hi ${name.split(' ')[0]}`;
/* python
name = 'Alex Kupiakov'
message = f"Hi {name.split(' ')[0]}"
*/
```
2. indexing string 
```js 
let lastChar = 'Alex'.slice(-1)  // python: last_char = 'Alex'[-1]
```
ressources 
<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>
<https://realpython.com/python-vs-javascript/>
