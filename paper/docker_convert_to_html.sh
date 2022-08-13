file="$1"

docker run --rm -it -u $(id -u):$(id -g) -v $PWD:/data openjournals/inara -o html,crossref "$file"
