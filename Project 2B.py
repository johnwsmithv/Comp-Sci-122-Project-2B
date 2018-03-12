#Google API
import urllib.request

def GoogleMaps(origin,destination):
    orgcity,orgstate= origin.split(',')
    destcity,deststate = destination.split(',')
    orgcity = orgcity.strip()
    orgstate = orgstate.strip()
    destcity = destcity.strip()
    deststate = deststate.strip()
    if " " in orgcity:
        orgcity = orgcity.replace(' ','+')
    elif " " in destcity:
        destcity = destcity.replace(' ','+')
    print(orgcity, orgstate)
    print(destcity, deststate)
    web_obj = urllib.request.urlopen(
        "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s+%s&destinations=%s+%s&mode=driving&sensor"
        "=false" % (orgcity,orgstate,destcity,deststate))
    results_str = str(web_obj.read())
    print(results_str)
    web_obj.close()
    #my name is john smith
    #Jake is not the goat

def main():
    origincity = str(input("Enter your City and State of Origin, seperated by a comma: "))
    destinationcity = str(input("Enter your Destination City and State, seperated by a comma: "))
    GoogleMaps(origincity,destinationcity)

main()
