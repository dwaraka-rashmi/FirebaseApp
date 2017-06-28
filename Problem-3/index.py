import sys
from config import db


# 1. The Total number of users that have "1" in the count array
def getUsersWithXCount(x):
    users_by_key = db.order_by_key().get()
    userCount = 0
    for l in users_by_key.each():
        val = db.child(l.key()).child('count').get()
        if 1 in val.val():
            userCount += 1
    print "The Total number of users that have \"1\" in the count array is ", userCount


# 2. The name of the users (user1,user2,user3, etc.) who have the "string":"hello world", as a key:value pair
def getUsersWithXPair(x):
    users_by_key = db.order_by_key().get()
    userList = []
    for l in users_by_key.each():
        if x.items()[0] in l.val().items():
            userList.append(l.key())
    print "The name of the users (user1,user2,user3, etc.) who have the \"string\":\"hello world\"," \
          " as a key:value pair are ", userList


# 3. The total number of users that have the "boolean" value as false
def getUsersWithBoolean(x):
    users_by_key = db.order_by_key().get()
    userCount = 0
    for l in users_by_key.each():
        val = db.child(l.key()).child('boolean').get().val()
        if val == x:
            userCount += 1
    print "The total number of users that have the \"boolean\" value as false is ", userCount


def printMenu():
    print "menu"
    print "1. The Total number of users that have \"1\" in the count array"
    print "2. The name of the users (user1,user2,user3, etc.) who have the \"string\":\"hello world\", as a key:value pair"
    print "3. The total number of users that have the \"boolean\" value as false"
    print "4. Show menu"


def main():
    printMenu()
    while True:
        com = raw_input('Command:').split()
        if len(com) == 0:
            print "invalid option"
            sys.exit(1)
        elif com[0] == "1":
            getUsersWithXCount(1)
        elif com[0] == "2":
            getUsersWithXPair({u'string': u'Hello World'})
        elif com[0] == "3":
            getUsersWithBoolean(False)
        elif com[0] == "4":
            printMenu()
        else:
            print "invalid option"
            sys.exit(1)


if __name__ == '__main__':
    main()