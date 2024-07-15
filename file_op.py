with open('nature.jpg', 'rb') as rf:
    with open('nature_remake.jpg', 'wb') as wf:
        chunk_size = 1024
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
