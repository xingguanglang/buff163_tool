
class item(object):
    def __init__(self,name,wear,price,time):
        self.name = name
        self.wear = wear
        self.price = price
        self.time = time
    def show_info(self):
        print("枪类：",self.name,"磨损：",self.wear,"价格：",self.price,"获取时间：",self.time)

class market_url(object):
    def __init__(self,rarity,quality,exterior,itemset):
        self.rarity = rarity
        self.quality = quality
        self.exterior = exterior
        self.itemset = itemset 
        self.url = f'https://buff.163.com/market/csgo#game=csgo&page_num=1&rarity={self.rarity[0]}&quality={self.quality[0]}&exterior={self.exterior[0]}&itemset={self.itemset[0]}&tab=selling'


class buff_item(object):
    def __init__(self,name,exterior,buff_id,itemset,rarity):

        self.name = name
        self.buff_id = buff_id
        self.exterior = exterior
        self.itemset = itemset
        self.rarity = rarity

        if exterior == "崭新出厂":
            self.min_wear = 0.00
            self.max_wear = 0.06999
        elif exterior == "略有磨损":
            self.min_wear= 0.07
            self.max_wear = 0.14999
        elif exterior == "久经沙场":
            self.min_wear = 0.15
            self.max_wear = 0.37999
        elif exterior == "破损不堪":
            self.min_wear = 0.38
            self.max_wear = 0.44999
        elif exterior == "战痕累累":
            self.min_wear = 0.45
            self.max_wear = 0.9999
        else:
            print ("undefined type")

    def show_info(self):
        print(f"name:{self.name}, exterior:{self.exterior}, buff_id:{self.buff_id}, itemset:{self.itemset}, rarity:{self.rarity}")

class itemset(object):


    def __init__(self,itemset_name:str,buff_items:list[buff_item]):
        self.name = itemset_name
        self.coverts = []
        self.classified = []
        self.restricted = []
        self.mil_specs = []
        self.industrials = []
        self.consummers = []
        element = []
        for i in buff_items:
            if i.itemset == itemset_name:
                element.append(i)
        for i in element:
            if i.rarity == "隐蔽":
                self.coverts. append(i)
            elif i.rarity == "保密":
                self.classified.append(i)
            elif i.rarity == "受限":
                self.restricted. append(i)
            elif i.rarity == "军规级":
                self.mil_specs. append(i)
            elif i.rarity == "工业级":
                self.industrials. append(i)
            elif i.rarity == "消费级":
                self.consummers. append(i)

    def flatten(self):
        temp = []
        for i in self.coverts:
            if i.name not in temp:
                temp.append(i.name)

        self.coverts = temp
        temp = []

        for i in self.classified:
            if i.name not in temp:
                temp.append(i.name)
        self.classified = temp
        temp = []
        for i in self.restricted:
            if i.name not in temp:
                temp.append(i.name)
        self.restricted = temp
        temp = []

        for i in self.mil_specs:
            if i.name not in temp:
                temp.append(i.name)
        self.mil_specs = temp
        temp = []

        for i in self.industrials:
            if i.name not in temp:
                temp.append(i.name)
        self.industrials = temp
        temp = []

        for i in self.consummers:
            if i.name not in temp:
                temp.append(i.name)
        self.consummers = temp
        return

class deep_partition(buff_item):
    def __init__(self,buff_item:buff_item,interval=0.01):
        self.wear_check_list = []
        self.buff_item = buff_item
        self.interval = interval
        super().__init__(buff_id=buff_item.buff_id,name=buff_item.name,exterior=buff_item.exterior,itemset=buff_item.itemset,rarity=buff_item.rarity)
        
        for i in range(int((self.max_wear-self.min_wear)/interval)+1):
            self.wear_check_list.append(f"{'{:.3f}'.format(i*interval+self.min_wear)}")
        self.wear_check_list.append(f"{'{:.3f}'.format(self.max_wear)}")
    
def create_itemset_by_listing(name:str,covert:list,classified:list,restricted:list,mil_spec:list,industrials:list,consumers:list):
    result = itemset(name,[])
    result.coverts = covert
    result.classified = classified
    result.restricted = restricted
    result.mil_specs = mil_spec
    result.industrials = industrials
    result.consumers = consumers
    return result