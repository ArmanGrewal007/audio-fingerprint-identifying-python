import sys

class Database(object):
  TABLE_SONGS = None
  TABLE_FINGERPRINTS = None

  def __init__(self, a):
    self.a = a

  def connect(self):
    raise NotImplementedError("connect must be implemented by a Database subclass")

  def insert(self, table, params):
    raise NotImplementedError("insert must be implemented by a Database subclass")

  def findOne(self, table, where):
    """Return a single matching row or None; subclasses should override with DB-specific logic."""
    raise NotImplementedError("findOne must be implemented by a Database subclass")

  def insertMany(self, table, columns, values):
    """Insert multiple rows; subclasses should implement efficient bulk insert."""
    raise NotImplementedError("insertMany must be implemented by a Database subclass")

  def get_song_by_filehash(self, filehash):
    return self.findOne(self.TABLE_SONGS, {
      "filehash": filehash
    })

  def get_song_by_id(self, id):
    return self.findOne(self.TABLE_SONGS, {
      "id": id
    })

  def add_song(self, filename, filehash):
    song = self.get_song_by_filehash(filehash)

    if not song:
      song_id = self.insert(self.TABLE_SONGS, {
        "name": filename,
        "filehash": filehash
      })
    else:
      song_id = song[0]

    return song_id

  def get_song_hashes_count(self, song_id):
    raise NotImplementedError("get_song_hashes_count must be implemented by a Database subclass")

  def store_fingerprints(self, values):
    self.insertMany(self.TABLE_FINGERPRINTS,
      ['song_fk', 'hash', 'offset'], values
    )
