import zlib
text = b"string compress" * 100
compressed = zlib.compress(text)
 
print("size of original: " + str(len(text)))
print("size of compressed: " + str(len(compressed)))
 
decompressed = zlib.decompress(compressed)
print("size of decompressed: " + str(len(decompressed)))
