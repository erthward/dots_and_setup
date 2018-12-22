####STEP 0:
#copy backup files to Desktop (get started now because it'll take a while)
cp -r /run/media/drew/SLAB/<BACKUP_DIRNAME> ~/Desktop

####STEP 1:
#install spotify (for entertainment while working)
sudo pacman -S --needed base-devel git wget yajl
git clone https://aur.archlinux.org/package-query.git
cd package-query/
makepkg -si
cd ..
git clone https://aur.archlinux.org/yaourt.git
cd yaourt/
makepkg -si
cd ..
sudo rm -dR ./yaourt/ ./package-query/
yaourt -S spotify-stable --needed --noconfirm
#get the PGP signature public ID from the ERROR output, use it to run:
gpg --recv-key $KEYID
#then run again
yaourt -S spotify-stable --needed --noconfirm
#now long into spotify and enjoy...


####STEP 2:
#play with settings:
# - tweak mouse sensitivity
# - dump file explorer and settings as taskbar icons
# - download fluxgui, then run it at command line and set zip code
yaourt -S fluxgui
# - set desktop image
# - get rid of Home and other default directories on Desktop
# - configure workspaces
# - set hotkeys for switching between workspaces and movin windows between them to Vim-type (h,j,k,l)
#set hotkeys for maximizing/minimizing windows
yaourt -S gnome-tweaks #BUT THIS DOESN'T SEEM TO WORK AFTER INSTALL
#get rid of the stupid terminal drop-down behavior by going to Settings->Keyboard->Keyboard Shortcuts tab, then changing the -terminal--drop-down option to get rid of the "--drop-down" bit


####STEP 3:
#get my dotfile-repo, and follow instructions in its README (ignoring/changing instructions specific to Ubuntu)
yaourt -S vim
git clone https://github.com/drewhart/dots_and_setup.git ~/.dots_and_setup
nano ./.dots_and_setup/README.md
for f in `ls ./.dots_and_setup/dots`; do ln -s ./.dots_and_setup/dots/$f ~/.$f; done
#copy bashrc separately, because it failed to copy after conflicting with existing .bashrc
cp ./.dots_and_setup/dots/bashrc ./.old_bashrc
#get Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
#launch git then run :PluginInstall<Enter>
#install Zshell
yaourt -S zsh
#follow the oh-my-zsh website directions to install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
#replace the new zshrc from the one that I cloned from my dots_and_setup repo
mv ~/.zshrc.pre_oh_my_zsh ~/.zshrc
#get solarized colors
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git
#run the install script in gnome-terminal-colors-solarized and follow on-screen instructions
#get tmux and tmuxifier
yaourt -S tmux
git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier
#get gnome-terminal and set it as default
yaourt -S gnome-terminal


####STEP 4:
#go into power settings and fix battery settings to improve life and disable hibernate (which ruined my first install of Manjaro!)



####STEP 5:
#install geospatial stuff
yaourt -S gdal
yaourt -S postgis
yaourt -S qgis


####STEP 6:
#install python stuff
yaourt -S python-pip
pip install matplotlib
#etc...


####STEP 7:
#install R stuff
yaourt -S tk  #tkinter, needed for R's chooseCRANmirror() popup
yaourt -S r
#fix the R personal library path, so that zsh doesn't accidentally cd into 'R' when I run 'R' in ~
#in /usr/lib/R/etc/Renviron, change:
#R_LIBS_USER=${R_LIBS_USER-'~/R/<...>'
#to
#R_LIBS_USER=${R_LIBS_USER-'~/R_lib/<...>'
yaourt -S rstudio-desktop-bin
#then run R and install.packages('raster'), etc...


####ADDITIONAL:
#I had a HUGE PROBLEM where twice I installed and twice I got arrested by numerous errors at boot,
#ultimately dumping me into a non-functional emergency shell where I couldn't even type.
#The steps at this site saved my ass: https://forum.manjaro.org/t/howto-restore-an-unbootable-system-after-an-interrupted-kernel-update/33085
