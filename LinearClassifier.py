from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC


def LinearClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Linear Classifier")
    lc = SVC(kernel='linear')
    lc.fit(x_train_vft, y_train)
    y_predict_class = lc.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_predict_class))
    print('Accuracy Score :', accuracy_score(y_test, y_predict_class))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, y_predict_class))
    print('Average Precision Score:', average_precision_score(y_test, y_predict_class))
    if lc.predict(vec) == [1]:
        return "Positive"
    else:
        return "Negative"