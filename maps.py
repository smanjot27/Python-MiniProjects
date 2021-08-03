import csv
import gmplot
gmap=gmplot.GoogleMapPlotter(75.7861919,30.8787931,17)
gmap.apikey='AIzaSyAkd--ziFbKO0w7GuBGXLfgqAyW9--m7BY'
# k=0
# with open('Untitled_map.csv','r') as myfile:
#     read=csv.reader(myfile)
#     fields=next(read)
#     for row in read:
#         lat=float(row[0])
#         longg=float(row[1])
#         if k==0:
#             gmap.marker(lat,longg,'red')
#             k=1
#         else:
#             gmap.marker(lat,longg,'blue')
# gmap.marker(lat,longg,'yellow')
gmap.draw('mymap.html')

