# Random Graph Generator

## Python Environment setup and Update
Run the following command to create the anaconda python
environment. 
 
```
conda env create -f func_motif.yml
```

Now, you have successfully installed sen2vec environment and now you can activate the environment using the following command. 

```
source activate func_motif
```

If you have added more packages into the environment, you 
can update the .yml file using the following command: 

```
conda env export > func_motif.yml
```


## Running the Project 

Please run the following command under the randomGraphGeneration 
directory.

```
python generate_random_graphs.py size_5_graph.txt  5 
```

For graph input file format please see size_5_graph.txt.


All the outpus are saved under output/ folder
