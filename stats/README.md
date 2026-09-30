# Blog visitor counter

No third parties, no cookies, no stored IP addresses.

- `px.rb` runs as CGI on isene.com. Each blog page loads it as a tiny
  image, and it writes one line per view to `~/blogstats/hits.tsv`.
- The visitor column is a hash of IP address and browser, with a secret
  salt and the date. It counts people per day and changes every day.
- `report.rb [days]` prints views per day, top pages and where visitors
  came from.

Server setup: the repo is cloned to `~/isene.github.io` with only this
folder checked out, and `cgi-bin/px.rb` on isene.com links here.
Deploy with `git pull` there.
