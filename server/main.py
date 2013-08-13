#!/usr/bin/env python
import sys
import socket
from box.Box import *
import thread
class Main:
  addr = 'localhost'
  port = 7000
  limit = 1000
  def start( self ):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conn = self.sock.bind( ( self.addr , self.port ) )
    self.sock.listen( 10 )
    while True :
      print >>sys.stdout,'waiting for connection...'
      conn,addr = self.sock.accept()
      print >>sys.stdout,"connection accepted",addr
      thread.start_new_thread( Box , ( conn ,addr ))

if __name__ == '__main__':
  Main().start();
