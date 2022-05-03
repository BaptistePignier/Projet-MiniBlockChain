from Objects import *

block = Block(1,"-000-vemvkcrwvyev-000-")
block.Validate(5)
print(block.start_key)
print(block.getContent())
print(block.end_key)
