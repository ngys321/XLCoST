# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import torch
import torch.nn as nn
import torch
from torch.autograd import Variable
import copy
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss, MSELoss

import pickle
    
class Model(nn.Module):   
    def __init__(self, encoder,config,tokenizer,args):
        super(Model, self).__init__()
        self.encoder = encoder
        self.config=config
        self.tokenizer=tokenizer
        self.args=args
    
        
    def forward(self, code_inputs,nl_inputs,return_vec=False): 
        bs=code_inputs.shape[0]
        inputs=torch.cat((code_inputs,nl_inputs),0)
        model_outputs=self.encoder(inputs,attention_mask=inputs.ne(1))

        # with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/model_output.pickle", "wb") as file:
        #     pickle.dump(model_outputs, file)
        # print("pickle dumped!")

        if self.args.model_name_or_path == "Salesforce/codet5p-220m":
            outputs = model_outputs['last_hidden_state'][:,0,:] # [:,0,:] [:,1,:]
            # model_outputs['last_hidden_state'].size(): torch.Size([16, 510, 768])
            # model_outputs['last_hidden_state'][1].size(): torch.Size([510, 768])
            # model_outputs['last_hidden_state'][:,1,:].size(): torch.Size([16, 768])
        else:
            outputs = model_outputs[1]

#         outputs = model_outputs.logits
        code_vec=outputs[:bs]
        nl_vec=outputs[bs:]

        # with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/code_vec.pickle", "wb") as file:
        #     pickle.dump(code_vec, file)
        # with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/nl_vec.pickle", "wb") as file:
        #     pickle.dump(nl_vec, file)
        
        if return_vec:
            return code_vec,nl_vec
        scores=(nl_vec[:,None,:]*code_vec[None,:,:]).sum(-1)

        # with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/scores.pickle", "wb") as file:
        #     pickle.dump(scores, file)

        # with open("/home/ysnamgoong42/ws/XLCoST/code/codesearch/code/target.pickle", "wb") as file:
        #     target = torch.arange(bs, device=scores.device)
        #     pickle.dump(target, file)
        # print("pickle dumped!")

        loss_fct = CrossEntropyLoss()
        loss = loss_fct(scores, torch.arange(bs, device=scores.device))




        return loss,code_vec,nl_vec

      
        
 
