#!/bin/bash
dir="./"
if [ $# -gt 0 ]; then
dir=$1
fi

cd $dir

if [ -e tags ]; then
echo "remove tags"
rm tags
fi

if [ -e cscope.in.out ]; then
echo "remove cscope.in.out"
rm cscope.in.out
fi

if [ -e cscope.out ]; then
echo "remove cscope.out"
rm cscope.out
fi

if [ -e cscope.po.out ]; then
echo "remove cscope.po.out"
rm cscope.po.out
fi

echo "generate ctags for $dir"
ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .
echo "generate cscope for $dir"
cscope -Rbq 
