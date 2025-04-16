



import subprocess
import os
import json
import datetime


CWD_PATH = os.getcwd()

file_io_config = {
"CWD_PATH": CWD_PATH,
"PATH_TO_HOME": CWD_PATH + "/Home/",
"PATH_TO_STATIC": CWD_PATH + "/Static/",
"PATH_TO_BUILD": CWD_PATH + "/build/",
"PATH_TO_TEST": CWD_PATH + "/test/",
"PATH_TO_E2E": CWD_PATH + "/e2e/",

"DEFAULT_PATH": "",

"pwd_bin": "/bin/pwd ",
"mkdir_bin": "/bin/mkdir -p ",
"rmdir_bin": "/bin/rm -rf ",
"rm_bin": "/bin/rm ",
"dush_bin": "/usr/bin/du -sh ",
"wc_bin": "/usr/bin/wc -l ",
"wcword_bin": "/usr/bin/wc -w ",
"wcbytes_bin": "/usr/bin/wc -m ",

"head_bin": "/usr/bin/head -n ",
"tail_bin": "/usr/bin/tail -n ",
"partial_file_line_limit": "100 ",
"headc_bin": "/usr/bin/head -c ",


"cat_bin": "/bin/cat ",

"grep_bin": " | /usr/bin/grep ",
"awk_bin": " | /usr/bin/awk ",
"xargs_bin": "| /usr/bin/xargs ",

"ps_bin": "/bin/ps aux ",
"kill_bin": "/bin/kill ",
"ls_bin": "/bin/ls -la ",
"ls1_bin": "/bin/ls -1 ",
"tree_bin": "/opt/homebrew/bin/tree ",


"launchctl_bin": "/bin/launchctl ",

"ENVIRON": os.environ,
"HOME_ENV": os.getenv("HOME")

}

#print(file_io_config["PATH_TO_E2E"])
#print(file_io_config["PATH_TO_BUILD"])
#lsof -p $(ps  aux | grep tomcat | awk '{print $2}' | xargs | awk '{print $2}')
#HOME_ENV
#DEFAULT_PATH

def to_ajson_string(some_object, sort_keys=True, indent=4):
  return json.dumps(some_object, sort_keys=sort_keys, indent=indent)

def load_ajson_string(some_json_string):
  return json.loads(some_json_string)

def pretty_json(some_object, indent=4):
  return json.dumps(some_object, indent=indent)

def pretty_print_json(some_object, indent=4):
  print(pretty_json(some_object, indent))

def eval_string_fn(some_string):
  return eval(some_string)

def exec_string_fn(some_string):
  return exec(some_string)


def write_file_fn(full_name, mode, data_string):
  with open(full_name, mode) as file:
    file.write(data_string)
    file.flush()
    file.close()

def read_file_raw_fn(file_name):
  with open(file_name, "r") as file:
    return file.readlines()

def read_file_fn(file_name):
  return "".join(read_file_raw_fn(file_name))

def read_dict_file_fn(file_name):
  return dict(eval_string_fn(read_file_fn(file_name)))

def show_directory_fn(directory_name):
  return list(sorted(os.listdir(directory_name)))


def use_subprocess_fn(command, command_input=""):
  myprocess = subprocess.Popen(command, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, errors = myprocess.communicate(input=command_input)
  myprocess.wait()
  return [output, errors]


def set_default_request_params(request, default_dict):
  request_dict = {**request}
  for key, value in default_dict.items():
    if key not in request:
      request_dict[key] = value
  return request_dict

def eval_string(request):
  return eval_string_fn(request["command"])

def exec_string(request):
  return exec_string_fn(request["command"])

def read_file_raw(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]    
})
  return {
"result": read_file_raw_fn(request["file_path"] + request["file_name"])
}

def read_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]     
})
  return {
"result": read_file_fn(request["file_path"] + request["file_name"])
}

def read_list_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]      
})
  return list(eval_string_fn(read_file_fn(request["file_path"] + request["file_name"])))

def read_dict_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]      
})
  return read_dict_file_fn(request["file_path"] + request["file_name"])

def show_directory(some_request):
  request = set_default_request_params(some_request, {
"directory_path": file_io_config["DEFAULT_PATH"],
})
  return show_directory_fn(request["directory_path"] + request["directory_name"])

def eval_string(request):
  return eval_string_fn(request["command"])

def exec_string(request):
  return exec_string_fn(request["command"])

def read_file_raw(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]    
})
  return {
"result": read_file_raw_fn(request["file_path"] + request["file_name"])
}

