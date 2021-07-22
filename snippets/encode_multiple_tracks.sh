#!/bin/bash

# Process wav recordings of the format
# disc.track artist - song.wav

cover=${album_cover:-cover.jpg}
album=${album_name:-ALBUM}
genre=${genre:-NONE}

files=*.wav

for a in $files
do
  
  noext="${a%.*}"
  song=${noext#*" - "}
  remainder=${noext%$song}
  artist=${remainder#*" "}
  dt=${remainder%$artist}
  artist=${artist%???}
  disc=${dt%.*}
  track=${dt#*$disc} 
  track=${track#*"."}
  echo "Name: $noext"
  echo "Song: $song"
  echo "Artist: $artist"
  echo "Disc: $disc"
  echo "Track: $track"
  echo "Album: $album"
  echo "Cover: $cover"
  echo "Genre: $genre" 

  lame -b 320 -B 320 -q 0 --tt "$song" --ta "$artist" --tl "$album" --tg "$genre" "$a"
  eyeD3 --to-v2.3 --add-image "$cover:FRONT_COVER" -d $disc -n $track "${noext}.mp3"

done
