class ind ():
    def mlang(self):
        print ("hindi")
    def cap(self):
        print("new delhi")
    def type(self):
        print("developing \n\n")
class usa():
    def mlang(self):
        print ("english")
    def cap(self):
        print("washington dc")
    def type(self):
        print("developed")
india = ind()
us = usa()
for c in (india,us):
    c.mlang()
    c.cap()
    c.type()
