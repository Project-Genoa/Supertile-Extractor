import os
import extractor

# Quale be like: nooooooooo you can't just bomb your filesystem like that
# Me: haha 8TB go brrrrrrrrrrrrrrr

for supertile in os.listdir('./'):
    if (supertile.split('.')[-1] == 'tiles'):
        extractor.extractSupertile(supertile)