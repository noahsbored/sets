ours = {"LAX", "JFK", "CDG", "DXB"}
theirs = {"JFK", "CDG", "LHR", "BKK"}


common = ours.intersection(theirs)
print("Destinations that both airlines fly to:", common)

e
unique = ours.difference(theirs)
print("Destinations unique to our airline:", unique)


unique_theirs = theirs.difference(ours)
print("Destinations unique to competitor airline:", unique_theirs)

neither = ours.symmetric_difference(theirs)
print("Destinations that neither airline shares:", neither)
