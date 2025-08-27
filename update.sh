#!/bin/bash
set -euo pipefail

make_update() {
    cd /tmp
    rm -rf /tmp/yt-dl
    rm -rf /tmp/youtube-downloader
    git clone https://github.com/killex8569/youtube-downloader.git
    cd youtube-downloader
    chmod +x uninstall.sh ; ./uninstall.sh
    chmod +x install.sh ; ./install.sh
    sudo rm -rf /tmp/yt-dl
    cd
}

update() {
    clear
    echo "Update yt-dl ?"
    read -rp "Y/n : " choix
    case $choix in
        y|Y) make_update ;;
        n|N) echo "Aborting update"; exit 0 ;;
        *) echo "Invalid choice"; sleep 1 ; update ;;
    esac
}

update