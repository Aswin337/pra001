songs=["ra ra rakamma","Naa ready","oo antava","jingucha"]
def art_find(i):
    song_artist=["ra ra rakamma-aswin","naa ready-lognath","oo antava-anachi","jingucha-praveen"]
    for song in song_artist:
        if i.lower() in song:
            return song
res=art_find("OO ANTAVA")
print(res)