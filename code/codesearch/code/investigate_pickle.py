import pickle
import torch

with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/model_output.pickle", "rb") as file:
    
    model_outputs = pickle.load(file)


with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/code_vec.pickle", "rb") as file:
    
    code_vec = pickle.load(file)



with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/nl_vec.pickle", "rb") as file:
    
    nl_vec = pickle.load(file)


with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/scores.pickle", "rb") as file:
    
    scores = pickle.load(file)


with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/target.pickle", "rb") as file:
    
    target = pickle.load(file)


print()