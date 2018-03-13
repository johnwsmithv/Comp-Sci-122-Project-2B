#Google API
import urllib.request

def GoogleMaps(origin,destination):
    #These splits split the city and state by the comma that is put into the input
    orgcity,orgstate= origin.split(',')
    destcity,deststate = destination.split(',')
    #The Strips get rid of any whitespace, so the names of the places can be put into the web address correctly
    orgcity = orgcity.strip()
    orgstate = orgstate.strip()
    destcity = destcity.strip()
    deststate = deststate.strip()
    #In order to deal with city names that have two words, like New York City, the whitespace needs to be filled with a + to work in the web address
    if " " in orgcity:
        orgcity = orgcity.replace(' ','+')
    elif " " in destcity:
        destcity = destcity.replace(' ','+')
    print(orgcity, orgstate)
    print(destcity, deststate)
    #These lines of code opens the Google API to the users speciifed inputs hence all of the %s to substitute for their inputs
    web_obj = urllib.request.urlopen(
        "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s+%s&destinations=%s+%s&mode=driving&sensor"
        "=false" % (orgcity,orgstate,destcity,deststate))
    results_str = str(web_obj.read())
    print(results_str)
    web_obj.close()

  #The main method runs the GoogleMaps method everytime the program is ran.
def main():
    origincity = str(input("Enter your City and State of Origin, seperated by a comma: "))
    destinationcity = str(input("Enter your Destination City and State, seperated by a comma: "))
    GoogleMaps(origincity,destinationcity)

main()
