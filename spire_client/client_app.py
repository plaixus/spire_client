#!/usr/bin/env python
# coding: utf-8

# In[10]:


import urllib3
import json

global SPIRE_URL
SPIRE_URL = 'http://spire-server.ros:5000'


# In[11]:


def record(filename, topics, duration=None):
    #filename = input('Enter the name of the bagfile: ')
    #topics = input('Enter a list of topic names, comma separated: ')
    topic_list = topics.split(',')
    req_json = json.dumps({'bagfile': filename, 'topics': topic_list, 
                           'duration': duration})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/record", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[23]:


def play(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/play", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[15]:


def info(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('GET', f"{SPIRE_URL}/info", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[63]:


def download(filename):
    #filename = input('Enter the name of the bagfile: ')
    http = urllib3.PoolManager()
    r = http.request('GET', f"{SPIRE_URL}/record/{filename}", headers={'Content-Type': 'application/json'})
    with open(f'{filename.split(".")[0]}_bag.csv', 'wb') as out:
        out.write(r.data)


# In[ ]:


def get_dataset(filename):
    #filename = input('Enter the name of the bagfile: ')
    http = urllib3.PoolManager()
    r = http.request('GET', f"{SPIRE_URL}/dataset/{filename}", headers={'Content-Type': 'application/json'})
    with open(f'{filename.split(".")[0]}_bag.zip', 'wb') as out:
        out.write(r.data)


# In[41]:


def rosbag_list():
    http = urllib3.PoolManager()
    r = http.request('GET', f"{SPIRE_URL}/index", headers={'Content-Type': 'application/json'})
    print(r.data.decode())


# In[25]:


def compress(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/compress", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[27]:


def decompress(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/decompress", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[29]:


def reindex(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/reindex", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[31]:


def check(filename):
    #filename = input('Enter the name of the bagfile: ')
    req_json = json.dumps({'bagfile': filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/check", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[35]:


def rosbag_filter(filename, out_filename, topic):
    #filename = input('Enter the name of the bagfile to be filtered: ')
    #out_filename = input('Enter the name of the filtered output bagfile: ')
    #topic = input('Enter the topic you want to filter from the bag: ')
    req_json = json.dumps({'bagfile': filename, 'topic': topic, 'output_file': out_filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/filter", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)


# In[72]:


def fix(filename, out_filename):
    #filename = input('Enter the name of the bagfile to be fixed: ')
    #out_filename = input('Enter the name of the fixed output bagfile: ')
    req_json = json.dumps({'bagfile': filename, 'output_file': out_filename})
    http = urllib3.PoolManager()
    r = http.request('POST', f"{SPIRE_URL}/fix", headers={'Content-Type': 'application/json'}, body=req_json)
    print(r.data)

