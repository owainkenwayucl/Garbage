# Generic makefile for using Lilypond to build PDFs/PNGs (and accidentally also
# MIDI files from ABC format files.

# Owain Kenway

%.png: %.ly Makefile
	lilypond --png $<

%.pdf: %.ly Makefile
	lilypond --pdf $<


%.ly : %.abc Makefile
	abc2ly -b $<

clean:
	rm -f *.png *.ly *.midi *.pdf

.PHONY: clean
