title: Debugging it all
date: 2021-08-11 21:00
author: Alex

# Setting Up for Python >= 3.7

`python -m pdb`
or 
`breakpoint()`
when older python 
`import pdb; pdb.set_trace()`

## Basic commands
l (ll) list lines around breakpoint
p (pp) pretty print
n (ext) statement 
c (ontinue) program
s (tep) into a function
i (nteract) enter REPL
!command (e.g. !help)

## ressources to check 
ipdb <https://pypi.org/project/ipdb/>
debugger commands <https://docs.python.org/3/library/pdb.html#debugger-commands>