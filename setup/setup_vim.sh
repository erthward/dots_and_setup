#install Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

#create a .vimrc softlink in the home directory that points to this repo's ./dots/vimrc file
ln -s ~/.vimrc ./dots/vimrc

#then start vim and run :PluginInstall to get things up to speed
vim -c ":PluginInstall" -c ":q" -c ":q" 

#will need to cd to YouCompleteMe's directory and run install.py with the appropriate flags
#in order for it to work
cd ./.vim/bundle/YouCompleteMe
./install.py --clang-completer --java-completer
        #NOTE: will need the appropriate libs installed for --clang-completer to work
        #NOTE: will need jdk installed for --java-completer to work
cd -


