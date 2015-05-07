#!/usr/bin/env ruby
str = ''
File.open("weixin.md", 'r') do |f|
  str = f.read
end


num = str.scan(/\d{8}/).count

count_string = "<div class='count'>" + num.to_s + "</div>" + "\n\n\n"

front = <<HEREDOC
hello peter
HEREDOC


# 每一个 div 以 时间戳为开始符，以空行为结束符，所以注意一个微信内部千万不要有空行

str = str.gsub(/\d{8}/, "<div class='card' id='#{$&}'>")
          .gsub(/^\s*$/, "</div>\n")   # 可以包含0或多个空格的空行

File.open("index.md", 'w') do |f|
  f.write(front)
end



File.open("index.md", 'a') do |f|
  f.write(count_string)
end


File.open("index.md", 'a') do |f|
  f.write(str + "</div>")   # 最后要封口
end


# system 'ssh peter@happyec.org "source .profile &&/home/peter/bin/card_deploy.sh"'
