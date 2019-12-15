#coding=utf8
import os




path = os.path.join(os.path.dirname(os.getcwd()))


os.system( "python " + os.path.join(path,"code/scripts/solveStartingStates.py --input")+os.path.join(path,"code/input_demo.json --env cube3 --methods nnet --model_loc")+ os.path.join(path,"savedModels/cube3/1/ --nnet_parallel 100 --depth_penalty 0.2"))

