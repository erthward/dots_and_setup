# install git
sudo apt install \
   vim \
   git \
   git-core

# clone this repo
git clone https://github.com/drewhart/dots_and_setup.git ~/.dots_and_setup

#create symlinks in home directory for all the dotfiles
cd ~
for f in `ls ./dots_and_setup/dots`
  do
        ln -s ./dots_and_setup/dots/$f ~/.$f
  done

# do other apt installs
sudo apt install \
   mplayer \
   feh \
   zathura \
   imagemagick \
   qpdf \
   firefox \
   brave-browser \
   chromium

# TODO: ADD PY HERE??


# TODO: CLEAN UP FROM HERE DOWN VVV

#set up Zshell
echo
echo 'Setting up Zshell...'
bash ./setup/setup_zsh.sh
echo

