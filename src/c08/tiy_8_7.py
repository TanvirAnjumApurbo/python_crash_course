def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


album = make_album('tailer swift', 'red')
print(album)

album = make_album('arinna grande', 'sweetener')
print(album)

album = make_album('badshah', 'kala chashma')
print(album)

album = make_album('maroon 5', 'sugar', tracks=10)
print(album)
