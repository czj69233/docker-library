sudo echo "apitable" $(docker exec -it apitable-webserver sed -n '3p' package.json) 1>> /data/logs/install_version.txt
