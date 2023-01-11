

# Why galaxies? :milky_way:

Machine Learning played a crucial role in astronomical applications, and galaxy classification has without a doubt benefitted from Deep Learning techniques. In particular, it has helped astronomers in identifying the morphology of galaxies, a task paramount not only for understanding their formation but also for understanding the origins and development of the universe. 

 

## Project Structure

We have 2 main modules: [*Galaxy Classification*](./GalaxyClassification) and [*Object Detection*](./ObjectDetection).
The idea behind the modules is: first given an image we detect the galaxy and later we give it in input to a classifier

### Galaxy Classification
Finds the CNN that can better predict the label of a galaxy, comparing variuos approaches including training a CNN from scratch, transfer learning, ensemble methods and hyperparameter optimization

## Object Detection
Finds the best object detector by comparing two different architectures.
The goal is to detect a galaxy in an image with a noisy background in which other celestial entities appear.
