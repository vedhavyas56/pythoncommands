items=['pen','paper','mobile','tv','mouse','fan']
print("\n printing the values by using index :")
result=items.index('tv')
print(result)

item='pen'
if items in items:
    result=item.index("item")
    print(f"thr (item)has an index of {result}")
else:
    print(f"{item} does't existin the given list.")
    

items=['pen','paper','mobile','tv','mouse','fan']  
print("\n printing the values by using iter")
items_iter=iter(items)
item=next(items_iter)
print(item)



items=['pen','paper','mobile','tv','laptop','mouse','keyboard','fan','light','switch']
print("\n Printing the Values by Using Iter: ")
items_iter=iter(items)
item=next(items_iter)
print(item)

item=next(items_iter)
print(item)


item=next(items_iter)
print(item)



item=next(items_iter)
print(item)

item=next(items_iter)
print(item)

item=next(items_iter)
print(item)

