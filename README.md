# dots_and_setup


### DEH 08-09-18

__A WORK IN PROGRESS__


My collection of dotfiles, lists of installed software, and setup scripts,
to make it easier for me to migrate and/or recreate my working environment
to/on new machines.


Run main_setup.sh to setup anything that be can done automatically. Then 
remaining software should be installed manually (see ./lists/manual_pkg).
[NOTE: The scripts may break part-way because of unforeseen dependencies, 
but should nonetheless serve as a good record of stuff I need to do.]


### DEH 08-11-18

__TURNED OUT NOT TO BE A WORK IN PROGRESS BECAUSE MY OS UPDATE FAILED AND I HAD TO REINSTALL__

Steps I took:

***NOTE: Best to run*** `sudo apt update` ***between every pair of*** `sudo apt install <pkg>` ***commands.***

1. Reinstall Ubuntu
2. sudo apt install vim git git-core
3. git clone https://github.com/drewhart/dots_and_setup.git ~/.dots_and_setup
4. cd ~
5. for f in `ls ./.dots_and_setup/dots`; do ln -s ./.dots_and_setup/dots/$f ~/.$f; done
6. run the git clone command in setup_vim.sh, to clone the Vundle repo
7. open vim and run :PluginInstall
8. sudo apt install zsh
9. follow instructions on the zshell website to install it
10. move ~/.zshrc.pre-oh-my-zsh back to ~/.zshrc
11. git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git
12. run the install script in gnome-terminal-colors-solarized and follow on-screen instructions
13. git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier
14. set hotkeys for moving between workspaces, moving windows between workspaces, and maximizing/minimizing windows
15. sudo apt install gnome-tweak-tool, then use it to adjust anything I want (e.g. workspace behavior, top bar)
16. OPTIONAL: On Ubuntu 18 the mouse kept lagging and stalling, and I couldn't click and drag (or click and highlight thereby); the following line fixed this:
        sudo apt remove xserver-xorg-input-synaptics
17. Install spotify (see instructions online)

18. Install GDAL and all
    sudo apt install libgdal-dev libgdal20 gdal-bin gdal-data python-gdal python3-gdal
    And also postgis
    sudo apt install postgis
19. Install pip
        sudo apt install python-pip python3-pip
    And then install all my common python packages with pip, and also install basemap:
    sudo apt install python-matplotlib python-mpltoolkits.basemap
20. Install libreoffice
    sudo apt install libreoffice
21. Install R
    sudo apt -y install r-base
    Then download RStudio from their webpage, install gdebi
    sudo apt install gdebi-core
    And then start R and install common packages there
22. Install f.lux, and set it with my coordinates and set it to autostart (Google the website)
