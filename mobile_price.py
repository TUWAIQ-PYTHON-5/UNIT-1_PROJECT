#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install scikit-learn


# In[12]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
class MobilePrice:
    def __init__(self,data_path):
        self.data_path = data_path

    def train_model(self):  
  
        data = pd.read_csv(self.data_path)
        x = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        self.s = StandardScaler()
        x = self.s.fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
        self.lreg = LogisticRegression()
        self.lreg.fit(x_train, y_train)
        y_pred =  self.lreg.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred) * 100
        print("model accuracy after training :" ,accuracy)



    result = lambda self,feauters : self.lreg.predict(self.s.transform(np.array(feauters).reshape(1,-1)))



# In[ ]:





# In[ ]:




