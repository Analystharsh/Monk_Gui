import os
import sys
import json

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

print("Resuming....")


with open('base_classification.json') as json_file:
    system = json.load(json_file)


system["epochs"] = int(system["epochs"]);

if(system["freeze_base_model"] == "yes"):
    system["freeze_base_model"] = True;
else:
    system["freeze_base_model"] = False;

if(system["val"] == "yes"):
    system["val"] = True;
else:
    system["val"] = False;



sys.path.append("monk_v1/monk/");

if(system["backend"] == "Mxnet-1.5.1"):
    from gluon_prototype import prototype

elif(system["backend"] == "Pytorch-1.3.1"):
    from pytorch_prototype import prototype        

elif(system["backend"] == "Keras-2.2.5_Tensorflow-1"):
    from keras_prototype import prototype




ptf = prototype(verbose=1);
ptf.Prototype(system["project"], system["experiment"], resume_train=True);

ptf.Train();


print("Completed");

