class ProductOfNumbers(object):

    def __init__(self):
        self.pre_product_dict = dict()
        self.pre_product_dict[0] = 1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.pre_product_dict.clear()
            self.pre_product_dict[0] = 1
            return
        else:
            dict_len = len(self.pre_product_dict)
            self.pre_product_dict[dict_len] = self.pre_product_dict[dict_len - 1] * num

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.pre_product_dict) - 1:
            return 0
        else:
            dict_len = len(self.pre_product_dict) - 1
            left = self.pre_product_dict[dict_len - k]
            whole = self.pre_product_dict[dict_len]
            return whole // left

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)