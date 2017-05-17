##eng2sp={}
##eng2sp ["one"] = "uno"
##eng2sp ["two"] = "dos"
##print(eng2sp)

##nhva ={}
##nhva ["apples"] = 430
##nhva ["bananas"] = 312
##nhva ["oranges"] = 525
##nhva ["peaes"] = 217
##print(nhva)

## 1 Dang khac cua kieu tu dien.
eng2sp = {"one":"uno","two":"dos","three":"tres"}
##print(eng2sp["one"])

##inventory = {"apples":430,"bananas":312,"oranges":525,"pears":217}
##print(inventory)
##del inventory["pears"]
##print(inventory)
##inventory ["pears"] = 0
##print(inventory)
##inventory ["bananas"] +=200
##print(inventory)
##len(inventory)

##for k in eng2sp.keys(): # The order of the k’s is not defined
##    print("Got key", k, "which maps to value", eng2sp[k])
##    ks = list(eng2sp.keys())
##    print(ks)

##for k in eng2sp:
##    print("Got key",k)
##    list(eng2sp.values())
##    v = ["Tres", "dos", "uno"]
##    list(eng2sp.items())
##    [("three", "tres"), ("two", "dos"), ("one", "uno")]
##    for (k,v) in eng2sp.items():
##        print("Got",k,"that maps to",v)

opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy()
