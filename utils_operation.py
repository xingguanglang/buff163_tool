from item import item,buff_item

#value 和 load 两个列表, 使同样的物品的使用较新的价格 load是加载的旧list value是运行获取的新list
def remove_redundancy(value:list[item],loads:list[item]):
    wears = [x.wear for x in value]

    result = []
    result2 = []
    removelist = []
    for i in value:
        if i.wear not in wears:
            result.append(i)
        else:
            result.append(i)
            removelist.append(i.wear)
    
    for i in range(len(loads)):
        if loads[i].wear not in removelist:
            result2.append(loads[i]) 
    result = result2 + result

    return result
