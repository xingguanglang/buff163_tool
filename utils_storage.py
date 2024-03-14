import json
from item import item,buff_item,deep_partition
from datetime import datetime
from os import listdir
def convert_dictlist_to_item(dictlist:list[dict]):
    result = []
    for i in dictlist:
        result.append(item(i['name'],i['wear'],i['price'],i['time']))
    return result

def convert_dictlist_to_buff_item(dictlist:list[dict]):
    result = []
    for i in dictlist:
        result.append(buff_item(i['name'],i["exterior"],i["buff_id"],i["itemset"],i["rarity"]))
    return result

def convert_dictlist_to_deep_partition(dictlist:list[dict]):
    result = []
    for i in dictlist:
        tmp = buff_item(i['name'],i["exterior"],i["buff_id"],i["itemset"],i["rarity"])
        result.append(deep_partition(tmp,i["interval"]))
    return result

def write_item_to_json(items:list[item],filedir="json/",filename="items"):
    namedic = {}
    for test in items:
        if test.name not in namedic.keys():
            namedic[test.name] = []
        namedic[test.name].append({"name":test.name,"wear":test.wear,"price":test.price,"time":test.time})
    for x in namedic.keys():
        # filepath = filedir + filename + "_" + x +datetime.now().strftime("-%Y-%m-%d_%H_%M_%S.json")
        filepath = filedir + filename + "_" + x +"_.json"
        with open(filepath,'w',encoding="utf-8") as f:
            for i in namedic[x]:
                tmp = json.dumps(i,ensure_ascii=False)
                f.write(tmp+'\n')
        f.close()

def write_buff_item_to_json(buff_items:list[buff_item],filedir="json/",filename="buff_items"):
    namedic = {}
    for test in buff_items:
        if test.name not in namedic.keys():
            namedic[test.name] = []
        namedic[test.name].append({'name':test.name,'exterior':test.exterior,"buff_id":test.buff_id,"itemset":test.itemset,"rarity":test.rarity})
    for x in namedic.keys():
        # filepath = filedir + filename + "_" + x +datetime.now().strftime("-%Y-%m-%d_%H_%M_%S.json")
        filepath = filedir + filename + "_" + x +"_.json"
        with open(filepath,'w',encoding="utf-8") as f:
            for i in namedic[x]:
                tmp = json.dumps(i,ensure_ascii=False)
                f.write(tmp+'\n')
        f.close()
    return

def write_deep_partition_to_json(deep_partitions:list[deep_partition],filedir="json/",filename="deep_partitions"):

    namedic = {}
    for test in deep_partitions:
        if test.name not in namedic.keys():
            namedic[test.name] = []
        namedic[test.name].append({'name':test.buff_item.name,'exterior':test.buff_item.exterior,"buff_id":test.buff_item.buff_id,"itemset":test.buff_item.itemset,"rarity":test.buff_item.rarity,"interval":test.interval})
    for x in namedic.keys():
        # filepath = filedir + filename + "_" + x +datetime.now().strftime("-%Y-%m-%d_%H_%M_%S.json")
        filepath = filedir + filename + "_" + x +"_.json"
        with open(filepath,'w',encoding="utf-8") as f:
            for i in namedic[x]:
                tmp = json.dumps(i,ensure_ascii=False)
                f.write(tmp+'\n')
        f.close()

def read_deep_partition_from_json(filepath="json/deep_partition.json"):
    result = []
    try:
        with open(filepath,'r',encoding="utf-8") as f:
            tmp = f.read().split('\n')[:-1:]
        for x in tmp:
            result.append(json.loads(x))
        result = convert_dictlist_to_deep_partition(result)
        f.close()
    except:
        return result
        
    return result

def read_deep_partition_from_all_json(filedir = "json/"):
    result = [ ]
    x = listdir(filedir)
    for i in x:
        if i[0] == "d":        
            try:
                with open(filedir+i,'r',encoding="utf-8") as f:
                    tmp = f.read().split('\n')[:-1:]
                f.close()
                for y in tmp:
                    result.append(json.loads(y))
            except:
                return result
    result = convert_dictlist_to_deep_partition(result)
    return result

def read_item_from_json(filepath = "json/storage.json"):
    result = []
    try:
        with open(filepath,'r',encoding="utf-8") as f:
            tmp = f.read().split('\n')[:-1:]
        for x in tmp:
            result.append(json.loads(x))
        result = convert_dictlist_to_item(result)
        f.close()
    except:
        return result
        
    return result

def read_buff_item_from_json(filepath="json/buff_item.json"):
    result = []
    try:
        with open(filepath,'r',encoding="utf-8") as f:
            tmp = f.read().split('\n')[:-1:]
        for x in tmp:
            result.append(json.loads(x))
        result = convert_dictlist_to_buff_item(result)
        f.close()
    except:
        return result
        
    return result

def read_buff_item_from_all_json(filedir = "json/"):
    result = [ ]
    x = listdir(filedir)
    for i in x:
        if i[0] == "b":        
            try:
                with open(filedir+i,'r',encoding="utf-8") as f:
                    tmp = f.read().split('\n')[:-1:]
                f.close()
                for y in tmp:
                    result.append(json.loads(y))
            except:
                return result
    result = convert_dictlist_to_buff_item(result)
    return result