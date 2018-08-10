#create symlinks in home directory for all dotfiles in ./dots/
for f in `ls ./dots`
  do
        ln -s ./dots/$f ~/.$f
  done

#set up Zshell
echo
echo 'Setting up Zshell...'
bash ./setup/setup_zsh.sh
echo

#set up Vim
echo
echo 'Setting up Vim...'
bash ./setup/setup_vim.sh
echo

#install important apt packages
echo
echo 'Installing some packages with apt (the rest will need to be manually installed; see ./lists/manual_pkg.txt)...'
for f in `cat ./lists/.apt_pkg.txt`
  do 
        sudo apt install $f
  done

#set up Python
echo 
echo 'Setting up key Python packages...'
bash ./setup/setup_python.sh
echo

#set up R



echo
echo '-------------------------------------'
echo 'All done! Remaining software should be manually installed. Any software that failed to install should be troubleshot manually.'
