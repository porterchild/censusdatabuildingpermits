data comes from https://www.census.gov/construction/bps/


I structured this flow of data as pipelines.
There will end up being 4 files - 
state units.csv
state valuation.csv
msa units.csv
msa valuation.csv

so there is a downloader and a storer for each. Pipe output from downloader to storer. I could have combined them, but I wanted 
to abstract a bit.

hours - 1, 1.5, 0.5
