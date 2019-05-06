hostList = []
import csv


def response(flow):
    #print("")
    #print("="*50)
    #print("FOR: " + flow.request.url)
    #print(flow.request.method + " " + flow.request.path + " " + flow.request.http_version)
    #print("-"*50 + "request headers:")
    with open("example2.csv", 'w') as file:

        for k, v in flow.request.headers.items():
            wr = csv.writer(file)
            if k == "Host":
                print("%-20s: %s" % (k.upper(), v))
                hostList.append(v)
                wr.writerow((hostList))

    print("the hostlist->>>")
    print(hostList)

    #print("-"*50 + "response headers:")
    #for k, v in flow.response.headers.items():
        #print("%-20s: %s" % (k.upper(), v))
        #print("-"*50 + "request headers:")

