import MySQLdb
import dateutil.parser

# http://bit.ly/2qAeub7
class Connection():
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","apple","CodeSearch")

	def add_record(self, record):
		cursor = self.db.cursor()
		stmt = "INSERT INTO codes(url, content, payload_digest, crawl_date) VALUES ('%s', '%s', '%s', '%s')" % (record['url'], record['content'], record['payload_digest'], getMySqlDateTime(record['warc-date']))
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

# https://stackoverflow.com/a/15228038/5415895
def getMySqlDateTime(s):
	res = str(dateutil.parser.parse(s))[:-6]
	return res