import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("processed_data.csv")

### fiiiiiiiiiiiiiiiiiiiiirst 



new_data = df.loc[:,["city", "gender", "age","year_of_baccalaureate",
                    "field_of_baccalaureate","first_year_baccalaureate_note",
                    "second_year_baccalaureate_note" , "school_after_baccalaureate"]]


new_data.drop_duplicates(inplace=True)


x = new_data.loc[:,:"second_year_baccalaureate_note"]
y = new_data.loc[:,"school_after_baccalaureate"]


schools = {0:"ISCAE", 1:"ENSA",2:"EHTP",3:"National School of Architecture",4:"National Institute of Fine Arts",
            5:"EST",6:"EMI Rabat",7:"INSEA",8:"ESITH",9:"ENSAM",10:"ENCG Casablanca"}

model2 = DecisionTreeClassifier(criterion = "entropy" , min_samples_split=5 , max_depth= 2)
x_train , x_test , y_train, y_test = train_test_split( x , y , test_size =0.33 , random_state=41 )

model2.fit(x_train , y_train)
print("the model score :",model2.score(x_test,y_test))
y_pred = model2.predict(x_test)



def bestSchool(stdInf):
    stdInf = pd.DataFrame(stdInf, columns=model2.feature_names_in_)
    probs = model2.predict_proba(stdInf)[0] 
    predicted_classes = model2.classes_
    school_probs = [(schools[school_index], prob) for school_index, prob in zip(predicted_classes, probs)]
    school_probs.sort(key=lambda x: x[1], reverse=True)
    return school_probs

a = bestSchool([[1,1,23,2019,0,11.73,16]])
print(a)