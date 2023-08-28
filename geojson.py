import json


with open('KYgeojson.json') as f:
        jdata = json.load(f)
        
coord_1 = jdata['features'][0]['geometry']['coordinates'][0][0]
coord_2 = jdata['features'][0]['geometry']['coordinates'][0][1]
coord_3 = jdata['features'][0]['geometry']['coordinates'][0][2]
coord_4 = jdata['features'][0]['geometry']['coordinates'][0][3]
coord_5 = jdata['features'][0]['geometry']['coordinates'][0][4]

coord_list = [coord_1, coord_2, coord_3, coord_4, coord_5]

coord = jdata['features'][0]['geometry']['coordinates'][0]

#for i in coord:
#    print(i)

coord_set = jdata['features']

coord_set_list = []

for i in coord_set:
    coord_set_list.append(i)

coord_type = jdata['features'][0]['geometry']['type']

def coord_bot(coordinates, coordinate_type):
    
    for i in coordinates:    
        print(f'{coordinate_type} #{coordinates.index(i) + 1} of {len(coordinates)}')
        print(f"Number of coordinates in {coordinate_type}: {len(i['geometry']['coordinates'][0])}")
        print(f'{i}\n')

#coord_bot(coord_set_list, coord_type)


def coord_permimeter(coordinates):
    i = coordinates['geometry']['coordinates'][0]
    print(i)
    num_of_coord = len(i)
    perimeter = 0

    for x in range(0, (num_of_coord - 1)):
        
        # slope calculator
        x_run = i[x+1][0] - i[x][0]
        y_rise = i[x+1][1] - i[x][1]
        m = y_rise / x_run

        # distance calculator
        distance = ((x_run**2) + (y_rise**2))**0.5
        perimeter += distance
        
        print(f'Line# {x+1}')
        print(f'Slope: {round(m, 4)}')
        print(f'Distance: {round(distance, 8)}\n')

    print(f'Perimeter of Polygon: {perimeter}')
    

coord_permimeter(coord_set_list[0])