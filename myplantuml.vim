" This file should be add into .vim/plugin after
" http://www.vim.org/scripts/script.php?script_id=3538 been installed
" Please refer to http://www.plantuml.com/running.html
let g:plantuml_executable_script="java -jar /Users/loc/Downloads/plantuml.jar -overwrite"
nnoremap <F4> :w<CR> :silent make<CR>
inoremap <F4> <Esc>:w<CR>:silent make<CR>
