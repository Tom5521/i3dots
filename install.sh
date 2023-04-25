#!/bin/bash

mkdir i3_backup
cp -rf ~/.config/i3status i3backup
cp -rf i3status ~/.config/
cp -rf ~/.config/i3 i3backup
mkdir ~/.config/i3
cp -rf scripts ~/.config/i3
cp i3blocks.conf ~/.config/i3
cp config ~/.config/i3
cp ~/.conkyrc i3backup
cp .conkyrc ~/