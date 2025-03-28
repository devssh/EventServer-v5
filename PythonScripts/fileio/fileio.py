#!/usr/bin/env python
# coding: utf-8

# # Import related to FileIO

# In[1]:


import subprocess
import os
import json


# # Configuration related to FileIO

# In[2]:


CWD_PATH = os.getcwd()
PATH_TO_STATIC = CWD_PATH + "/Static/"
PATH_TO_BUILD = CWD_PATH + "/build/"
PATH_TO_TEST = CWD_PATH + "/test/"
PATH_TO_E2E = CWD_PATH + "/e2e/"

DEFAULT_PATH = ""

mkdir_bin = "/bin/mkdir -p "
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
#lsof

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


# In[5]:


def use_subprocess(command, commandInput=""):
  myprocess = subprocess.Popen(command, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, errors = myprocess.communicate(input=commandInput)
  myprocess.wait()
  return [output, errors]


# In[6]:


def write_directory(directory_name, directory_path="", mkdir_bin=mkdir_bin):
  return use_subprocess(mkdir_bin + directory_path + directory_name)

def remove_directory(directory_name, directory_path="", rmdir_bin=rmdir_bin):
  return use_subprocess(rmdir_bin + directory_path + directory_name)


# In[7]:


def remove_file(directory_name, directory_path="", rm_bin=rm_bin):
  return use_subprocess(rm_bin + directory_path + directory_name)


# In[8]:


def du_sh(directory_name, directory_path="", dush_bin=dush_bin):
  return use_subprocess(dush_bin + directory_path + directory_name)

# alias
def get_folder_size(directory_name, directory_path=""):
  return du_sh(directory_name, directory_path)


# In[9]:


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
  return use_subprocess(ls_bin + directory_path + directory_name)

def ls1_dir(directory_name, directory_path="", ls1_bin=ls1_bin):
  return use_subprocess(ls1_bin + directory_path + directory_name)


# In[10]:


def eval_string(some_string):
  return eval(some_string)


# In[11]:


def exec_string(some_string):
  return exec(some_string)


# In[12]:


def read_list_file(filename, filepath=""):
  return list(eval_string(read_file(filename, filepath)))


# In[13]:


def read_dict_file(filename, filepath=""):
  return dict(eval_string(read_file(filename, filepath)))

# alias
def read_json_file(filename, filepath=""):
  return read_dict_file(filename, filepath)


# In[14]:


def to_ajson_string(some_object, sort_keys=True, indent=4):
  return json.dumps(some_object, sort_keys=sort_keys, indent=indent)


# In[15]:


def load_ajson_string(some_json_string):
  return json.loads(some_json_string)


# In[16]:


def read_file_head(filename, filepath="", linecount=partial_file_line_limit, head_bin=head_bin):
  return use_subprocess(head_bin + str(linecount) + " " + filepath + filename)


# In[17]:


def read_file_tail(filename, filepath="", linecount=partial_file_line_limit, tail_bin=tail_bin):
  return use_subprocess(tail_bin + str(linecount) + " " + filepath + filename)


# In[18]:


def read_file_characters(filename, filepath="", charcount=partial_file_line_limit, head_bin=head_bin):
  return use_subprocess(headc_bin + str(charcount) + " " + filepath + filename)


# In[19]:


# no way to offset using head tail without full buffer being processed


# In[20]:


def grep_file(filename, filepath="", filter_string="", grep_bin=grep_bin):
 return use_subprocess(cat_bin + filepath + filename + grep_bin + filter_string)


# In[21]:


def wc_file(filename, filepath="", wc_bin=wc_bin):
  return use_subprocess(wc_bin + filepath + filename)

def wcword_file(filename, filepath="", wcword_bin=wcword_bin):
  return use_subprocess(wcword_bin + filepath + filename)

def wcbytes_file(filename, filepath="", wcbytes_bin=wcbytes_bin):
  return use_subprocess(wcbytes_bin + filepath + filename)


# In[22]:


def tree_dir(directory_name, directory_path="", tree_bin=tree_bin):
  return use_subprocess(tree_bin + directory_path + directory_name)


# In[23]:


def process_id_of(filter_string):
  return use_subprocess(ps_bin + grep_bin + filter_string + awk_bin + "'{print $2}'" + xargs_bin)


# In[24]:


def kill_process_ids(process_ids):
  return [use_subprocess(kill_bin + str(process_id)) for process_id in process_ids]


# In[25]:


def list_directory_with_type(directory_name, directory_path=""):
  directory_content = show_directory(directory_path + directory_name)
  directory_content_mapping = [[content, os.path.isdir(directory_path + directory_name + content)] for content in directory_content]
  return directory_content_mapping


# In[26]:


def append_to_file(filename, data_string, filepath=""):
  mode="a"
  write_file(filename, data_string, filepath, mode)


# In[ ]:





# In[ ]:





# # Custom Usage

# In[27]:


custom_usage = """
# extract configuration
CODEBASE_HOME = "/Users/devssh/EventServer/Codebase/"

# hardcode a function value
def read_home_dir():
  return list_directory_with_type(CODEBASE_HOME)

# execute function
print(read_home_dir())

"""

#exec(custom_usage)


# In[28]:


custom_usage_output="""
[['.DS_Store', False], ['Bootstrapper-Springboot-2022', False], ['Documentation-AttemptV3-2024', False], ['EventServer-v5', False], ['Puzzles-2024', False], ['PythonReact', False], ['PythonReactv3-2023', False], ['Rex5', False], ['Rex5Migration', False], ['UserInterfaceV5', False], ['html-tut', False], ['immoguna', False], ['names', False]]
"""

#custom_usage_output


# # Usage

# In[29]:


usage = """

print(None)
print(None is not None)
print("abc" is not None)
print(["", ""] is not None)

print("\\n\\n\\nInit point")
print(write_directory("/Users/devssh/test1"))
print(remove_directory("/Users/devssh/test1"))
print(write_directory("/Users/devssh/test1"))
print(write_directory("/Users/devssh/test2"))
print(write_directory("/Users/devssh/test2"))
print(write_file("/Users/devssh/test1/abc.txt", "Hello\\nWorld!\\n"))

print("\\n\\n\\nLS point")
print(ls_dir("/Users/devssh/test1"))
print(write_directory("/Users/devssh/test3"))
print(remove_directory("/Users/devssh/test3"))

TEST_DIR="/Users/devssh/test1/"
print(write_new_file("def.txt", "to be deleted", TEST_DIR))
print(remove_file("/Users/devssh/test1/def.txt"))
print(du_sh(TEST_DIR))

print("\\n\\n\\nRead point")
print(read_file("/Users/devssh/test1/abc.txt"))
print(show_directory("/Users/devssh/test1"))
print(ls1_dir("/Users/devssh/test1"))

print("\\n\\n\\nEval point")
print(eval_string("print('hello')"))
print(exec_string("print('world')"))

print(write_file("sample_list.txt", '["one", "three", "two"]',TEST_DIR))
print(read_list_file("/Users/devssh/test1/sample_list.txt"))

print(write_file("sample_dict.txt", '{"one": "1", "three": 3, "two": 2}',TEST_DIR))
print(read_dict_file("/Users/devssh/test1/sample_dict.txt"))

print(to_ajson_string({"one": 1, "two": "two"}))
print(load_ajson_string(to_ajson_string({"one": 1, "two": "two"})))
print(load_ajson_string(to_ajson_string(["one", "two"])))
print(to_ajson_string(["one", "two"]))

print("\\n\\n\\nHead point")
print(append_to_file("abc.txt", "\\nline1",TEST_DIR))
print(append_to_file("abc.txt", "\\nline2",TEST_DIR))
print(append_to_file("abc.txt", "\\nline3",TEST_DIR))
print(append_to_file("abc.txt", "\\nline4",TEST_DIR))
print(append_to_file("abc.txt", "\\nline5",TEST_DIR))
print(append_to_file("abc.txt", "\\nline6",TEST_DIR))
print(append_to_file("abc.txt", "\\nline7\\n",TEST_DIR))

print(read_file_head("abc.txt", TEST_DIR, "5"))
print(read_file_tail("abc.txt", TEST_DIR, "5"))
print(read_file_characters("abc.txt", TEST_DIR, "10"))
print(grep_file("abc.txt", TEST_DIR, "line"))
print(wc_file(TEST_DIR + "abc.txt"))
print(wcword_file(TEST_DIR + "abc.txt"))
print(wcbytes_file(TEST_DIR + "abc.txt"))
print(tree_dir(TEST_DIR))

print("\\n\\n\\nShell point")
print(process_id_of("ssh-agent"))
print(kill_process_ids(process_id_of("ssh-agent")[0].split(" ")))
print(write_directory(TEST_DIR + "test_dir"))
print(list_directory_with_type(TEST_DIR))

"""

#exec(usage)


# In[30]:


usage_output = """

None
False
True
True



Init point
['', '']
['', '']
['', '']
['', '']
['', '']
None



LS point
['total 8\ndrwxr-xr-x   3 devssh  staff    96 Mar 28 19:37 .\ndrwxr-x---+ 86 devssh  staff  2752 Mar 28 19:37 ..\n-rw-r--r--   1 devssh  staff    13 Mar 28 19:37 abc.txt\n', '']
['', '']
['', '']
None
['', '']
['4.0K\t/Users/devssh/test1/\n', '']



Read point
Hello
World!

['abc.txt']
['abc.txt\n', '']



Eval point
hello
None
world
None
None
['one', 'three', 'two']
None
{'one': '1', 'three': 3, 'two': 2}
{
    "one": 1,
    "two": "two"
}
{'one': 1, 'two': 'two'}
['one', 'two']
[
    "one",
    "two"
]



Head point
None
None
None
None
None
None
None
['Hello\nWorld!\n\nline1\nline2\n', '']
['line3\nline4\nline5\nline6\nline7\n', '']
['Hello\nWorl', '']
['line1\nline2\nline3\nline4\nline5\nline6\nline7\n', '']
['      10 /Users/devssh/test1/abc.txt\n', '']
['       9 /Users/devssh/test1/abc.txt\n', '']
['      56 /Users/devssh/test1/abc.txt\n', '']
['/Users/devssh/test1/\n├── abc.txt\n├── sample_dict.txt\n└── sample_list.txt\n\n0 directories, 3 files\n', '']



Shell point
['5331 5329\n', '']
[['', 'kill: 5337: No such process\n'], ['', 'kill: 5335: No such process\n']]
['', '']
[['abc.txt', False], ['sample_dict.txt', False], ['sample_list.txt', False], ['test_dir', True]]

"""


# # Integration usage

# In[ ]:





# # E2E usage

# In[ ]:





# # Export

# In[31]:


# export it as object
# import object in other file and use in server methods with appropriate return handling.


# In[ ]:





# # FAQ

# In[32]:


faq = """
1. Handling return type for server
2. Handling parameters for signature
3. Handling default parameters
4. Handling usage

"""


# In[ ]:




