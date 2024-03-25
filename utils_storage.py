import json
from item import item,buff_item,deep_partition,itemset,create_itemset_by_listing,tradeupitem
from datetime import datetime
from os import listdir
def convert_dictlist_to_tradeupitem(dictlist:list[dict]):
    result = []
    for i in dictlist:
        name = i['name']
        bfitem = read_buff_item_from_json("json/buff_items_"+name+" _.json")[0]
        result.append(tradeupitem(bfitem,item(bfitem.name,-1,-1,-1,-1),i['minwear'],i['maxwear']))
    # print("result:",result)
    return result
def convert_dictlist_to_item(dictlist:list[dict]):
    result = []
    for i in dictlist:
        result.append(item(i['name'],i['wear'],i['price'],i['itemset'],i['time']))
    return result

def convert_dictlist_to_itemset(dictlist:list[dict]):
    i = dictlist
    return create_itemset_by_listing(i['name'],i['coverts'],i['classified'],i['restricted'],i['mil_spec'],i['industrials'],i['consumers'])
    

def convert_dictlist_to_itemset_all(dictlist:list[dict]):
    result = []
    for i in dictlist:
        tmp=create_itemset_by_listing(i['name'],i['coverts'],i['classified'],i['restricted'],i['mil_spec'],i['industrials'],i['consumers'])
        result.append(tmp)
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
    wears = []
    filepath = filedir + filename + "_" + items[0].name +"_.json"
    buffer = read_item_from_json(filepath)
    items_wear = [e.wear for e in items]
    temp = []
    if buffer != -1:
        for test in buffer:
            if test.wear not in items_wear:
                temp.append(test)
    items = temp + items

    for test in items:
        if test.wear not in wears:
            wears.append(test.wear)
    wears.sort()
    for i in wears:
        for test in items:
            if test.wear == i:
                if test.name not in namedic.keys():
                    namedic[test.name] = []
                namedic[test.name].append({"name":test.name,"wear":float(test.wear),"price":test.price,"itemset":test.itemset,"time":test.time})
    
    
    for x in namedic.keys():
        # filepath = filedir + filename + "_" + x +datetime.now().strftime("-%Y-%m-%d_%H_%M_%S.json")
        filepath = filedir + filename + "_" + x +"_.json"
        with open(filepath,'w',encoding="utf-8") as f:
            for i in namedic[x]:
                tmp = json.dumps(i,ensure_ascii=False)
                f.write(tmp+'\n')
        f.close()

def write_itemset_to_json(itemsets:list[itemset],filedir="json/",filename="sets"):
    namedic = {}
    for test in itemsets:
        test.flatten()
        if test.name not in namedic.keys():
            namedic[test.name] = []
        namedic[test.name].append({"name":test.name,"coverts":test.coverts,"classified":test.classified,"restricted":test.restricted,"mil_spec":test.mil_specs,"industrials":test.industrials,"consumers":test.consummers})
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
        filepath = filedir + filename + "_" + test.name +"_.json"
        buffer = read_buff_item_from_json(filepath)
        idlist = []
        if buffer != -1:
            for i in buffer:
                idlist.append(i.buff_id)
        if test.name not in namedic.keys():
            namedic[test.name] = []
        if test.buff_id not in idlist:
            namedic[test.name].append({'name':test.name,'exterior':test.exterior,"buff_id":test.buff_id,"itemset":test.itemset,"rarity":test.rarity})
        if buffer != -1:
            for temp in buffer:

                namedic[test.name].append({'name':temp.name,'exterior':temp.exterior,"buff_id":temp.buff_id,"itemset":temp.itemset,"rarity":temp.rarity})

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
        filepath = filedir + filename + "_" + test.name +"_.json"
        buffer = read_deep_partition_from_json(filepath)
        idlist = []
        if buffer != -1:
            for i in buffer:
                idlist.append(i.buff_id)
        if test.name not in namedic.keys():
            namedic[test.name] = []
        if test.buff_id not in idlist:
            namedic[test.name].append({'name':test.name,'exterior':test.exterior,"buff_id":test.buff_id,"itemset":test.itemset,"rarity":test.rarity,"interval":test.interval})
        if buffer != -1:
            for temp in buffer:
                namedic[test.name].append({'name':temp.name,'exterior':temp.exterior,"buff_id":temp.buff_id,"itemset":temp.itemset,"rarity":temp.rarity,"interval":temp.interval})

    for x in namedic.keys():
        # filepath = filedir + filename + "_" + x +datetime.now().strftime("-%Y-%m-%d_%H_%M_%S.json")
        filepath = filedir + filename + "_" + x +"_.json"
        
        with open(filepath,'w',encoding="utf-8") as f:
            for i in namedic[x]:

                tmp = json.dumps(i,ensure_ascii=False)
                f.write(tmp+'\n')
        f.close()

def write_deep_partition_to_json1(deep_partitions:list[deep_partition],filedir="json/",filename="deep_partitions"):

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
def read_wear_list(filepath="wear_list.json"):
    result = []
    try:
        with open(filepath,'r',encoding="utf-8") as f:
            tmp = f.read().split('\n')[:-1:]
        for x in tmp:
            result.append(json.loads(x))
        result = convert_dictlist_to_tradeupitem(result)
        # print(111111)
        f.close()
    except:
        return result
        
    return result


def read_deep_partition_from_json(filepath="json/deep_partition.json"):
    result = []
    try:
        with open(filepath,'r',encoding="utf-8") as f:
            tmp = f.read().split('\n')[:-1:]
        for x in tmp:
            result.append(json.loads(x))
        print(result)
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

def read_itemset_from_all_json(filedir = "json/"):
    result = [ ]
    x = listdir(filedir)
    for i in x:
        if i[0] == "s":        
            try:
                with open(filedir+i,'r',encoding="utf-8") as f:
                    tmp = f.read().split('\n')[:-1:]
                f.close()
                for y in tmp:
                    result.append(json.loads(y))
            except:
                return result
    result = convert_dictlist_to_itemset_all(result)
    return result


def read_itemset_from_json(filepath = "json/set.json"):
    with open(filepath,'r',encoding="utf-8") as f:
        tmp = f.read().split('\n')[:-1:]
    for x in tmp:
        result = json.loads(x)
    result = convert_dictlist_to_itemset(result)
    f.close()
    return result
        
    # return result

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
        return -1
        
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
        return -1
        
    return result

def read_buff_item_from_all_json(filedir = "json/"):
    result = []
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

if __name__ == "__main__":
    # a = read_buff_item_from_json("json/buff_items_双持贝瑞塔 | 血红蛋白 _.json")
    # write_buff_item_to_json(a)
    1