# Banner Area
def logo():
    banner = open("banner.txt","r")
    showbanner = banner.read()
    print(showbanner)
    banner.close()