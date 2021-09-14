title: FME & PythonCaller combo
date: 2020-04-07 21:50
author: Alex

# FME & PythonCaller combo.
The main goal with that article is justify my use of FME as valuable experience for becoming a Python developer. 

## Shortly about FME (Feature Manipulation Engine) 

The main desktop application of Safe Software is FME Workbench. The inteface consist of, among other, canvas. Here user Alex graphically define a translation called a "workspace" wich can be saved for re-use later (fme workspace files on that regard are similar to script files).
<https://docs.safe.com/fme/html/FME_Desktop_Documentation/FME_Coordinate_Systems/!FME_Terminology/terminology.htm>

FME Desktop is like a mindmap: you are using canvas to graphically define a translation with transformers. Transformers are "the building blocks used in FME Workbench, each having a specific function. They can be used alone in a simple workspace, or combined to create complicated processes".

A classical simple workspace looks like that:
picture1


1. Create features (an individual item within the translation) OR read the source dataset (many formats accessible in FME).
2. Directing the items into individual port based on result of evaluation of 'if-elif-else' condition statement > you can then write the items to different files for each resulting port.


## PythonCaller
PythonCaller transformer used to perform tasks within FME, which are not possible with standard FME transformers.
Transformer PythonCaller executes a user-supplied Python script (3.7+) to manipulate features.
<https://knowledge.safe.com/articles/60319/pythoncaller-transformer.html>
PythonCaller can interface with a Python script in two different ways - by a function or by a class.

## Function 

Use the Function Interface when you intend to process a single feature at a time.

### usecase 1 collection.Counter()
Prior to use of PythonCaller you need to accomplish the following:
1. Create some dummy items to use as input for Python function.
2. Add a PythoCaller Transfromer.
3. Inside it make a count of items having some particular attribute value for 'attribute1'. 
4. Output values containing in Counter() object as its own attribute called 'attribute2' counted values.

When you use function to process features, all features will enter the function one by one for processing.

```
# script uses an FME Objects method, collections module
import fme
import fmeobjects 
import collections

def count_list(feature): # function accepts FMEFeature objects as its only argument
    some_var = feature.getAttribute('_list{}')
    cnt_elmnts = collections.Counter(some_var).most_common()
    feature.setAttribute('result', str(cnt_elmnts)) 
    # attribute is added to the feature with setAttribute() method on the feature
```

5. Click OK to dismiss the code editor.

In the same pane, set the Class or Function to Process Feature parameter to the name of the function: timestampFeature. Because we have added a new attribute we can expose it by entering its name in the Attributes to Expose parameter: type in the new attribute name in the Enter Values for Attributes to Expose window.

## Python Classes within PythonCaller.

If you need to process all values of given attribute for a bunch of features then you may need use classes. 

Use the Class Interface for more flexibility. The Class Interface is useful when you want to operate on a group of features together, such as collecting all the features received and then outputting them in a specific sort order. Another common use case is to accumulate all the features, perform an operation on the whole set, and then output all of the features with a calculated value as a new attribute.

You can use Python Classes to accumulate values between features (GIS items)
PythonCaller will output one single feature containing a list attribute. 
Code is from safe community <https://knowledge.safe.com/questions/52168/pythoncaller-all-values-for-each-attribute.html>
```
import fme
import fmeobjects
from collections import Counter

class FeatureProcessor(object):
    def __init__(self):
        self.T1_values = []

    def input(self,feature):
        t1 = feature.getAttribute('T1')
        self.T1_values.append(t1)

    def close(self):
        f = fmeobjects.FMEFeature()
        T1_duplicates = [k for k,v in Counter(self.T1_values).items() if v>1]
        f.setAttribute('T1_duplicates', T1_duplicates)
        self.pyoutput(f)
```
            
If you wish to dig deep then you can find fun reads e.g.
Maybe you can find this article useful. 
<https://www.slideshare.net/DanielaPerri2/when-to-use-python-in-fme>

