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

```
wgdl [-h] [-t THREAD] [-d DIR] [-l] board
```

### Get a list of threads on a board

List all the threads in Wallpapers General

```
wgdl -l wg
```

### Download images from a thread

```
wgdl wg -t 1234567
```

You can specify the output directory with `-d`, otherwise the thread title
would be used.

```
wgdl -d walls wg -t 1234567
```

## Roadmap

- [ ] add a TUI for selecting a thread interactively in the terminal
- [ ] query threads for a word instead of passing the id of the thread
- [X] select the output directory
- [X] extend this to other threads and media
