



from file_io import file_io, file_io_config, file_io_extra

def pretty_json(some_object, indent=4):
  return json.dumps(some_object, indent=indent)

paths = [
"/bin",
"/usr/local/bin",
"/usr/bin",
"/opt/homebrew/bin",
"/usr/sbin",
"/opt/homebrew/anaconda3/bin"
]

location = "/Users/devssh/EventServer/Codebase/EventServerV5/Shell/bin/"

file_io["remove_directory"]({
"directory_name": location
})


file_io["write_directory"]({
"directory_name": location
})

reverse_index = {}

for i, path in enumerate(paths):
  reverse_index[i + 1] = path
  reverse_index[path] = i + 1

def write_shell_file(path):
  res0 = file_io["ls1_dir"]({"directory_name": path})["result"].split("\n")
  for binary_exe_name in res0:
    reverse_index[binary_exe_name] = reverse_index[path]
  res1 = file_io["write_file"]({
"file_name": location + "ls1"+ path.replace("/", "-") +".json",
"data_string": pretty_json(res0)
})
  res2 = file_io["write_file"]({
"file_name": location + "lsla"+ path.replace("/", "-") +".json",
"data_string": file_io["ls_dir"]({"directory_name": path})["result"]
})
  res3 = file_io["write_file"]({
"file_name": location + "group"+ path.replace("/", "-") +".json",
"data_string": pretty_json(sorted(file_io["ls_dir"]({"directory_name": path})["result"].split("\n")))
})
  return [res1, res2, res3]

for path in paths:
  print(pretty_json(write_shell_file(path)))

file_io["write_file"]({

"file_name": "/Users/devssh/EventServer/Codebase/EventServerV5/Shell/bin/aliases.json",
"data_string": pretty_json({
"bin": [
"ps"
],
"usr-local-bin": "docker, k8, gcm, vagrant, auth links",
"usr-bin": {
"s flag": [
"su",
"sudo",
"at",
"atq",
"atrm",
"batch",
"crontab",
"login",
"newgrp",
"quota",
"top",
],
"read only special exec": [
"write"
],
"links": [
"auval",
"bzcmp",
"bzless",
"captoinfo",
"cvaffinity",
"cvcp",
"cvmkdir",
"cvmkfile",
"ex",
"fontrestore",
"infotocap",
"klist",
"kswitch",
"ldapadd",
"mailq",
"manpath",
"nano",
"ncdestroy",
"ncinit",
"nclist",
"newaliases",
"qlmanage",
"reset",
"rview",
"rvim",
"safaridriver",
"sdx",
"slogin",
"snfsdefrag",
"snmpinform",
"swcutil",
"tar",
"tclsh",
"tclsh8.5",
"tkcon",
"vi",
"view",
"vimdiff",
"wish",
"yaa"
]
},
"opt-homebrew-bin": "mostly links",
"details": """
1. Background shading is the s flag instead of x making it protected from execution
2. Symbolic links are purple, normal files are red. usr-local-bin is symbolic.
It turns out as l flag indicating link instead of - for regular file.
3. ACFS is short for Oracle ASM Cluster FileSystem. ASM is Automatic Storage Management
4. /usr/sbin
5. /System/Library
6. /opt/homebrew/anaconda3/bin
"""
})
})

summary = []
for path in paths:
  res5 = file_io["wc_file"]({
"file_name": location + "ls1" + path.replace("/", "-") + ".json"
})["result"]
  summary = [*summary, res5]

file_io["write_file"]({
"file_name": "/Users/devssh/EventServer/Codebase/EventServerV5/Shell/bin/summary.json",
"data_string": pretty_json(
summary
)})

file_io["write_file"]({
"file_name": location + "reverse-index-binary-name.json",
"data_string": pretty_json(reverse_index)
})

print(reverse_index[reverse_index["lsof"]])
