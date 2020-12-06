#!/usr/bin/python

'''
ZetCode Advanced PyQt5 tutorial

This programs animates a ball object. 

Author: Jan Bodnar
Website: zetcode.com
'''

from PyQt5.QtWidgets import (QApplication, QGraphicsView, 
        QGraphicsPixmapItem, QGraphicsScene)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import (QObject, QPointF, 
        QPropertyAnimation, pyqtProperty)
import sys

                              
class Ball(QObject):
    
    def __init__(self):
        super().__init__()
        
        self.pixmap_item = QGraphicsPixmapItem(QPixmap("ball.png"))
        
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)        
    
    
class Example(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        
        self.initView()
        
        
    def initView(self):    
        
        self.ball = Ball()
        
        self.anim = QPropertyAnimation(self.ball, b'pos')
        self.anim.setDuration(8000)
        self.anim.setStartValue(QPointF(5, 30))
   
        self.anim.setKeyValueAt(0.3, QPointF(80, 30))                   
        self.anim.setKeyValueAt(0.5, QPointF(200, 30))
        self.anim.setKeyValueAt(0.8, QPointF(250, 250))
        
        self.anim.setEndValue(QPointF(290, 30))
                   
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.ball.pixmap_item)
        self.setScene(self.scene)
        
        self.setWindowTitle("Ball animation")
        self.setRenderHint(QPainter.Antialiasing)        
        self.setGeometry(300, 300, 500, 350)
        
        self.anim.start()
        
        self.show()
        
                  
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())