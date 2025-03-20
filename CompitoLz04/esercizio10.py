def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    marged_dict:dict=dict1
    for key, value in dict2.items():
        if key in marged_dict:
            marged_dict[key]+=value
        else:
            marged_dict[key]=value
    return marged_dict

print(merge_dictionaries({"x":5},{"y":-5}))