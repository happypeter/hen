#!/usr/bin/env ruby

# 为了保证导出正确， weixin.md 中千万不要随拍加空行
# 只有两篇日记之间加”一个“空行，其他地方都不要有任何的空行
str = ''
File.open("weixin.md", 'r') do |f|
  str = f.read
end


num = str.scan(/\d{8}/).count

count_string = "<div class='count'>" + num.to_s + "</div>" + "\n\n\n"

header = <<HEREDOC
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>weixin</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
HEREDOC

footer = <<HEREDOC

</body>
</html>
HEREDOC

# 每一个 div 以 时间戳为开始符，以空行为结束符，所以注意一个微信内部千万不要有空行

str = str.gsub(/(\d\d\d\d\d\d\d\d)/, "<div class='card' id='\\1'>\n<img class='pic-of-day' src='pic-of-day/\\1.jpg'></img>\n<div class='text'>")
          .gsub(/^\s*$/, "</div>\n</div>\n")   # 可以包含0或多个空格的空行

File.open("index.html", 'w') do |f|
  f.write(header)
end

File.open("index.html", 'a') do |f|
  f.write(count_string)
end

File.open("index.html", 'a') do |f|
  f.write(str + "</div></div>")   # 最后要封口
end

File.open("index.html", 'a') do |f|
  f.write(footer)   # 最后要封口
end
system 'scp index.html peter@haoduoshipin.com:toy/weixin/'
