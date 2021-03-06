"""Find the titles of the top visited Vroots.

This program will take a CSV data file and output lines of

    Vroot Title

To run:

    python top_titles.py anonymous-msweb.data
"""

from count_titles import CountTitles
import csv

# run in local mode with the input being MS browsing data
mr_job = CountTitles(args=['--runner', 'local', 'msanon/anonymous-msweb.data.gz'])
with mr_job.make_runner() as runner:
    runner.run()
    title_counts = [mr_job.parse_output_line(line) for line in
            runner.stream_output()]
    results = sorted(title_counts, key=lambda (k,v): v, reverse=True)
    print results[:10]
