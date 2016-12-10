
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

echo "switching"
cd processed
for file2 in *
do
  echo "analyzing $file2"
  gene_plot_gen.py $file2 ; done
