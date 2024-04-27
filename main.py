#!/usr/bin/env python3
# from argparse import ArgumentParser
import json, os, shutil

def main():
	html = '<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'

	with open("links.json") as rf:
		links = json.load(rf)

	shutil.rmtree("dist", ignore_errors=True)
	os.mkdir("dist")

	for link in links:
		html_document = html.format(url=link["url"])
		file_path = f'dist/{link["name"]}.html'

		with open(file_path, "w") as wf:
			wf.write(html_document)

if __name__ == "__main__":
	main()
