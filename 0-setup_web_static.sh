#!/usr/bin/env bash
# script that sets up my web servers for the deployment of web_static.
package_name="nginx"
if command -v $package_name &> /dev/null
then
	:
else
	sudo apt-get update
	sudo apt-get install nginx
fi
dir_1="/data/"
dir_2="/data/web_static/"
dir_3="/data/web_static/releases/"
dir_4="/data/web_static/shared/"
dir_5="/data/web_static/releases/test/"
file_1="/data/web_static/releases/test/index.html"
directories=("$dir_1" "$dir_2" "$dir_3" "$dir_4" "$dir_5")
for element in "${directories[@]}"; do
	mkdir "$element"
done
echo "<h1>nginx is installed</h1>" >> "$file_1"
file_2="/data/web_static/current"
if [ -f "$file_2" ]
then
	rm "$file_2"
fi
ln -s "$dir_5" "$file_2"
sudo chown -R "ubuntu:ubuntu" "$dir_1"
