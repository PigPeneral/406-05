import random as rm
class TBSp:
  def __init__(self, name, oshi):
    self.name = name
    self.oshi = oshi
  def ch13(self):
    print(f"{self.oshi}" + " " + f"{"好き" * rm.getrandbits(6)}")
mikotoBOT = TBSp("ch13", "美琴")
mikotoBOT.ch13()