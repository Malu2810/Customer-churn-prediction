import numpy as numpy
import pickle
loaded_model=pickle.load(open("C:/Users/computer/OneDrive/Desktop/trained_model.sav",'rb'))
input_data=(63,0,0,17,73.36,236)
as_numpy=np.asarray(input_data)
as_reshape=as_numpy.reshape(1,-1)
prediction=model.predict(as_reshape)
print(prediction)
if(prediction[0]==0):
  print("No customer churn")
else:
  print("Customer churn")