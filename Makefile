
.PHONY: all customprimitives bulkblendfromshape removedoublesfromall

all: bulkblendfromshape customprimitives removedoublesfromall

customprimitives:
	zip customprimitives.zip customprimitives/*
bulkblendfromshape:
	zip bulkblendfromshape.zip bulkblendfromshape/*
removedoublesfromall:
	zip removedoublesfromall.zip removedoublesfromall/*

clean:
	rm *.zip

