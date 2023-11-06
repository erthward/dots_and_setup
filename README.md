# dots_and_setup

My collection of dotfiles and scripts for software installation and configuration,
to make it easier for me to migrate my working environment to new machines.

Scripts are numerically named in the order in which they're intended to be used,
and could either be executed wholesale or run interactively.
(...Actually, probably the latter. The scripts may break part-way because
of unforeseen dependency issues,
but should nonetheless serve as a good record of the steps to take.)


### Steps:

***NOTE: Best to run*** `sudo apt update` ***between every pair of*** `sudo apt install <pkg>` ***commands.***

0. Install Ubuntu (or other OS)
1. Run the `1_apt_setup.sh` script to install git, clone this repo to the correct location, softlink dotfiles, and run other necessary apt installs.
2.8. sudo apt install zsh
2.9. follow instructions on the oh-my-zsh website to install it
2.10. move ~/.zshrc.pre-oh-my-zsh back to ~/.zshrc
2.11. git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git
2.12. run the install script in gnome-terminal-colors-solarized and follow on-screen instructions
2.13. git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier
2.14. set hotkeys for moving between workspaces, moving windows between workspaces, and maximizing/minimizing windows
3. Run the commands in `3_vim_setup.sh` to install Vundle and then use it to install other
4. Execute `4_python_and_R_setup.sh` to use conda to create my general-purpose scientific computing environment and install my py and R packages into it. (NOTE: this can easily be used separately or reused later for standalone Python environment configuration.)
5. Execute `5_julia_setup.sh` to install Julia with my preferred packages (NOTE: this can easily be used separately or reused later for standalone Julia installation.)

# TODO: CLEAN UP REMAINDER BELOW HERE
14. download snap deb file from Snap's website, then run `sudo snap install ferdi` and `sudo snap install spotify` :)
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
