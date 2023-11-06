#install Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

#NOTE: make sure that script number 1 already established  ~/.vimrc
# as a softlink to ./dots_and_setup/dots/vimrc file

#then start vim and run :PluginInstall to get things up to speed
vim -c ":PluginInstall" -c ":q" -c ":q" 

#NOTE: if YouCompleteMe installed, then will then need to cd to YouCompleteMe's
# directory and run install.py with the appropriate flags in order for it to work
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer --java-completer
        #NOTE: will need the appropriate libs installed for --clang-completer to work
        #NOTE: will need jdk installed for --java-completer to work
cd -


