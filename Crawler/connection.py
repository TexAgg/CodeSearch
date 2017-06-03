import MySQLdb

# http://bit.ly/2qAeub7
class Connection():
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","5625","CodeSearch")

	def add_record(self, record):
		cursor = self.db.cursor()
		stmt = "INSERT INTO codes(url, content, payload_digest) VALUES ('%s', '%s', '%s')" % (record['url'], record['content'], record['payload_digest'])
		try:
			cursor.execute(stmt)
   			self.db.commit()
		except:
			print "BAD STUFF!!!"
			self.db.rollback()
		
		# https://stackoverflow.com/a/865272/5415895
		def __enter__(self):
			return self
		
		def __exit__(self, exc_type, exc_value, traceback):
			self.db.close()