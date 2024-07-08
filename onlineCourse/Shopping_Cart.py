#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    def _init_(self, name:str, price:int):
        self.name = name
        self.price = price


class ShoppingCart:
    def _init_(self):
        self.items = []
    
    def add(self, item:Item):
        self.items.append(item)
    
    def total(self) -> int:
        return sum(map(lambda x: x.price, self.items))
    
    def _len_(self):
        return len(self.items)
items = list(map(lambda x: Item(x[0], x[1]), (("bike", 1000), ("headphones", 100))))
cart = ShoppingCart()

for i in items:
    cart.add(i)
    print(f"""Added Item : {i.name} -> Price : {i.price}Cart Total : {cart.total()}Items in Cart : {len(cart)}""")

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()