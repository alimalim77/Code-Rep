
class ProductOfNumbers:

    def __init__(self):
        self.pref = [1]
        

    def add(self, num: int) -> None:
        if not num:
            self.pref = [1]
        else:
            last = self.pref[-1]
            self.pref.append(last*num)
            # if not self.pref:
            #     self.pref.append(num)
            # else:
            #     last = self.pref[-1]
            #     self.pref.append(num*last)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref):
            return 0
        return self.pref[-1]//self.pref[len(self.pref)-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)