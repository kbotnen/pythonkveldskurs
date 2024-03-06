#!/usr/bin/env python
# coding: utf-8

# ## Python turtle
# Hva er python turtle, hvorfor python turtle?

# In[ ]:


""" Draw a square.
from turtle import *

speed(2)
shape("turtle")

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
"""


# In[ ]:


""" Draw a pyramid.
from turtle import *

speed(2)
shape("turtle")

forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)
"""


# In[ ]:


""" Draw a colorfull pyramid.
from turtle import *

speed(2)
shape("turtle")

pensize(10)
pencolor("red")
forward(100)
right(120)
pencolor("blue")
forward(100)
right(120)
pencolor("green")
forward(100)
right(120)
"""


# In[ ]:


""" Excercise: Draw a square with for loop.
"""


# In[ ]:


""" Excercise: Draw a square with for loop.
Excercise solution: The code below.
from turtle import *

speed(2)
shape("turtle")

for count in range(4):
    forward(100)
    right(90)
"""


# In[ ]:


""" Draw a square with for loop and variables.
from turtle import *

speed(2)
shape("turtle")

sides = 4
length = 100
angle = 90
for count in range(sides):
    forward(length)
    right(angle)
"""


# In[ ]:


""" Excercise: Draw a pentagon."""


# In[ ]:


""" Excercise: Draw a pentagon.
Exercise solution. The code below.
from turtle import *

speed(2)
shape("turtle")

sides = 5
length = 100

angle = 360/sides
for count in range(sides):
    forward(length)
    right(angle)
"""


# In[ ]:


""" Make a polygon function.

from turtle import *

speed(2)
shape("turtle")

def polygon(sides, length):
    angle = 360 / sides

    for count in range(sides):
        forward(length)
        right(angle)

polygon(4, 100)
"""


# In[ ]:


""" Make a polyline function. We dont need to add up to 360 degrees.

from turtle import *

speed(2)
shape("turtle")

def polylines(sides, length, angle):
    for count in range(sides):
        forward(length)
        right(angle)

polylines(5, 100, 144)
"""


# In[ ]:


""" Excercise: Draw a circle using the polylines function."""


# In[ ]:


""" Excercise: Draw a circle using the polylines function.
Exercise solution. The code below.

from turtle import *

speed(15)
shape("turtle")

def polylines(sides, length, angle):
    for count in range(sides):
        forward(length)
        right(angle)

polylines(91, 100, 91)
"""