def read_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]     
})
  return {
"result": read_file_fn(request["file_path"] + request["file_name"])
}

def read_list_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]      
})
  return list(eval_string_fn(read_file_fn(request["file_path"] + request["file_name"])))

def read_dict_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"]      
})
  return read_dict_file_fn(request["file_path"] + request["file_name"])

def show_directory(some_request):
  request = set_default_request_params(some_request, {
"directory_path": file_io_config["DEFAULT_PATH"],
})
  return show_directory_fn(request["directory_path"] + request["directory_name"])

def write_file(some_request):
  request = set_default_request_params(some_request, {
"file_path": file_io_config["DEFAULT_PATH"],
"mode": "w"
})
  full_name = request["file_path"] + request["file_name"]
  data_string = request["data_string"]
  mode = request["mode"]
  write_file_fn(full_name, mode, data_string)
  return {"write_file": full_name, "result": "200"}

def write_new_file(request):
  request["mode"] = "w"
  return write_file(request)

def append_to_file(request):
  request["mode"] = "a"
  return write_file(request)

def use_subprocess(some_request):
  request = set_default_request_params(some_request, {
"command_input": "",
"command_name": "use_subprocess"
})
  result = use_subprocess_fn(request["command"], request["command_input"])
  success = result[0]
  error = result[1]
  if success == "" and error == "":
    success = "200"
  if error != "":
    success = "418"
  return {request["command_name"]: request["command"], "result": success.strip(), "error": error}

def simple_concat_command_string(request, default_dict, command_list, command_name):
  updated_request = set_default_request_params(request, default_dict)
  command = "".join([updated_request[key] for key in command_list])
  return use_subprocess({"command": command, "command_name": command_name})

