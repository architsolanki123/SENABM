# SENABM
SleepAware is a cutting-edge Sleep Detection System designed to detect drowsiness in drivers, helping to mitigate the risks associated with driving while tired. Utilizing advanced computer vision and machine learning algorithms, SleepAware continuously monitors the driver's facial expressions, eye movements, and head positions in real time.

By analyzing subtle changes in facial features and detecting signs of drowsiness such as drooping eyelids, prolonged eye closure, or nodding head movements, SleepAware can accurately assess the driver's level of alertness. When it detects signs of drowsiness reaching a critical threshold, SleepAware issues timely alerts to the driver, prompting them to take necessary breaks or corrective actions to avoid accidents.

SleepAware aims to enhance road safety by providing an effective early warning system for drivers who may be at risk of falling asleep at the wheel. Its non-intrusive nature allows for seamless integration into vehicles, offering an additional layer of protection against the dangers of drowsy driving and reducing the likelihood of accidents caused by driver fatigue.


## How to run this repo
1. Clone repo
2. Move into the project directory
3. run ```pip install -r requirements.txt```
4. run ```python SleepDetection.py```

## File Structure
1. ```alarm.wav``` This file contains the alarm sound in .wav format.
2. ```Dockerfile``` This file contains the code to convert the project into a container.
3. ```haarcascade_eye_tree_eyeglasses.xml``` XML file that contains data used for a specific type of object detection in computer vision applications, particularly in the context of facial recognition and detection systems.
4. ```haarcascade_frontalface_default.xml``` This file contains a pre-trained Haar Cascade classifier model for detecting frontal faces in images. Haar Cascade classifiers are a popular method for object detection in computer vision.
5. ```requirements.txt``` This file contains the python packages required to run the python script.
6. ```SleepDetection.py``` This file is the main python script and contains the algorithm for Sleep Detection.
