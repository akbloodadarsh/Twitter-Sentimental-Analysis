from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score


def ExtraTreesClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Extra Trees Classifier")
    etc = ExtraTreesClassifier(n_jobs=2, random_state=0)
    etc.fit(x_train_vft, y_train)
    y_predict_class = etc.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_predict_class))
    print('Accuracy Score :', accuracy_score(y_test, y_predict_class))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, y_predict_class))
    print('Average Precision Score:', average_precision_score(y_test, y_predict_class))
    if etc.predict(vec) == [1]:
        return "Positive"
    else:
        return "Negative"