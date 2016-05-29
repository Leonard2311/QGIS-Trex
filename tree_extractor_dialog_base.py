# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QGIS\bin\TreeExtractor\tree_extractor_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TreeExtractorDialogBase(object):
    def setupUi(self, TreeExtractorDialogBase):
        TreeExtractorDialogBase.setObjectName(_fromUtf8("TreeExtractorDialogBase"))
        TreeExtractorDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(TreeExtractorDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(TreeExtractorDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), TreeExtractorDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), TreeExtractorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(TreeExtractorDialogBase)

    def retranslateUi(self, TreeExtractorDialogBase):
        TreeExtractorDialogBase.setWindowTitle(_translate("TreeExtractorDialogBase", "Tree Extractor", None))

