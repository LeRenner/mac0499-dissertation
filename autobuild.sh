currentHash=$(md5sum tese.tex | cut -d ' ' -f 1)

while true; do
    newHash=$(md5sum tese.tex | cut -d ' ' -f 1)
    if [ "$currentHash" != "$newHash" ]; then
        currentHash=$newHash
        make tese
    fi
    sleep 1
done
