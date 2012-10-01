#!/usr/bin/python
import OsmApi
import csv

date_from="2011-10-03T00:00:00Z"
date_to="2011-10-10T00:00:00Z"
users = ["Alcin Stevenson", "jean presler", "WingedStone", "Guensmork", "richelet",
         "bonhommebrunie", "jeandany", "jeune", "rlouino", "wilner",
         "lubin nancy", "wilford", "Perest Jonas", "senatusgesner",
         "vetillac seneque", "jaakkoh", "Heurtelou",
         "Tinono", "nadege michaud", "fenel", "ALCE SamuelPaul",
         "worldwidewolford", "wonderchook", "Mdr", "MJNcs", "lyonel_lav", "Marion Barry",
         "patricia_beauvoir", "Souvenise Saint-Jean", "Gine", "alexis josy",
         "eustache70", "Adler Salvador", "SergeDorval", "pierre eddy",
         "Wildbill", "rab", "manic12"
        ]
 
# Haiti bbox: min_lon=-74.83, max_lon=-72.49, min_lat=17.4, max_lat=20.43
# PaP bbox: min_lon=-72.452, max_lat=18.672, max_lon=-71.178, min_lat=18.468

def getChangesets(username=None, min_lon=-74.83, min_lat=17.4, max_lon=-71.49, max_lat=20.43):
    changesets = osmApi.ChangesetsGet(min_lon, min_lat, max_lon, max_lat,
            username=username, closed_after=date_from,
            created_before=date_to)
    return changesets
    
def getChangesetStats(cid):
    stat= {"node":0, "way":0, "relation":0}
    for changesetData in osmApi.ChangesetDownload(cid):
#     if(changesetData["action"] == "create")
        if changesetData["type"] == "node" :
            stat["node"] += 1
        elif changesetData["type"] == "way":
            stat["way"] += 1
        elif changesetData["type"] == "relation":
            stat["relation"] += 1    
        elif(true):
            s = 'unexpected data:' + str(changesetData["type"])
            str( s)
    return stat

def updateStat(dict1, dict2):
    return dict((n, dict2.get(n, 0)+ dict2.get(n, 0)) for n in set(dict1)|set(dict2))
    

#
# Action begins here!
#print "Seb's stats script v0.4"
str( "Seb's stats script v0.4")
osmApi = OsmApi.OsmApi()
csv = open('stats.csv', 'wb')
for user in users:
    stats = {"node": 0, "way":0, "relation":0}
    #print "Checking changesets for " + str(user)
    str("Checking changesets for " + str(user))
    changesets = getChangesets(username=user)
    for id in changesets:
        csstat= getChangesetStats(id)
        stats["node"] += csstat["node"]
        stats["way"]  += csstat["way"]
        stats["relation"] += csstat["relation"] 
#        stats = updateStat(stats, getChangesetStats(id))
#    print user + ", " + str(len(changesets)) + ", " + str(stats["node"]) + ", " + str(stats["way"]) + ", " + str(stats["relation"])
    csv.write(str(user) +", " + str(len(changesets)) + ", " + str(stats["node"]) + ", " + str(stats["way"]) + ", " + str(stats["relation"]) + "\n")
    csv.flush()
csv.close()
#print "Done."
"Done."