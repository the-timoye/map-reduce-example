import os

# clean generated files
if os.path.exists('tupled_songs.txt'):
    os.remove('tupled_songs.txt')

file = open('song_file.txt', 'r', newline='\n')
tupled_songs_file = open('tupled_songs.txt', 'a')

# save tuples in new file
for line in file:
    song = line.rstrip('\n')
    new_line = tuple([song.rstrip('\n' ),1])
    tupled_songs_file.write('{}\n'.format(new_line))

tupled_songs_file.close()
file.close()