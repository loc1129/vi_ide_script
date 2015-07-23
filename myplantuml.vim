" This file should be add into .vim/plugin after
" http://www.vim.org/scripts/script.php?script_id=3538 been installed
" Please refer to http://www.plantuml.com/running.html
au BufNewFile,BufRead *.uml set filetype=plantuml
let g:plantuml_executable_script='java -jar /home/luocheng/tools/plantuml.jar %'
let s:makecommand=g:plantuml_executable_script
"" define a sensible makeprg for plantuml files
autocmd Filetype plantuml let &l:makeprg=s:makecommand

nnoremap <F5> :w<CR> :silent make\|redraw!\|cc<CR>
inoremap <F5> <Esc>:w<CR>:silent make\|redraw!\|cc<<CR>

"au BufNewFile,BufRead *.uml set filetype=plantuml
"autocmd FileType plantuml
            "\ map <silent> <F6> :!java -jar /home/luocheng/tools/plantuml.jar % && test -n "$DISPLAY" && display %:r.png<cr><space>
