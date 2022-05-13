def my_favorite_songs():
    """my favorite songs"""
    song_1 = "Ace of Spades"
    song_2 = "Dirty"
    song_3 = "Blue Train"

    return song_1, song_2, song_3

# head, *tail = my_favorite_songs()
favorite_song, *rest = my_favorite_songs()

print("My favorite song is", favorite_song)
print("The rest of the songs are", rest)

def print_songs(songs):
    """Recursive walking"""
    if songs != []:
        head, *tail = songs
        print(head)
        print_songs(tail)

print_songs(my_favorite_songs())

# mintaillesztés

def list_generator(x_val = 10, y_val = 10):
    """List generator for x * y"""
    return [x * y for x in list(range(1, x_val+1)) for y in list(range(1, y_val+1))]

generated_list = list_generator()

first, second, *_, last = generated_list

print(first)
print(second)
print(last)
