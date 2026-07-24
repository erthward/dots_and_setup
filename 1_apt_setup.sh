# get apt up to date before starting
sudo apt update && sudo apt upgrade

# install git
sudo apt install \
   vim \
   git \
   git-core

# clone this repo
git clone https://github.com/drewhart/dots_and_setup.git ~/.dots_and_setup

# move the default .bashrc file to the Desktop temporarily
mv ~/.bashrc ~/Desktop/bashrc.bkp

#create symlinks in home directory for all the dotfiles
cd ~
for f in `ls ./dots_and_setup/dots`
  do
        ln -s ./dots_and_setup/dots/$f ~/.$f
  done

# if that succeeded then safely delete the old .bashrc whenever desired!

# add ubuntugis repo to apt (for `gdal-bin` installation)
sudo add-apt-repository ppa:ubuntugis/ppa

# do other apt installs
sudo apt install \
   # scripting tools
   python3 \
   # PDF tools
   zathura \
   okular \
   xournalpp \
   qpdf \
   pdftk \
   # copy/paste tool
   xclip \
   # file-renaming tool
   rename \
   # image and video tools
   imagemagick \
   feh \
   mplayer \
   # spatial tools
   gdal-bin \
   # web tools
   brave-browser \
   chromium-browser \
   gnome-tweaks \
   # software install tools
   snapd

# make sure zathura copies to main clipboard
echo "set selection-clipboard clipboard" >> ~/.config/zathura/zathurarc

# run snap installs
sudo snap install --edge ferdium
  # NOTE: be sure to AV to Ferdium so Teams/etc work!
  #       and also be sure to enable audio for teams within Ferdium!
sudo snap connect ferdium:camera
sudo snap connect ferdium:audio-record
sudo snap install \
   firefox \
   spotify

# now log into Spotify play something good!   :)


