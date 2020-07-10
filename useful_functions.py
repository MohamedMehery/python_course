#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def get_file_exit(filename):
    return filename[filename.index('.') + 1]

def rol_dice(num):
    return random.randint(1,num)

