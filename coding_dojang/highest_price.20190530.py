products = input()
a_list = list(map(int, products.split(";")))
a_list.sort(reverse=True)
for i in a_list:
    print("{0:>9,}".format(i))
