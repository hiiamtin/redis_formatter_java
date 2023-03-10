import javaobj.v2 as javaobjv2
import sys
import json

data = sys.argv[1]
# print(data.encode().decode('unicode_escape').encode("raw_unicode_escape"))
pyobj = javaobjv2.loads(bytes.fromhex(data))
ob = pyobj.dump()

def set_to_value_of_root(data, stack):
    root = stack.pop()
    root_key = list(root.keys())[0]
    root_value = root[root_key]
    key = list(root_value.keys())[-1]
    root_value[key] = data
    stack.append({root_key:root_value})

def new_object(data, level, stack):
    if(data.startswith("OBJECT")):
        data = data.split(":")
        key_name = data[0].split(" ")[1]
        value = data[1] if data[1] != " " else {}
        stack.append({level:{key_name:value}})
    elif(data.startswith("INTEGER")):
        data = int(data.split(":")[1].strip())
        set_to_value_of_root(data,stack)
    elif(data.startswith("STRING") or data.startswith("[String")):
        data = data.split(":")[1].strip()[1:-2]
        set_to_value_of_root(data,stack)
    elif(data.startswith("b'")):
        data = data.strip()
        set_to_value_of_root(data,stack)

def append_object(parent, data, level, stack):
    if(data.startswith("OBJECT")):
        data = data.split(":")
        key_name = data[0].split(" ")[1]
        value = data[1] if data[1] != " " else {}
        parent[key_name] = value
        stack.append({level:parent})

def check_keyword(str,stack):
    level = len(str)-len(str.lstrip())
    while(level > 0 and len(stack) > 0 and level <= list(stack[-1].keys())[0]):
        if(level == list(stack[-1].keys())[0]):
            data = stack.pop()
            key_name = list(data.keys())[0]
            value = data[key_name]
            append_object(value,str.lstrip(),level,stack)
            break
        else:
            data, *_ = stack.pop().values()
            set_to_value_of_root(data,stack)
            break
    else:
        new_object(str.lstrip(),level,stack)

def change_to_dict(object,stack=[]):
    if(len(object) < 1):
        data = list(stack.pop().values())[0]
        return data
    check_keyword(object[0],stack)    
    return change_to_dict(object[1:],stack)

key = {}
stack = []
string_array = ob.split("\n")
result = change_to_dict(string_array)
print(json.dumps(result,indent=4))