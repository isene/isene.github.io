#!/usr/bin/env ruby
# Blog visitor counter, run as CGI on isene.com.
# Each blog page loads /cgi-bin/px.rb?p=<path>&r=<referrer> as an image.
# One line per view in hits.tsv: time, path, referrer, visitor.
# No cookies and no IP address stored. The visitor is a hash of IP and
# browser with a secret salt and the date, so it changes every day.
require "base64"
require "cgi"
require "digest"
require "time"

DIR = ENV["BLOGSTATS_DIR"] || "/home/geir/blogstats"
GIF = Base64.decode64("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7")
BOTS = /bot|crawl|spider|slurp|preview|monitor|curl|wget|python|headless/i

def clean(value)
  value.to_s.dup.force_encoding("UTF-8").scrub.gsub(/[\t\r\n]/, " ")[0, 300]
end

begin
  q = CGI.parse(ENV["QUERY_STRING"].to_s)
  path = clean(q["p"].first)
  agent = ENV["HTTP_USER_AGENT"].to_s
  if path.start_with?("/") && agent !~ BOTS
    now = Time.now.utc
    salt = File.read(File.join(DIR, "salt")).strip
    visitor = Digest::SHA256.hexdigest([salt, now.strftime("%F"), ENV["REMOTE_ADDR"], agent].join("|"))[0, 12]
    line = [now.iso8601, path, clean(q["r"].first), visitor].join("\t") + "\n"
    File.open(File.join(DIR, "hits.tsv"), "a", 0o640) { |f| f.write(line) }
  end
rescue StandardError
  # A counter must never break the page it sits on.
end

$stdout.binmode
print "Content-Type: image/gif\r\nCache-Control: no-store\r\n" \
      "Content-Length: #{GIF.bytesize}\r\n\r\n", GIF
