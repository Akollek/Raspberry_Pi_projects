
#!/bin/bash

# Find the mix ID
MIX=$1
curl "http://8tracks.com/$MIX.json?api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" > mix.json 
python mix_parser.py mix
MIXID=`cat mix`
LENGTH=`cat tracks`
rm tracks
rm mix
rm mix.json

#Create a play token
curl "http://8tracks.com/sets/new.json?api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" > token.json 
python token_parser.py
TOKEN=`cat token`
rm token
rm token.json

# Get the first song
curl "http://8tracks.com/sets/$TOKEN/play.json?mix_id=$MIXID&api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" > song.json 
python song_parser.py
URL=`cat song`
TITLE=`cat title`
DURATION=$((`cat duration`))
TRACK=`cat track`
rm song.json
rm title
rm song
rm duration
rm track
echo
echo "================================================================================="
echo "     $TITLE is playing."
echo "---------------------------------------------------------------------------------"
echo
mplayer $URL
echo
echo "================================================================================="
echo

# Report that the song was played
curl "http://8tracks.com/sets/874076615/report.xml?track_id=$TRACK&mix_id=$MIXID&api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" &

for (( c=2; c<=$LENGTH; c++ ))
do
curl "http://8tracks.com/sets/$TOKEN/next.json?mix_id=$MIXID&api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" > song.json 
python song_parser.py
URL=`cat song`
TITLE=`cat title`
rm song.json
rm title
rm song
rm duration

echo
echo "================================================================================="
echo "     $TITLE is playing."
echo "---------------------------------------------------------------------------------"
echo
mplayer $URL
echo
echo "================================================================================="
echo

# Report that the song was played
curl "http://8tracks.com/sets/874076615/report.xml?track_id=$TRACK&mix_id=$MIXID&api_key=2256b5ab4f6f92d858c9530bd68900e0d0ff42f6" &
done

