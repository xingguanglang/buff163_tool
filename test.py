

class buff_item_deep_partition(object):
    def __init__(self,interval):
        super().__init__()
        self.wear_check_list = []
        self.max_wear = 0.1499
        self.min_wear = 0.07
        for i in range(int((self.max_wear-self.min_wear)/interval)):
            self.wear_check_list.append(f"{'{:.3f}'.format(i*interval+self.min_wear)}")
        self.wear_check_list.append(self.max_wear)