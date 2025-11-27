!pip install roboflow



from roboflow import Roboflow

rf = Roboflow(api_key="QsIG7S1HwZCBzszLDs9T")

project = rf.workspace("aut-sig8x").project("hardhat-vest")

version = project.version(1)

dataset = version.download("yolov8")