# NYT-headlines

A simple python crawler that parses the New York Times homepage and writes the day's headlines to a file named `timesheadlines.txt`  

The script works by retrieving all `h3` from the page and writing them to a file, so
it should work with any other publications with minimal adjustments.  

The only required package is `beautifulsoup4`
