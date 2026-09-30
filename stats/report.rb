#!/usr/bin/env ruby
# Blog visitor report from hits.tsv, written by px.rb.
#   report.rb [days]    default 30
require "uri"

DIR = ENV["BLOGSTATS_DIR"] || "/home/geir/blogstats"
days = (ARGV[0] || 30).to_i.clamp(1, 3650)
since = (Time.now.utc - days * 86_400).strftime("%F")
file = File.join(DIR, "hits.tsv")
rows = File.exist?(file) ? File.foreach(file).map { |l| l.chomp.split("\t", 4) } : []
rows.select! { |t, *| t.to_s[0, 10] >= since }
abort "No visits in the last #{days} days." if rows.empty?

per_day = Hash.new { |h, k| h[k] = [0, {}] }
rows.each { |t, _, _, v| d = per_day[t[0, 10]]; d[0] += 1; d[1][v] = true }
visitors = per_day.values.sum { |_, v| v.size }

def top(list, n)
  list.tally.sort_by { |k, c| [-c, k] }.first(n)
end

def bar(n, max, width = 30)
  "#" * (max.zero? ? 0 : (n * width.to_f / max).ceil)
end

puts "Last #{days} days: #{rows.size} views by #{visitors} visitors (counted per day)"
puts
puts "Per day (last 14 days)          views  visitors"
recent = per_day.keys.sort.last(14)
max = recent.map { |d| per_day[d][0] }.max
recent.each do |d|
  v, who = per_day[d]
  printf "%s %-18s %6d  %8d\n", d, bar(v, max, 18), v, who.size
end

puts
puts "Top pages"
top(rows.map { |r| r[1] }, 15).each { |p, c| printf "%6d  %s\n", c, p }

puts
puts "Came from"
hosts = rows.map do |r|
  host = (URI.parse(r[2]).host rescue nil).to_s.sub(/\Awww\./, "")
  host.empty? ? "(direct)" : host
end.reject { |h| h == "isene.org" }
top(hosts, 10).each { |h, c| printf "%6d  %s\n", c, h }
