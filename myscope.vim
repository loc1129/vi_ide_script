if has("cscope") && executable("cscope")
   if has('quickfix')
      set cscopequickfix=s-,c-,d-,i-,t-,e-,g-
   endif
   set csprg=/usr/local/bin/cscope
   set csto=0
   set cst

   function! GenerateCtagsAndCscope()
      !ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .
      !cscope -Rbq
   endfunction
   map <C-F12> :call GenerateCtagsAndCscope()<CR>

   nmap <C-\>s :scs find s <C-R>=expand("<cword>")<CR><CR>
   nmap <C-\>g :scs find g <C-R>=expand("<cword>")<CR><CR>
   nmap <C-\>c :scs find c <C-R>=expand("<cword>")<CR><CR>
   nmap <C-\>t :scs find t <C-R>=expand("<cword>")<CR><CR>
   nmap <C-\>e :scs find e <C-R>=expand("<cword>")<CR><CR>
   nmap <C-\>f :scs find f <C-R>=expand("<cfile>")<CR><CR>
   nmap <C-\>i :scs find i <C-R>=expand("<cfile>")<CR><CR>
   nmap <C-\>d :scs find d <C-R>=expand("<cword>")<CR><CR>

   if !has('python')
      echo "my script for cscope require vim compiled with python"
      finish
   else
      python << EOF
import vim
import os, os.path
from itertools import takewhile
def iterate(fun, x):
   yield x
   for element in iterate(fun, fun(x)):
      yield element
for path in takewhile(lambda x: x!='/', iterate(os.path.dirname, os.getcwd())):
   cscopefile = os.path.join(path, 'cscope.out')
   if os.access(cscopefile, os.R_OK):
      vim.command('cscope add ' + cscopefile + ' ' + path)
      break
EOF
   endif
   if $CSCOPE_DB != ""
   cs add $CSCOPE_DB
   endif
endif
