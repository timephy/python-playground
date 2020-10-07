# read_stream_nonblocking

Creates a different thread on which the stream-reading blocks, when values are
received it adds them to a Queue (FIFO) which can be read synchronously and
non-blocking.
