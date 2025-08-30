from libs.reader_file import FileReader

song = None
seconds = 5

r = FileReader(123)
r.recognize(seconds=seconds)

print(song)
