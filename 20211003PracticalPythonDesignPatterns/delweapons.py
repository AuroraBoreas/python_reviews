txt = """
[Vision of Kobbel the Poetic]
[Vision of Mirren the Manipulator]
[Vision of Durio the Contemptuous]
[Vision of Baverne the Hunter]
[Vision of Asaliea the Channeler]
[Vision of Mouglon the Watchful]
[Vision of Haliver the Seeker]
[Vision of Belitrea the Blade of Want]
[Vision of Katarin the Bonecrusher]
[Vision of Azra the Sunslayer]
[Vision of Elegos the Harmless]
[Vision of Carver the Carver]
[Vision of Mosa the Majestic]
[Vision of Wossaul the Giant]
[Vision of Codd the Cheerful]
"""

for line in txt.split('\n'):
    print(line.replace('[','').replace(']',''))