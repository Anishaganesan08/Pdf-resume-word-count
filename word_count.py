#!/usr/bin/env python
# coding: utf-8


# In[ ]:





# In[3]:

#the PyPDF2 is a python library for working with PDF documents
get_ipython().system('pip install PyPDF2')


# In[5]:


from PyPDF2 import PdfReader

#reader is used to read the PDF
#PdfReader is used to extract texts,images and other data from PDF documents
reader=PdfReader('/media/Anisha resume final1.pdf')

page=reader.pages[0]

text=page.extract_text()

words=text.split()
print(len(words))


# In[ ]:




