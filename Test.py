



# class SV:
#     code:int
#     name:str
#     ns:str
#     mh1:float
#     mh2:float
#     mh3:float
#     def __init__(self, code, name, ns, mh1, mh2, mh3):
#         self.code = code
#         self.name = name
#         self.ns = ns
#         self.mh1 = mh1
#         self.mh2 = mh2
#         self.mh3 = mh3
#     def tongDiem(self):
#         return self.mh1 + self.mh2 + self.mh3
#     def __str__(self):
#         return self.code + " " + self.name + " " + self.ns + " " + '%.1f' % self.tongDiem()



# if __name__ == '__main__':
#     ls = list()
#     for t in range(int(input())):
#         x = SV(t + 1, input(), input(), float(input()), float(input()), float(input()))
#         ls.append(x)
#     ls.sort(key=lambda x : -x.tongDiem())
#     for i in ls:
#         print(i)
# def checkstring(st1, st2, st3):

#   if st1.startswith(st2) or st1.endswith(st3):
#     print('True')
#   else:
#     print('False ')

# if _name_ == "_main_":
#   st1 = input()
#   st2 = input()
#   st3 = input()

# (checkstring(st1, st2, st3))


while True:
    print('Enter your age:')
    age=input()
    if age.isdecimal():
        break
    print("t")