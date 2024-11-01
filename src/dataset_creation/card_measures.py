# Modify measurements as needed
cardWidth = 56
cardHeight = 94  
cornerXmin = 1  # From left side of the card to the desired bounding box
cornerXmax = 17  # From left side of the card to the desired bounding box end
cornerYmin = 2  # From top side of the card to the desired bounding box
cornerYmax = 19  # From top side of the card to the desired bounding box end

# We convert the measures from mm to pixels: multiply by an arbitrary factor 'zoom'
# You shouldn't need to change this
zoom = 4
cardWidth *= zoom
cardHeight *= zoom
cornerXmin = int(cornerXmin * zoom)
cornerXmax = int(cornerXmax * zoom)
cornerYmin = int(cornerYmin * zoom)
cornerYmax = int(cornerYmax * zoom)
