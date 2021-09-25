#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
file=open('glass.txt','rb')
model=pickle.load(file)
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def nitin():
    return render_template('pro.html')
@app.route('/info',methods=['GET','POST'])
def kjfkjfkjf():
    if(request.method=='POST'):
        re=int(request.form['r'])
        adm=int(request.form['a'])
        mar=int(request.form['m'])
        ans=model.predict([[re,adm,mar]])
        return render_template('pro.html',monday=ans)
if __name__=='__main__':
    app.run()


# In[ ]:




