from time import sleep
class Bird(object):
    def chirp(self,sound):
        print(sound)
    def set_color(self,color):
        self.color=color

summer=Bird()

summer.set_color("hello")

print(summer.color)

class hon(object):
    def one(self):
        print("song")
class son(hon):
    def one(self):
        super().one()
        print("hello")

qq = hon()
qq.one()

two= son()
two.one()

def gen():
    a=100
    yield a
    a=a*8
    yield a
    yield 1000
for i in gen():
    print(i)

f = open("new.txt","w")
print(f.closed)

f.write ("hello,world")
f.close()
print(f.closed)

with open("new.txt","w") as f:
    f.write("hello mengejie")
