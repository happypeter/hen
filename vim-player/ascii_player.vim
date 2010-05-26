function! AsciiPlayer()
    set nowrap
    set scrolloff=0
    set columns=80        
    set lines=26           
    normal gg
    !mplayer bad_apple.mp3  2>/dev/null 1>/dev/null &
    let i = 1
    while i < 3283
        execute "normal 25\<CR>zt"
        redraw
        let i = i + 1
        sleep 67m
    endwhile
endfunction
command! AsciiPlayer call AsciiPlayer()
