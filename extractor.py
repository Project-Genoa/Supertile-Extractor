import os

# Extract a Quale Supertile(tm)
def extractSupertile(supertileFile):
    supertileExtractionPath = os.path.join('./', supertileFile.split('.')[0])
    os.mkdir(supertileExtractionPath)

    tileRoot = [ int(supertileFile.split('_')[0]), int(supertileFile.split('_')[1].split('.')[0]) ]

    with open(supertileFile, 'rb') as file:
        # Read supertile data
        superTileData = file.read()

        # Split entire supertile data by PNG header
        splitTiles = superTileData.split(bytearray([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]))
        print(len(splitTiles[1:]), "tiles detected for extraction")

        # For calculating filename
        tileHorizontalIndex = 0
        tileVerticalIndex = 0
        tileIndex = 0
        for tile in splitTiles[1:]: # Remove 1st "tile" because it is actually the headers
            # Calculate filename
            tileName = str(tileRoot[0] + tileHorizontalIndex) + '_' + str(tileRoot[1] + tileVerticalIndex)

            print("Extracting supertile (" + supertileFile + "): [" + str(tileIndex+1) + '/' + str(len(splitTiles)-1) + '] - ' + tileName)

            # Create tile file
            with open(os.path.join(supertileExtractionPath, str(tileName) + '.png'), 'wb') as tileFile:
                tileFile.write(bytearray([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])) # Write PNG Header (removed during .split)
                tileFile.write(tile) # Write tile data

            if (tileHorizontalIndex < 63): # supertiles are 64x64
                tileHorizontalIndex += 1
            else:
                tileHorizontalIndex = 0
                tileVerticalIndex += 1
            
            tileIndex += 1

#extractSupertile('338_523.tiles')