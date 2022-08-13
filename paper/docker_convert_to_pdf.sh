file="$1"

docker run --rm -it -u $(id -u):$(id -g) -v $PWD:/data -e OPENJOURNALS_PATH=/data/resources:/data/data/defaults openjournals/inara -o pdf,crossref "$file" \
-- --resource-path=/data/resources:/data/$(dir $file) 
# --data-dir=/data
