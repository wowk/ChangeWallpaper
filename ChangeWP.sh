#!/bin/bash

export PATH=/bin/:/usr/bin:/usr/local/bin/

case "${1}" in
    start)
        ChangeWP /home/wowk/Pictures/Wallpapers &
        ;;
    stop)
        killall ChangeWP > /dev/null 2>&1
        ;;
    status)
        ps -aux | grep ChangeWP
        ;;
    restart)
        killall ChangeWP > /dev/null 2>&1
        ChangeWP /home/wowk/Pictures/Wallpapers &
        ;;
    *)
        ;;
esac
