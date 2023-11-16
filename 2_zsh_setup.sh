# install zsh
sudo apt update && sudo apt upgrade
sudo apt install zsh

# make zsh the default shell
chsh -s $(which zsh)
# NOTE: if you don't have root access, so the above doesn't work, then standard practice
# appears to be to create ~/.bash_profile with the following lines in it:
#      export SHELL=/bin/zsh
#      exec /bin/zsh -1
# and you may need to restart after that for change to take effect
# A simpler alternative is Gnome Termainal Preferences -> check "Run a custom command
# instead of my shell", then put /bin/zsh in the provded field.

# install ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# move my personalized .zshrc, which ohmyzsh backed up as .zshrc.pre-oh-my-zsh,
# back to my main .zshrc
# NOTE: backup the default .zshrc if desired, but a new call to the curl command
# that set up ohmyzsh should be sufficient to recover it if needed
mv .zshrc.pre-oh-my-zsh .zshrc

# get solarized zshell colors set up (follow CLI instructions)
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git
cd ./gnome-terminal-colors-solarized/
bash ./install.sh

# enable zsh-syntax-highlighting and zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# get tmuxifier and Tmux Plugin Manager (tpm)
git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier 
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# NOTE: then start tmux and run `tmux source ~/.tmux.conf` to install plugins

# install pywal
pip3 install pywal

# lastly, if I've made any custom color themes that aren't already in ~/.oh-my-zsh/themes,
# then copy them there!
