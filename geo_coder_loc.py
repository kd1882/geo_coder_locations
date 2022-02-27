import geocoder

def main():
  # Declare destinations list here
  destinations = ['Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge']

  # Loop through each destination
  for destination in destinations:
    #   Get the lat-long coordinates from `geocoder.arcgis`
    #   Print out the place name and the coordinates
    location = geocoder.arcgis(destination)
    # Variables to split up lat and lng so they're able to be formatted
    loc_lat = location.lat
    loc_lng = location.lng
    print(f'{destination} is located at ({loc_lat:.4f}, {loc_lng:.4f})')

main()
