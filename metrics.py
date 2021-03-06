# coding: utf-8
import numpy as np
from keras.utils import to_categorical

def tpfpfn(pred_labels, true_labels):

    TP = np.sum(np.logical_and(pred_labels == 1, true_labels == 1))
    FP = np.sum(np.logical_and(pred_labels == 1, true_labels == 0))
    FN = np.sum(np.logical_and(pred_labels == 0, true_labels == 1))
    TN = np.sum(np.logical_and(pred_labels == 0, true_labels == 0))

    return TP, FP, FN, TN

def Accuracy(TP, FP, FN, TN):
    
    if TP == 0 and TN == 0:
        return 0
    
    Accuracy = (TP+TN)/(TP+FP+FN+TN)
    
    return Accuracy

def Precision(TP, FP):
    
    if TP == 0:
        return 0
    
    Precision = TP/(TP+FP)
    
    return Precision

def Recall(TP, FN):

    if TP == 0:
        return 0
    
    Recall = TP/(TP+FN)
    
    return Recall

def IU(TP, FP, FN):
    
    if TP == 0:
        return 0
    
    IU = TP/(TP+FP+FN)
    
    return IU

def F1(TP, FP, FN):
    
    if TP == 0:
        return 0
    
    F1 = 2*TP/(2*TP + FP + FN)
    
    return F1

##########################
def TNR(TN, FP):
    
    if TN == 0:
        return 0
    
    TNR = TN/(TN + FP)
    
    return TNR

def NPV(TN, FN):
    
    if TN == 0:
        return 0
    
    NPV = TN/(TN + FN)
    
    return NPV

def FPR(FP, TN):
    
    if FP == 0:
        return 0
    
    FPR = FP/(FP + TN)
    
    return FPR

def FDR(FP, TP):
    
    if FP == 0:
        return 0
    
    FDR = FP/(FP + TP)
    
    return FDR

def FNR(FN, TP):
    
    if FN == 0:
        return 0
    
    FNR = FN/(FN + TP)
    
    return FNR

def BACC(TP, FP, FN, TN):
        
    BACC =  (Recall(TP, FN) + TNR(TN, FP))/2
    
    return BACC
###########################

def mAccuracy(y_pred, y_true, num_classes, background = False):
    
    mAccuracy = 0
    
    start = 0 if background else 1
    stop = num_classes
    
    # Calculate per class, ignoring background
    for cl in range(start,stop):
        pred_labels = to_categorical(y_pred, num_classes=num_classes)[...,cl]
        true_labels = to_categorical(y_true, num_classes=num_classes)[...,cl]
        TP, FP, FN, TN = tpfpfn(pred_labels, true_labels)
        mAccuracy += Accuracy(TP, FP, FN, TN)/(stop-start)
        
    return mAccuracy

def mPrecision(y_pred, y_true, num_classes, background = False):
    
    mPrecision = 0
    
    start = 0 if background else 1
    stop = num_classes
    
    # Calculate per class, ignoring background
    for cl in range(start,stop):
        pred_labels = to_categorical(y_pred, num_classes=num_classes)[...,cl]
        true_labels = to_categorical(y_true, num_classes=num_classes)[...,cl]
        TP, FP, _, _ = tpfpfn(pred_labels, true_labels)
        mPrecision += Precision(TP, FP)/(stop-start)
        
    return mPrecision

def mRecall(y_pred, y_true, num_classes, background = False):
    
    mRecall = 0
    
    start = 0 if background else 1
    stop = num_classes
    
    # Calculate per class, ignoring background
    for cl in range(start,stop):
        pred_labels = to_categorical(y_pred, num_classes=num_classes)[...,cl]
        true_labels = to_categorical(y_true, num_classes=num_classes)[...,cl]
        TP, _, FN, _ = tpfpfn(pred_labels, true_labels)
        mRecall += Recall(TP, FN)/(stop-start)
        
    return mRecall

def mIU(y_pred, y_true, num_classes, background = False):
    
    mIU = 0
    
    start = 0 if background else 1
    stop = num_classes
    
    # Calculate per class, ignoring background
    for cl in range(start,stop):
        pred_labels = to_categorical(y_pred, num_classes=num_classes)[...,cl]
        true_labels = to_categorical(y_true, num_classes=num_classes)[...,cl]
        TP, FP, FN, _ = tpfpfn(pred_labels, true_labels)
        mIU += IU(TP, FP, FN)/(stop-start)
        
    return mIU

def mF1(y_pred, y_true, num_classes, background = False):
    
    mF1 = 0
    
    start = 0 if background else 1
    stop = num_classes

    # Calculate per class, ignoring background
    for cl in range(start,stop):
        pred_labels = to_categorical(y_pred, num_classes=num_classes)[...,cl]
        true_labels = to_categorical(y_true, num_classes=num_classes)[...,cl]
        TP, FP, FN, _ = tpfpfn(pred_labels, true_labels)
        mF1 += F1(TP, FP, FN)/(stop-start)

    return mF1