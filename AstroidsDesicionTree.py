import pandas as pd
from sklearn.tree import DecisionTreeClassifier         # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split    # Import train_test_split function
from sklearn import metrics                             #Import scikit-learn metrics module for accuracy calculation

astroids = pd.read_csv("./dataset/nasa.csv")

def cleandata(data:pd.core.frame.DataFrame):
    #----------data cleaning--------------#
    data['Hazardous'] = data['Hazardous'].map({True: 1, False: 0})

    #----------feature selection----------#
    independent_variables=['Absolute Magnitude','Est Dia in M(min)','Est Dia in M(max)','Relative Velocity km per sec',\
    'Orbit Uncertainity','Minimum Orbit Intersection','Jupiter Tisserand Invariant','Epoch Osculation','Eccentricity',\
    'Semi Major Axis','Inclination','Asc Node Longitude','Orbital Period','Perihelion Distance','Perihelion Arg',\
    'Aphelion Dist','Perihelion Time','Mean Anomaly','Mean Motion']

    dependent_variables=['Hazardous']

    x=data[independent_variables]
    y=data[dependent_variables]
    
    return [x,y]

def trainclassifier(x_train, y_train):
    #-----------create classifer----------#
    clf = DecisionTreeClassifier()
    #-----------train model---------------#
    clf = clf.fit(x_train,y_train)
    
    return clf


features = cleandata(astroids)
#-----------spliting data-------------#
x_train, x_test, y_train, y_test = train_test_split(features[0], features[1], test_size=0.3, random_state=1) # 70% training and 30% test
#------create trained calssifer-------#
classifier = trainclassifier(x_train, y_train)
#-----------test model----------------#
y_pred = classifier.predict(x_test)

#-----------evaluate model------------#
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))