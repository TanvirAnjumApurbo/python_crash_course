def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\nPlease tell me about an album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
