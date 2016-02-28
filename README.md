# inkscape laser sequence extension

If you use(d) inkscape to create models for laser cutting, chances are you have ran into the following problem: the laser cutter first cuts the large shape, then it ever so slightly moves, then the holes in that shape are created but with a small offset. Thats why I created this simple extension to deal with this!

The extension exists out of a couple lines of code that will re-arrange the order of the vectors for you, so the small holes get cut first.


## how to use

1. Install the extension
Simply copy the files lasercut_sequence.inx and lasercut_sequence.py into the C:\Program Files\Inkscape\share\extensions folder (or wherever your inkscape installation folder might be.)

2. Apply changes
Before you print your model, run the extension once. (Extensions > laser cutting > Fix print sequence)
![extensions > laser cuttign > fix print sequence](http://i.imgur.com/6ScxnRL.png)

Congratulations! your model will now print in the correct order.
