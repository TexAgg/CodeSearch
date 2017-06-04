import MySQLdb

# http://bit.ly/2qAeub7
class Connection():
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","apple","CodeSearch")

	def add_record(self, record):
		cursor = self.db.cursor()
		stmt = "INSERT INTO codes(url, content, payload_digest) VALUES ('%s', '%s', '%s')" % (record['url'], record['content'], record['payload_digest'])
		try:
			cursor.execute(stmt)
   			self.db.commit()
		# https://stackoverflow.com/a/1715206/5415895
		except Exception, e:
			print "BAD STUFF: %s" % e
			#print stmt
			self.db.rollback()
		
		# https://stackoverflow.com/a/865272/5415895
		def __enter__(self):
			return self
		
		def __exit__(self, exc_type, exc_value, traceback):
			self.db.close()