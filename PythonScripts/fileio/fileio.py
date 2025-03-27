#!/usr/bin/env python
# coding: utf-8

# # Import related to FileIO

# In[1]:


import subprocess
import os
import json


# # Configuration related to FileIO

# In[60]:


CWD_PATH = os.getcwd()
PATH_TO_STATIC = CWD_PATH + "/Static/"
PATH_TO_BUILD = CWD_PATH + "/build/"
PATH_TO_TEST = CWD_PATH + "/test/"
PATH_TO_E2E = CWD_PATH + "/e2e/"

DEFAULT_PATH = ""

mkdir_bin = "/usr/bin/mkdir -p "
rmdir_bin = "/bin/rm -rf "
rm_bin = "/bin/rm "
dush_bin = "/usr/bin/du -sh "
wc_bin = "/usr/bin/wc -l "
wcword_bin = "/usr/bin/wc -w "
wcbytes_bin = "/usr/bin/wc -m "

head_bin = "/usr/bin/head -n "
tail_bin = "/usr/bin/tail -n "
partial_file_line_limit = "100 "
headc_bin = "/usr/bin/head -c "


cat_bin = "/bin/cat "

grep_bin = " | /usr/bin/grep "
awk_bin = " | /usr/bin/awk "
xargs_bin = "| /usr/bin/xargs "

ps_bin = "/bin/ps aux "
kill_bin = "/bin/kill "
ls_bin = "/bin/ls -la "
ls1_bin = "/bin/ls -1 "
tree_bin = "/opt/homebrew/bin/tree "

ENVIRON = os.environ
HOME_ENV = os.getenv("HOME")

#use AST or get all the config variables and functions into an object => dict key

print(PATH_TO_STATIC)
print(PATH_TO_BUILD)
#print(HOME_ENV)


# # Functions related to FileIO

# In[3]:


def write_file(filename, data_string, filepath="", mode="w"):
  with open(filepath + filename, mode) as file:
    file.write(data_string)
    file.flush()
    file.close()


# In[4]:


def write_new_file(filename, data_string, filepath=""):
  mode = "w"
  write_file(filename, data_string, filepath, mode)


# In[27]:


