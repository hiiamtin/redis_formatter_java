import javaobj.v2 as javaobjv2
import datetime
import json
import struct
import ast

# data = sys.argv[1]
# pyobj = javaobjv2.loads(bytes.fromhex(data))
data = b'\xac\xed\x00\x05sr\x00-th.co.scb.fasteasy.common.model.ResponseModel\x8b\xe4\xdb\xa5\xd5\xfb\xc1\xf9\x02\x00\x01L\x00\x07dataObjt\x00\x12Ljava/lang/Object;xr\x002th.co.scb.fasteasy.common.model.BaseResponseObject\xfb\xba/\x84\xc6>\x126\x02\x00\x01L\x00\x06statust\x000Lth/co/scb/fasteasy/common/model/ResponseStatus;xpsr\x00.th.co.scb.fasteasy.common.model.ResponseStatus\xdd\xf7\x04E=\xe9\xe2\x9b\x02\x00\x03L\x00\x04codet\x00\x13Ljava/lang/Integer;L\x00\x0bdescriptiont\x00\x12Ljava/lang/String;L\x00\x06headerq\x00~\x00\x07xpsr\x00\x11java.lang.Integer\x12\xe2\xa0\xa4\xf7\x81\x878\x02\x00\x01I\x00\x05valuexr\x00\x10java.lang.Number\x86\xac\x95\x1d\x0b\x94\xe0\x8b\x02\x00\x00xp\x00\x00\x03\xe8t\x00\x07Successpsr\x00*th.co.scb.fasteasy.common.model.CustomerV2\xf3\xba\x10\xb5\xce\xab\xafp\x02\x00-L\x00\x0aatmCardRefq\x00~\x00\x07L\x00\x0fblockReasonCodeq\x00~\x00\x07L\x00\x16blockReasonDescriptionq\x00~\x00\x07L\x00\x10bulkActivateDatet\x00\x10Ljava/util/Date;L\x00\x0fbuzzebeeBaseURLq\x00~\x00\x07L\x00\x0cbuzzebeeHashq\x00~\x00\x07L\x00\x06cardIdq\x00~\x00\x07L\x00\x08cardTypeq\x00~\x00\x07L\x00\x0bcountryCodeq\x00~\x00\x07L\x00\x05emailq\x00~\x00\x07L\x00\x15emailNotificationFlagq\x00~\x00\x07L\x00\x15emailVerificationFlagq\x00~\x00\x07L\x00\x0bfastpayFlagq\x00~\x00\x07L\x00\x08languageq\x00~\x00\x07L\x00\x0alastNameENq\x00~\x00\x07L\x00\x0alastNameTHq\x00~\x00\x07L\x00\x0fmaskAccountFlagq\x00~\x00\x06L\x00\x0cmiddleNameENq\x00~\x00\x07L\x00\x0cmiddleNameTHq\x00~\x00\x07L\x00\x08mobileNoq\x00~\x00\x07L\x00\x16mutualFundTcAcceptDateq\x00~\x00\x0eL\x00\x19mutualFundTcAcceptVersionq\x00~\x00\x06L\x00\x06nameENq\x00~\x00\x07L\x00\x06nameTHq\x00~\x00\x07L\x00\x0epredictiveFlagq\x00~\x00\x07L\x00\x10profilePhotoPathq\x00~\x00\x07L\x00\x15promptpayTcAcceptDateq\x00~\x00\x0eL\x00\x18promptpayTcAcceptVersionq\x00~\x00\x07L\x00\x12referredFriendFlagq\x00~\x00\x07L\x00\x0fregisterCardRefq\x00~\x00\x07L\x00\x10registerCardTypeq\x00~\x00\x07L\x00\x0fregisterChannelq\x00~\x00\x07L\x00\x0cregisterDateq\x00~\x00\x0eL\x00\x0crelationFlagq\x00~\x00\x07L\x00\x07segmentq\x00~\x00\x07L\x00\x0ctcAcceptDateq\x00~\x00\x0eL\x00\x0ftcAcceptVersionq\x00~\x00\x06L\x00\x09themeFlagq\x00~\x00\x07L\x00\x07titleENq\x00~\x00\x07L\x00\x07titleTHq\x00~\x00\x07L\x00\x06userIdq\x00~\x00\x07L\x00\x08userModeq\x00~\x00\x07L\x00\x0auserStatusq\x00~\x00\x07L\x00\x08userTypeq\x00~\x00\x07L\x00\x18verificationRequiredFlagq\x00~\x00\x07xpppppt\x00\x7fhttps://extapigw-uat.scbeasy.com:8443/buzzebees/home.aspx?hash=B03E72C6EBA6B22AEEC10AC6B38BD32B35E706376CA8292AAF64E2E2FEE0A1DAt\x00@B03E72C6EBA6B22AEEC10AC6B38BD32B35E706376CA8292AAF64E2E2FEE0A1DAt\x00\x0d2563030200011t\x00\x02P1pt\x00\x17qatestall1234@gmail.comt\x00\x011t\x00\x010t\x00\x010t\x00\x02ent\x00\x06NUMJUNt\x00\x1b\xe0\xb8\x99\xe0\xb9\x89\xe0\xb8\xb3\xe0\xb8\x88\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\x97\xe0\xb8\xa3\xe0\xb9\x8csq\x00~\x00\x09\x00\x00\x00\x00t\x00\x00t\x00\x00t\x00\x0a0844031733pq\x00~\x00\x1bt\x00\x08WUTCHARAt\x00\x0f\xe0\xb8\xa7\xe0\xb8\xb1\xe0\xb8\x8a\xe0\xb8\xa3\xe0\xb8\xb0t\x00\x011psr\x00\x0djava.sql.Date\x14\xfaFh?5f\x97\x02\x00\x00xr\x00\x0ejava.util.Datehj\x81\x01KYt\x19\x03\x00\x00xpw\x08\x00\x00\x01\x81Ih\x96\x80xt\x00\x015ppppsr\x00\x12java.sql.Timestamp&\x18\xd5\xc8\x01S\xbfe\x02\x00\x01I\x00\x05nanosxq\x00~\x00#w\x08\x00\x00\x01k\xd0\xda\xd5\xf8x\x07\xedk@t\x00\x010psq\x00~\x00"w\x08\x00\x00\x01\x86\x13\x12\x1e\x80xsq\x00~\x00\x09\x00\x00\x00*t\x00\x011t\x00\x03LACt\x00\x0c\xe0\xb8\x88.\xe0\xb8\xad.\xe0\xb8\x95.t\x00\x1e001400000000000000000023595578t\x00\x0aINDIVIDUALt\x00\x01Pt\x00\x01Ct\x00\x010'
pyobj = javaobjv2.loads(data)
ob = pyobj.dump()

def convert_datetime(data: str):
    data_bytes = ast.literal_eval(data)
    input_num = struct.unpack('>Q', data_bytes)[0]
    date = datetime.datetime.fromtimestamp(input_num/1000)
    return date.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

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
        data = convert_datetime(data.strip())
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