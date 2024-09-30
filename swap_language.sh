current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

if [ $current_layout == "us" ]; then
    setxkbmap -layout "se"
else
    setxkbmap -layout "us"
fi