def use_subprocess(command, commandInput=""):
  myprocess = subprocess.Popen(command, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, errors = myprocess.communicate(input=commandInput)
  myprocess.wait()
  return [output, errors]


# In[28]:


def write_directory(directory_name, directory_path="", mkdir_bin=mkdir_bin):
  return use_subprocess(mkdir_bin + directory_path + directory_name)

def remove_directory(directory_name, directory_path="", rmdir_bin=rmdir_bin):
  return use_subprocess(rmdir_bin + directory_path + directory_name)


# In[29]:


def remove_file(directory_name, directory_path="", rm_bin=rm_bin):
  return use_subprocess(rm_bin + directory_path + directory_name)


# In[41]:


def du_sh(directory_name, directory_path="", dush_bin=dush_bin):
  return use_subprocess(dush_bin + directory_path + directory_name)

# alias
def get_folder_size(directory_name, directory_path=""):
  return du_sh(directory_name, directory_path)


# In[61]:


def read_file_raw(filename, filepath=""):
  with open(filepath + filename, "r") as file:
    return file.readlines()

def read_file(filename, filepath=""):
  return "".join(read_file_raw(filename, filepath))

def show_directory(directory_name_with_path):
  return list(sorted(os.listdir(directory_name_with_path)))

def list_directory(directory_name, directory_path=""):
  return show_directory(directory_path + directory_name)

def ls_dir(directory_name, directory_path="", ls_bin=ls_bin):
  return useSubprocess(ls_bin + directory_path + directory_name)

def ls1_dir(directory_name, directory_path="", ls1_bin=ls1_bin):
  return useSubprocess(ls1_bin + directory_path + directory_name)


# In[31]:


def eval_string(some_string):
  return eval(some_string)


# In[32]:


def read_list_file(filename, filepath=""):
  return list(eval_string(read_file(filename, filepath)))


# In[33]:


def read_dict_file(filename, filepath=""):
  return dict(eval_string(read_file(filename, filepath)))

# alias
def read_json_file(filename, filepath=""):
  return read_dict_file(filename, filepath)


# In[34]:


def to_ajson_string(some_object, sort_keys=True, indent=4):
  return json.dumps(some_object, sortKeys=sort_key, indent=indent)


# In[35]:


def load_ajson_string(some_json_string):
  return json.loads(some_json_string)


# In[56]:





# In[37]:


def read_file_head(filename, filepath="", linecount=partial_file_line_limit, head_bin=head_bin):
  return use_subprocess(head_bin + linecount + filepath + filename)


# In[38]:


def read_file_tail(filename, filepath="", linecount=partial_file_line_limit, tail_bin=tail_bin):
  return use_subprocess(tail_bin + linecount + filepath + filename)


# In[45]:


def read_file_characters(filename, filepath="", charcount=partial_file_line_limit, head_bin=head_bin):
  return use_subprocess(headc_bin + charcount + filepath + filename)


# In[62]:


read_file_head_offset_signature = {
"filename"    
}
# to debug i would need to add params, hmm
def read_file_headoffset(params=read_file_head_offset_signature):
  filename, filepath="", linecount=partial_file_line_limit, offsetcount= head_bin=head_bin


# In[23]:


def grep_file(filename, filepath="", filter_string, grep_bin=grep_bin):
  return use_subprocess(cat_bin + filepath + filename + grep_bin + filter_string)


# In[50]:


def wc_file(filename, filepath="", wc_bin=wc_bin):
  return use_subprocess(wc_bin + filepath + filename)

def wcword_file(filename, filepath="", wcword_bin=wcword_bin):
  return use_subprocess(wcword_bin + filepath + filename)

def wcbytes_file(filename, filepath="", wcbytes_bin=wcbytes_bin):
  return use_subprocess(wcbytes_bin + filepath + filename)


# In[48]:


def tree_dir(directory_name, directory_path="", tree_bin=tree_bin):
  return use_subprocess(tree_bin + directory_path + directory_name)


# In[24]:


def process_id_of(filter_string):
  return use_subprocess(ps_bin + grep_bin + filter_string + awk_bin + "'${print $2}'" + xargs_bin)


# In[25]:


def kill_process_ids(process_ids):
  return [use_subprocess(kill_bin + str(process_id)) for process_id in process_ids]


# In[ ]:


def list_directory_with_type(directory_name, directory_path=""):
  items = useListdir(path)
  output = [[file, os.path.isdir(path + file)] for file in items]
  directory = list(sorted([[item, status] for [item, status] in output if status]))
  files = list(sorted([[item, status] for [item, status] in output if not status]))
  return {directory_path: [*directory, *files]}


# In[51]:


def append_to_file(filename, data_string, filepath=""):
  mode="a"
  write_file(filename, data_string, filepath, mode)


# In[ ]:





# In[ ]:





# # Custom Usage

# In[39]:


custom_usage = """
# extract configuration
CODEBASE_HOME = "/Users/devssh/EventServer/Codebase/"

# hardcode a function value
def read_home_dir():
  return list_directory_with_type(CODEBASE_HOME)

# execute function
print(read_home_dir())

"""

#eval(custom_usage)


# # Usage

# In[44]:


usage = """

du_sh(CODEBASE_HOME)

"""


# In[43]:


usage_output = """

[' 11G\t/Users/devssh/EventServer/Codebase/\n', '']
"""


# # Integration usage

# In[ ]:





# # E2E usage

# In[ ]:





# # Export

# In[53]:


# export it as object
# import object in other file and use in server methods with appropriate return handling.


# In[ ]:





# # FAQ

# In[59]:


faq = """

"""


# In[ ]:




