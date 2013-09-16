set nu
set ts=8
set shiftwidth=8
set noexpandtab
set et
syntax on
set showcmd
set autoindent
set hlsearch
colorscheme desert

let Grep_Xargs_Options = '-0'

set nocp
filetype plugin on

"map alt+c and alt+v in mac
"To Mac users out there: for mapping ALT+hjkl, use instead the real character
"generated (find out which character using the combination while in INSERT
"mode)
vmap ç y:call system("pbcopy", getreg("\""))<CR>
nmap √ :call setreg("\"",system("pbpaste"))<CR>p

" 状态栏
set laststatus=2      " 总是显示状态栏
highlight StatusLine cterm=bold ctermfg=yellow ctermbg=blue
        " 获取当前路径，将$HOME转化为~
function! CurDir()
        let curdir = substitute(getcwd(), $HOME, "~","g")
        return curdir
endfunction
set statusline=[%n]\ %f%m%r%h\\|\\pwd:\ %{CurDir()}\\\|%=\|\ %l,%c\ %p%%\\|\ascii=%b,hex=%b%{((&fenc==\"\")?\"\":\"\\|\\".&fenc)}\\|\ %{$USER}\ @\ %{hostname()}\
