#!/bin/bash

# Script to modify .vimrc for snippets and shortcuts





##############
#  SNIPPETS  #
##############

# Can have a directory with snippets of code inside files
# ~/.snippets/if
# cat if
## if (( $COUNT < 10 )) for numerical tests
## if [[ $USER = "root" ]] for string tests
# if [[ ]]
#  then
#		echo "true"
#  else
#		echo "false"
# if

# In normal mode
# use ':r "path to snippet"
# :r = read in
# :r!=reads in command like date EX:
#			:r!date "+\%x"

###############
#  SHORTCUTS  #
###############

# Enables line numbers with 'Ctrl + N' in normal mode
echo "nmap <C-n> :set invnumber<CR>" >> ~/.vimrc
echo "map <F2> i#!/bin/bash" >> ~/.vimrc 
echo "map <F3> i#!/usr/bin/python3" >> ~/.vimrc
echo "map <F4> o#This file was created on <ESC>:r!date '+\%d \%b \%y'<ESC>kJ" >> ~/.vimrc

echo "\" target sections" >> ~/.vimrc
echo "nmap <F6> i/*{{{/*<CR><CR><CR>/*}}}/*" >> ~/.vimrc
echo "imap <F6> /*{{{/*<CR><CR><CR>/*}}}/*" >> ~/.vimrc

echo "\" folding" >> ~/.vimrc
echo "set foldmethod=marker" >> ~/.vimrc
echo "inoremap <F9> <ESC> za" >> ~/.vimrc
echo "nnoremap <F9> za" >> ~/.vimrc
echo "vnoremap <F9> za" >> ~/.vimrc

echo "\" Open all folds" >> ~/.vimrc
echo "inoremap <F7> <ESC> zR" >> ~/.vimrc
echo "nnoremap <F7> zR" >> ~/.vimrc
echo "vnoremap <F7> zR" >> ~/.vimrc

echo "\" Close all folds" >> ~/.vimrc
echo "inoremap <F8> <ESC> zm" >> ~/.vimrc
echo "nnoremap <F8> zm" >> ~/.vimrc
echo "vnoremap <F8> zm" >> ~/.vimrc

echo "hi ipaddr ctermfg=white ctermbg=darkred cterm=bold" >> ~/.vimrc


echo "hi localhost ctermfg=white ctermbg=darkred cterm=bold" >> ~/.vimrc

echo "autocmd BufReadPost,BufNewFile * call matchadd('localhost', '\v(127\.0\.0\.1|::1)')" >> ~/.vimrc


echo "hi comments ctermfg=green ctermbg=black cterm=bold" >> ~/.vimrc

echo "autocmd BufReadPost,BufNewFile * call matchadd('comments', '\v^#')" >> ~/.vimrc


echo "[+] Added key shortcuts to vim config file"
echo "[+] Complete!"

