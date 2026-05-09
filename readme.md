# wgdl

Download images from a thread on 4chan.org/wg.

## Installation

You can build the binary file with a simple `make`. Then you can copy the
binary to a directory in your `PATH`. For example:

```
make
cp wgdl ~/.local/bin/
```

## Usage

At the moment the only functionality is downloading all images in a thread:

```
wgdl wg/1234567
```

## Roadmap

- [ ] add a TUI for selecting a thread interactively in the terminal
- [ ] query threads for a word instead of passing the id of the thread
- [ ] select the output directory
- [X] extend this to other threads and media
