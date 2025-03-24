#!/usr/bin/env python
# coding: utf-8

# # Import related to FileIO

# In[1]:


import subprocess
import os
import json


# # Configuration related to FileIO

# In[2]:


PATH_TO_STATIC = os.getcwd() + "/Static/"
PATH_TO_BUILD = os.getcwd() + "/build/"
PATH_TO_TEST = os.getcwd() + "/test/"
PATH_TO_E2E = os.getcwd() + "/e2e/"

mkdir_bin = "/usr/bin/mkdir -p "
rmdir_bin = "/bin/rm -rf "
rm_bin = "/bin/rm "
dush_bin = "/usr/bin/du -sh "

os.getenv("some_env_name")

print(PATH_TO_STATIC)
print(PATH_TO_BUILD)


# # Functions related to FileIO

# In[3]:


def write_file(filepath, filename, dataString, mode="w"):
  with open(filepath + filename, mode) as file:
    file.write(dataString)
    file.flush()
    file.close()


# In[4]:


def write_new_file(filepath, filename, dataString):
  mode = "w"
  write_file(filepath, filename, dataString, mode)


# In[5]:


def use_subprocess(command, commandInput=""):
  myprocess = subprocess.Popen(command, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, errors = myprocess.communicate(input=commandInput)
  myprocess.wait()
  return [output, errors]


# In[6]:


def write_directory(directory_path, directory_name, mkdir_bin=mkdir_bin):
  use_subprocess(mkdir_bin + directory_path + directory_name)

def remove_directory(directory_path, directory_name, rmdir_bin=rmdir_bin):
  use_subprocess(rmdir_bin + directory_path + directory_name)


# In[7]:


def remove_file(directory_path, directory_name, rm_bin=rm_bin):
  use_subprocess(rm_bin + directory_path + directory_name)


# In[8]:


def du_sh(directory_path, dush_bin=dush_bin):
  use_subprocess(dush_bin + directory_path)

# alias
def get_folder_size(directory_path):
  du_sh(directory_path)


# In[17]:


def read_file(filepath, filename):
  with open(filepath + filename, "r") as file:
    return "".join(file.readlines())

def show_directory(directory_name_with_path):
  return list(sorted(os.listdir(directory_name_with_path)))

def list_directory(directory_path, directory_name):
  return show_directory(directory_path + directory_name)


# In[10]:


def eval_string(some_string):
  return eval(some_string)


# In[11]:


def read_list_file(filepath, filename):
  return list(eval_string(read_file(filepath, filename)))


# In[12]:


def read_dict_file(filepath, filename):
  return dict(eval_string(read_file(filepath, filename)))

# alias
def read_json_file(filepath, filename):
  return read_dict_file(filepath, filename)


# In[13]:


def to_ajson_string(some_object, sort_keys=True, indent=4):
  return json.dumps(some_object, sortKeys=sort_key, indent=indent)


# In[14]:


def load_ajson_string(some_json_string):
  return json.loads(some_json_string)


# In[15]:


#display(os.environ)
os.getenv("HOME")


# In[ ]:





# In[ ]:




