from bs4 import BeautifulSoup
import warc
import csv
import re
from connection import Connection

# I don't need Hadoop for this lol.
def scrape(fname):
	# http://bit.ly/2pOfwkm
	csvfile = open('out/data.csv', 'w')
	fieldnames = ['url', 'content', 'payload_digest']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	conn = Connection()

	# http://bit.ly/2pPIKOT
	f = warc.open(fname)
	for record in f:
		process(record, writer, conn)
	csvfile.close()

def process(record, writer, conn):
	if record['Content-Type'] == 'application/http; msgtype=response':
		payload = record.payload.read()
		headers, body = payload.split('\r\n\r\n', 1)

		if 'Content-Type: text/html' in headers:
			codes = get_code(body)
			for c in codes:
				print "HTML: " + record['WARC-Target-URI']
				rec = {
					"url": record['WARC-Target-URI'], 
					'content': c.encode('utf-8'),
					"payload_digest": record['WARC-Payload-Digest']
				}
				writer.writerow(rec)
				conn.add_record(rec)
		elif "Content-Type: text/plain":
			print "PLAINTEXT: " + record['WARC-Target-URI']
			#print body
			writer.writerow({
				"url": record['WARC-Target-URI'], 
				'content': body.decode('ascii', 'replace').encode('utf-8', 'replace'),
				"payload_digest": record['WARC-Payload-Digest']
			})

def get_code(data, ctr=None):
	if ctr is None:
		ctr = []
	# http://bit.ly/2qhuYIp
	soup = BeautifulSoup(data, 'html.parser')
	for code in soup.find_all('pre'):
		ctr.append(code.get_text())
	for code in soup.find_all('code'):
		ctr.append(code.get_text())
	for code in soup.find_all('textarea'):
		ctr.append(code.get_text())
	return ctr

if __name__ == "__main__":
	fname = "crawl-data/CC-MAIN-2014-35/segments/1408500800168.29/warc/CC-MAIN-20140820021320-00000-ip-10-180-136-8.ec2.internal.warc.gz"
	scrape(fname)
