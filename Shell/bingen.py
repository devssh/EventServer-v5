



from file_io import file_io


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

def write_shell_file(path):
  res1 = file_io["write_file"]({
"file_name": location + "ls1"+ path.replace("/", "-") +".json",
"data_string": pretty_json(file_io["ls1_dir"]({"directory_name": path})["result"].split("\n"))
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


res4 = file_io["write_file"]({

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

print(res4)



