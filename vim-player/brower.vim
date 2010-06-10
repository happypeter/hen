function! Browser ()
  let line = getline (".")
"  let line = matchstr (line, "\%(http://\|www\.\)[^ ,;\t]*")
  exec "!firefox ".line
endfunction
map <Leader>w :call Browser ()<CR>

" <Leader> defaults to `\`
" NOW Browser() only works for lines containing nothing but the link
" refer to http://vim.wikia.com/wiki/VimTip306 
