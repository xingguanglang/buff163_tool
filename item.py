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
    
class deep_partition(object):
    def __init__(self,interval):
        super().__init__()
        self.wear_check_list = []
        self.max_wear = 0.1499
        self.min_wear = 0.07
        for i in range(int((self.max_wear-self.min_wear)/interval)):
            self.wear_check_list.append(f"{'{:.3f}'.format(i*interval+self.min_wear)}")
        self.wear_check_list.append(self.max_wear)