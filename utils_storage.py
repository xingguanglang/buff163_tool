import json
from item import item,buff_item
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



def write_item_to_json(items:list[item],filepath="json/storage.json"):
    temp = []
    for test in items:
        
        temp.append({"name":test.name,"wear":test.wear,"price":test.price,"time":test.time})
    with open(filepath,'w',encoding="utf-8") as f:
        for x in temp:
            tmp = json.dumps(x,ensure_ascii=False)
            f.write(tmp+'\n')
    f.close()

def write_buff_item_to_json(buff_items:list[buff_item],filepath="json/buff_item.json"):
    temp = []
    for test in buff_items:
        temp.append({'name':test.name,'exterior':test.exterior,"buff_id":test.buff_id,"itemset":test.itemset,"rarity":test.rarity})
    with open(filepath,'w',encoding="utf-8") as f:
        for x in temp:
            tmp = json.dumps(x,ensure_ascii=False)
            f.write(tmp+'\n')
    f.close()
    return

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


name_dic = {
    ("AK-47_前线迷雾",1):buff_item(buff_id=33905,exterior="崭新出厂",name="AK-47_前线迷雾",itemset="千瓦",rarity="隐蔽"),
    ("AK-47_前线迷雾",2):buff_item(buff_id=33907,exterior="略有磨损",name="AK-47_前线迷雾",itemset="千瓦",rarity="隐蔽")
}
# buff_item_list = [buff_item(buff_id=33905,type=1,name="AK-47_前线迷雾"),buff_item(buff_id=33907,type=2,name="AK-47_前线迷雾")]
# items = [item("我",1,1,12)]

# write_item_to_json(items)
# result = read_item_from_json()
# print(result[0].name)

if __name__ == "__main__":


    
    buff_item_list = [buff_item(buff_id=33905,exterior="崭新出厂",name="AK-47_前线迷雾",itemset="千瓦",rarity="隐蔽"),buff_item(buff_id=33907,exterior="略有磨损",name="AK-47_前线迷雾",itemset="千瓦",rarity="隐蔽")]
    write_buff_item_to_json(buff_item_list)
    result = read_buff_item_from_json()
    print("finish")