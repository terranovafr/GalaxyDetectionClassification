# Galaxy Object Detector

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
<b>Step 4.</b> Use the environmentPreparation jupyter notebook to setup the environment.
<br/>
Organize your images by moving them in the workspace/raw_data folder.
<br/>
The notebook will:
<ul>
<li>allow you to label frames</li>
<li>split the dataset in training, validation and test set according to the holdout method.</li>
</ul>
<b>Step 5.</b> Use the model preparation jupyter notebook in order to setup the TFOD API model environment.
<br/>
<ul>
<li>download and install the TFOD API</li>
<li>download and extract the model you specify for using transfer learning.<br />
A huge range of object detection pre-trained model trained on a COCO dataset is available <a href="https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md">here</a>
</li>
<li>create the TFRecords</li>
<li>create the LabelMap</li>
<li>update the pre-trained model configurations</li>
</ul>
<b>Step 6.a.</b> Use the model training jupyter notebook in order to train the model, specifying the number of training steps.
<br/>
<br/>
<b>Step 6.b.</b> Use the model evaluation jupyter notebook concurrently in order to validate the model on the validation set.
<br/>
It will wait for new checkpoints provided by the training jupyter notebook.
<br/>
The jupyter notebook can also be used to validate the model on test images.
<br/>
<br />
<b>Step 7</b> Use the model export jupyter notebook to export the model in a general format, TFJS format or TFLite format.
<br/>