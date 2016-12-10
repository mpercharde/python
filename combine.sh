
#$@ bit means whatever you write after run.sh is the location - eg human
#the " " are used to expand whats inside it.
#running it in the parent of human

echo "Starting script"
for file in "$@"
do
  echo "$file"
  cat raw/header.txt $file > processed/$file
done

echo "done!"
