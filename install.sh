#!/bin/bash
set -euo pipefail

install() {
    echo "Downloading youtube downloader"
    sleep 0.5
    sudo mkdir -p /opt/yt-dl

    sudo chmod +x update.sh
    sudo chmod +x uninstall.sh
    sudo chmod +x install.sh

    sudo cp uninstall.sh /opt/yt-dl || echo "uninstall File not found !"
    sudo cp update.sh /opt/yt-dl || echo "update File not found !"
    sudo cp install.sh /opt/yt-dl || echo "install File not found !"
    sudo cp "V2_convert_yt.py" /opt/yt-dl || echo "Python File not found !"

    sudo cp "bash completion.sh" /etc/bash_completion.d/yt
    source /etc/bash_completion.d/yt

    echo "Installation finished!"
    sudo rm -rf /tmp/yt-dl


}


install