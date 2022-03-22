import json
import re
import sys

data = []
try:
    with open('solution.json') as f:
        content = f.readlines()
        try:
            for line in content:
                data.append(json.loads(line))
        except Exception as e:
            text = content
            if text[0] == "NO-SOLUTION":
                print("PASSED")
                pass
            else:
                print(f"FAILED |File should be list of jsons (key value are string) OR plain text as NO-SOLUTION (without string quotes) | Error : {e}")
            sys.exit()
except Exception as e:
    print(f"not able to read solution.json | Error : {str(e)}")
    sys.exit()

try:
    assert type(data)==type([]),"FAILED | Not able to read file as a list of solutions, make sure every assignment is in different line"

    assert data != [],"FAILED | Empty Json found, write NO-SOLUTION in the file."

    for line,sol in enumerate(data):
        assert type(sol)==type({}), f"FAILED | Every solution line should be json | Error in line | {line+1}"
        for key,value in sol.items():
            assert type(key)==type(""),f"FAILED | Key should be of string form | Error in line {line+1} | key : {key}"
            assert type(value) == type(""), f"FAILED | Value should be of string form | Error in line {line+1} | value : {value}"
            k = re.compile(r"[0-9]+").sub("##",key)
            assert k=="N##_##", f"FAILED | Key should be of N#_# where # is number (0,1...) form | Error in line {line} | key : {key}"
            assert value in ["R","M","A","E"], f"FAILED | Value should be one of the following - A,E,M,R | Error in line {line} | value : {value}"

except AssertionError as e:
    print(e)
    sys.exit()

print("PASSED")