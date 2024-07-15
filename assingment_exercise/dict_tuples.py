info = {
    'china':143,
    'india': 136,
    'usa':32,
    'pakistan': 21
}

# print(dir(info))
# print(info.keys())

def print_dict(dct):
    for keys, values in info.items():
        print("{}==> {}".format(keys, values))

# print_dict(info)

def add_dict_info(dct):
    country_name = input("Enter country name: ", )
    if country_name in dct.keys():
        print("it already exists")
    else:
        country_population = int(input("Enter following country's population ",))
        dct.__setitem__(country_name, country_population)


# add_dict_info(info)
# print(info)

def remove_dict(dct):
    remove_item = input("Enter country name: ", )
    if remove_item in dct.keys():
        dct.pop(remove_item)
        print_dict(dct)
    else:
        Print("This one does not exists")

# remove_dict(info)


def query_dict(dct):
    country_name = input("Country name: ", )
    if country_name in dct.keys():
        print("Population of {} is {}".format(country_name, dct.__getitem__(country_name)))


query_dict(info)





