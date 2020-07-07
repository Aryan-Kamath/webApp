## a map or hash table
##I can set up a captains = {}, where curly brackets indicates an empty dictionary
captains = {}


captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"


for ship in captains:
    print(ship + ":" + captains[ship])