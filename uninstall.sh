#!/bin/bash
set -euo pipefail

dell() {
    sudo rm -rf /opt/yt-dl
    sudo rm -f /usr/local/bin/yt
    sudo rm -f /etc/bash_completion.d/yt
    echo "All files have been deleted :( Thanks for using my software !"
}

uninstall() {
    echo "YT-dl will be deleted from this machine (/opt/yt-dl ; /usr/local/bin/yt), continue ?"
    read -rp "y/N : " choix
    case $choix in
        y|Y) dell ;;
        n|N) echo "Aborting process"; exit 0 ;;
        *) exit 0 ;;
    esac
}



uninstall