# inkscape laser sequence extension

If you use(d) inkscape to create models for laser cutting, chances are you have ran into the following problem: the laser cutter first cuts the large shape, then it ever so slightly moves, then the holes in that shape are created but with a small offset. Thats why I created this simple extension to deal with this!

The extension exists out of a couple lines of code that will re-arrange the order of the vectors for you, so the small holes get cut first.


## how to use

1. Install the extension
First, download the required files. this can be done by clicking "download zip" in the top right corner.
![download zip](http://i.imgur.com/gFwuinb.png)
Extract the zip into the inkscape extensions folder (See `Edit > Preferences > System > Inkscape-Extensions`) such that `lasercut_sequence.py` and `lasercut_sequence.inx` are directly in this directory.

2. Apply changes
Before you print your model, run the extension once. (Extensions > laser cutting > Fix print sequence)
![extensions > laser cuttign > fix print sequence](http://i.imgur.com/6ScxnRL.png)

Congratulations! your model will now print in the correct order.
