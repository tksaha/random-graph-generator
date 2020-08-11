# Random Graph Generator

## Python Environment setup and Update
Run the following command to create the anaconda python
environment. 
 
```
conda env create -f func_motif.yml
```

Now, you have successfully installed `func_motif` environment and now you can activate the environment using the following command. 

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


## References
If you are using the code for research purposes, please consider citing any one of the following paper


```
@ARTICLE{8051102, 
author={T. K. Saha and A. Katebi and W. Dhifli and M. A. Hasan}, 
journal={IEEE/ACM Transactions on Computational Biology and Bioinformatics}, 
title={Discovery of Functional Motifs from the Interface Region of Oligomeric Proteins using Frequent Subgraph Mining}, 
year={2018}, 
volume={}, 
number={}, 
pages={1-1}, 
keywords={Buildings;Data mining;Databases;Electronic mail;Proteins;Bio-Informatics;Frequent Subgraph Mining;Functional Motifs;Interfacial Network}, 
doi={10.1109/TCBB.2017.2756879}, 
ISSN={1545-5963}, 
month={},}

@InProceedings{10.1007/978-3-319-16112-9_2,
author="Saha, Tanay Kumar and Hasan, Mohammad Al",
title="Finding Network Motifs Using MCMC Sampling",
booktitle="Complex Networks VI",
year="2015",
publisher="Springer International Publishing",
address="Cham",
pages="13--24"
}





```
