stocks ={
    "info" : [600,630,620],
    "ril" : [1430,1490,1567],
    "mtl" : [234,180,160],
}



def print_info_avg(dcts):
    for keys, values in dcts.items():
        total = 0
        for x in values:
            total += x
            avg = total / len(values)

        print("{} ==> {} ==> avg: {:.2f}".format(keys, values, avg))

print_info_avg(stocks)


##faced problem
def add_dict(dct):
    user_input = input("Enter stocks name: [tata,500]", )
    stocks_name, share_values = user_input.split(",")
    share_values = int(share_values)

    if stocks_name in stocks:
        stocks[stocks_name].append(share_values)
    else:
        stocks[stocks_name] = [share_values]


add_dict(stocks)
print(stocks)




