import os
from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__, static_url_path = '', static_folder='static')

@app.route('/')
def root():
	return render_template('home.html')

@app.route('/publications')
def publications():
	req = urllib2.urlopen("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=strauss-albee%20d&retmode=json")
	reqjson = json.load(req)
	pubs = reqjson["esearchresult"]["idlist"]
	urlstring = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pubs)
	req2 = urllib2.urlopen(urlstring)
	req2json = json.load(req2)
	print urlstring
	# print json.dumps(req2json, indent=4)
	papers = []
	for key, value in req2json["result"].items(): #save all paper info to a list, then sort reverse chronologically
		if key != "uids":
			papers.append(value)
	papers.sort(key=lambda x: x["sortpubdate"],reverse=True)
	return render_template('publications.html', papers = papers)

@app.route('/projects')
def projects():
	return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)
