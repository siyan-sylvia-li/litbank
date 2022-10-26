import glob

if __name__ == "__main__":
    fs = glob.glob("original/*.txt")
    scrape_file = open("scraper.sh", "w+")
    TEMPLATE = "wget https://www.gutenberg.org/files/{X}/{X}-0.txt\n"
    for f in fs:
        n = (f.split("_")[0]).replace("original/", "")
        scrape_file.write(TEMPLATE.format(X=n))

