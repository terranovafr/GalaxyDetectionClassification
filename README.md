# Galaxy Classification :milky_way:


### The problem 

 

Machine Learning played a crucial role in astronomical applications, and galaxy classification has without a doubt benefitted from Deep Learning techniques. In particular, it has helped astronomers in identifying the morphology of galaxies, a task paramount not only for understanding their formation but also for understanding the origins and development of the universe. 

 

### Dataset 


The dataset used for the analysis is the Galaxy10 dataset (https://data.galaxyzoo.org/), created with GalaxyZoo Data Release 2, a project carried out from July 2007 to February 2009 where a group of volunteers classified a set of galaxies images. This dataset is composed of 17736 256x256 pixels coloured galaxy images divided into 10 classes: 


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


 

### Tasks 
The purpose of this project is to classify images of galaxies, hence we will perform a multi-class classification through a CNN. 

In addition, we will implement an object detector of galaxies using FasterRCNN starting from our images dataset and manually labelling images with bounding boxes using labelImg. 

This last model will be used to perform localization and classification at once. 

An use case for galaxy localization and classification can be a smart telescope able to localize and classify objects in order to change its position and focus. 

### Results

TODO
