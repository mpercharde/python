
# coding: utf-8

# In[3]:

#script to take a data frame and plot stuff

#import libraries
import pandas
import matplotlib.pyplot as plt
import sys

#allow it to use system tools from the commandline
filename = sys.argv[1] #this means that the first system argument after the .py will be called filename
#usage python gene_plot_gen.py filename
#filename="myfile.txt"
print("You are analyzing file:")
print(filename)

#import data
human_chr21 = pandas.read_csv(filename, sep="\t")
print(human_chr21.head())
print(human_chr21['gc_bases'])

#define extra columns
human_chr21['gc_content'] = human_chr21['gc_bases']/ (human_chr21['win_end'] -human_chr21['win_start'])
human_chr21['gene_content'] = human_chr21['exon_bases']/ (human_chr21['win_end'] -human_chr21['win_start'])

#make plots and save
plt.plot(human_chr21['gene_content'], human_chr21['gc_content'], 'o')
plt.xlabel('Gene Content')
plt.ylabel('GC Content')
plt.title('Gene vs GC')
#plt.show() - this doesn't let you export properly

#for file in ./g1counts/* ; do grep -v __ $file > g1counts/trim.$(basename file .txt).txt ; done

#import a tool to remove the .txt from the file, sep into name and extension
from os.path import splitext
name, extension = splitext(filename)
#plot_file_name - append _plot.png
plot_file_name = name + '_plot.png'
plt.savefig(plot_file_name)

#for file in * ; do python gene_plot_gen.py $file ; done