def write_directory(request):
  return simple_concat_command_string(request, {
"mkdir_bin": file_io_config["mkdir_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["mkdir_bin", "directory_path", "directory_name"], 
"write_directory")

def remove_directory(request):
  return simple_concat_command_string(request, {
"rmdir_bin": file_io_config["rmdir_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["rmdir_bin", "directory_path", "directory_name"], 
"remove_directory")

def remove_file(request):
  return simple_concat_command_string(request, {
"rm_bin": file_io_config["rm_bin"],
"file_path": file_io_config["DEFAULT_PATH"]
}, 
["rm_bin", "file_path", "file_name"], 
"remove_file")

def du_sh(request):
  return simple_concat_command_string(request, {
"dush_bin": file_io_config["dush_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["dush_bin", "directory_path", "directory_name"], 
"du_sh")

def ls_dir(request):
  return simple_concat_command_string(request, {
"ls_bin": file_io_config["ls_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["ls_bin", "directory_path", "directory_name"], 
"ls_dir")

def ls1_dir(request):
  return simple_concat_command_string(request, {
"ls1_bin": file_io_config["ls1_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["ls1_bin", "directory_path", "directory_name"], 
"ls1_dir")

def read_file_head(request):
  return simple_concat_command_string(request, {
"head_bin": file_io_config["head_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"line_count": str(file_io_config["partial_file_line_limit"]),
"gap": " "
}, 
["head_bin", "file_path", "line_count", "gap", "file_name"], 
"read_file_head")

def read_file_tail(request):
  return simple_concat_command_string(request, {
"tail_bin": file_io_config["tail_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"line_count": str(file_io_config["partial_file_line_limit"]),
"gap": " "
}, 
["tail_bin", "file_path", "line_count", "gap", "file_name"], 
"read_file_tail")

def read_file_head_characters(request):
  return simple_concat_command_string(request, {
"headc_bin": file_io_config["headc_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"char_count": str(file_io_config["partial_file_line_limit"]),
"gap": " "
}, 
["headc_bin", "file_path", "char_count", "gap", "file_name"], 
"read_file_head_characters")

def grep_file(request):
  return simple_concat_command_string(request, {
"grep_bin": file_io_config["grep_bin"],
"cat_bin": file_io_config["cat_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"filter_string": ""
}, 
["cat_bin", "file_path", "file_name", "grep_bin", "filter_string"], 
"grep_file")

def wc_file(request):
  return simple_concat_command_string(request, {
"wc_bin": file_io_config["wc_bin"],
"file_path": file_io_config["DEFAULT_PATH"]
}, 
["wc_bin", "file_path", "file_name"], 
"wc_file")

def wcword_file(request):
  return simple_concat_command_string(request, {
"wcword_bin": file_io_config["wcword_bin"],
"file_path": file_io_config["DEFAULT_PATH"]
}, 
["wcword_bin", "file_path", "file_name"], 
"wcword_file")

def wcbytes_file(request):
  return simple_concat_command_string(request, {
"wcbytes_bin": file_io_config["wcbytes_bin"],
"file_path": file_io_config["DEFAULT_PATH"]
}, 
["wcbytes_bin", "file_path", "file_name"], 
"wcbytes_file")

def tree_dir(request):
  return simple_concat_command_string(request, {
"tree_bin": file_io_config["tree_bin"],
"directory_path": file_io_config["DEFAULT_PATH"]
}, 
["tree_bin", "directory_path", "directory_name"], 
"tree_dir")

def process_ids_of(request):
  return simple_concat_command_string(request, {
"ps_bin": file_io_config["ps_bin"],
"grep_bin": file_io_config["grep_bin"],
"filter_string": "",
"awk_bin": file_io_config["awk_bin"],
"awk_arg": "'{print $2}'",
"xargs_bin": file_io_config["xargs_bin"]
}, 
["ps_bin", "grep_bin", "filter_string", "awk_bin", "awk_arg", "xargs_bin"], 
"process_id_of")

def unload_gunicorn(request):
  return simple_concat_command_string(request, {
"launchctl_bin": file_io_config["launchctl_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"unload": "unload "
}, 
["launchctl_bin", "unload", "file_path", "file_name"], 
"load_gunicorn")

def load_gunicorn(request):
  return simple_concat_command_string(request, {
"launchctl_bin": file_io_config["launchctl_bin"],
"file_path": file_io_config["DEFAULT_PATH"],
"load": "load "
}, 
["launchctl_bin", "load", "file_path", "file_name"], 
"load_gunicorn")

def kill_process_ids(request):
  updated_request = set_default_request_params(request, {
"kill_bin": file_io_config["kill_bin"]  
})
  return {
"result": [
use_subprocess({
"command": file_io_config["kill_bin"] + str(process_id), 
"command_name": "kill_process_ids"
}) for process_id in request["process_ids"].split(" ")
]}

def list_directory_with_type(some_request):
  request = set_default_request_params(some_request, {
"directory_path": file_io_config["DEFAULT_PATH"]      
})
  directory_name = request["directory_path"] + request["directory_name"]
  directory_content = show_directory_fn(directory_name)
  directory_content_mapping = [
[content, os.path.isdir(directory_name + content)]
for content in directory_content
]
  return {
"directory_name": directory_name,
"dirs": [
dir_name for [dir_name, dir_type] in directory_content_mapping if dir_type    
],
"files": [
file_name for [file_name, dir_type] in directory_content_mapping if not dir_type
]
}

file_io = {
"eval_string": eval_string,
"exec_string": exec_string,
"read_file_raw": read_file_raw,
"read_file": read_file,
"read_list_file": read_list_file,
"read_dict_file": read_dict_file,
"read_json_file": read_dict_file,
"show_directory": show_directory,
"list_directory": show_directory,
"write_file": write_file,
"append_to_file": append_to_file,
"use_subprocess": use_subprocess,
"write_directory": write_directory,
"remove_directory": remove_directory,
"remove_file": remove_file,
"du_sh": du_sh,
"get_folder_size": du_sh,
"ls_dir": ls_dir,
"ls1_dir": ls1_dir,
"read_file_head": read_file_head,
"read_file_tail": read_file_tail,
"read_file_head_characters": read_file_head_characters,
"grep_file": grep_file,
"wc_file": wc_file,
"wcword_file": wcword_file,
"wcbytes_file": wcbytes_file,
"tree_dir": tree_dir,
"process_ids_of": process_ids_of,
"unload_gunicorn": unload_gunicorn,
"load_gunicorn": load_gunicorn,
"kill_process_ids": kill_process_ids,
"list_directory_with_type": list_directory_with_type
}

file_io_extra = {
"to_ajson_string": to_ajson_string,
"load_ajson_string": load_ajson_string,
"pretty_json": pretty_json,
"pretty_print_json": pretty_print_json,
"eval_string_fn": eval_string_fn,
"exec_string_fn": exec_string_fn,
"write_file_fn": write_file_fn,
"read_file_raw_fn": read_file_raw_fn,
"read_file_fn": read_file_fn,
"read_dict_file_fn": read_dict_file_fn,
"show_directory_fn": show_directory_fn,
"use_subprocess_fn": use_subprocess_fn,
"set_default_request_params": set_default_request_params,
"write_new_file": write_new_file,
"simple_concat_command_string": simple_concat_command_string
}








