import os
import jwt

class asshole:
    __gender = ''
    def __init__(self,claim,gender='helicopter'):
        self.claim = claim
        self.__gender = gender

    def say(self):
        print('I am %s, so %s'%(self.__gender,self.claim))

if __name__ == '__main__':
    crap = asshole('我是个傻逼','transgender')
    crap.say()


