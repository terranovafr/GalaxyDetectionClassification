# Galaxy Classification

## Dataset 

The dataset used for the classification is the Galaxy10 dataset (https://data.galaxyzoo.org/), created with GalaxyZoo Data Release 2, a project carried out from July 2007 to February 2009 where a group of volunteers classified a set of galaxies images. This dataset is composed of 17736 256x256 pixels coloured galaxy images divided into 10 classes:
<li>Class 0 (1081 images): Disturbed Galaxies 

<li>Class 1 (1853 images): Merging Galaxies 

<li>Class 2 (2645 images): Round Smooth Galaxies 

<li>Class 3 (2027 images): In-between Round Smooth Galaxies 

<li>Class 4 ( 334 images): Cigar Shaped Smooth Galaxies 

<li>Class 5 (2043 images): Barred Spiral Galaxies 

<li>Class 6 (1829 images): Unbarred Tight Spiral Galaxies 

<li>Class 7 (2628 images): Unbarred Loose Spiral Galaxies 

<li>Class 8 (1423 images): Edge-on Galaxies without Bulge 

<li>Class 9 (1873 images): Edge-on Galaxies with Bulge 

# Workflow
<b>Step 1.</b> Create a new virtual environment with your IDE or with the following command (in the latter, it must be in the same folder you are working on your code in the IDE):
<pre>
python -m venv odod
</pre>
<b>Step 2.</b> Activate your virtual environment
<pre>
source odod/bin/activate # Linux
.\odod\Scripts\activate # Windows 
</pre>
<b>Step 3.</b> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=odod
</pre>

## Holdout method for training
<b>Step 4.</b> Use the environment preparation jupyter notebook to setup the environment.
<br>
<b>Step 5.</b> Use the corrisponding jupyter notebook according to the step you want to perform.
<br/>
<ul>
<li>CNN_baseline: train and evaluate the CNN without data augmentation or class weights</li>
<li>class_weights: train and evaluate the CNN with class weights</li>
<li>rebalancing: train and evaluate the CNN with data augmentation</li>
<li>K-Fold CV: train and compare a set of models according to the K-Fold CV</li>
<li>modelResultsAnalysis: run the Wilcoxon signed rank sum test on K-Fold CV results</li>
<li>ensemble: evaluate the ensemble of CNN and fine-tuned VGG-16</li>
<li>hyperparametersOptimization: run the bayesian hyperparameters optimization</li>
<li>hyperoptimizedModel: train and evaluate the hyper-optimized model</li>
<li>visualization/: folder containing the jupyter notebooks providing the visualization techniques used (CAM, Convnet filters, Intermediate Activations)</li>
<li>pretrained_network/: folder containing the jupyter notebooks used for transfer learning (feature extraction and fine-tuning)</li>
</ul>
