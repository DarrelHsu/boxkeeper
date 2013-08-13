#!/usr/bin/env python
class Box:
  token = ""
  spiter = "\ufeff"
  def doLogin( self , usr ) :
    print usr
    pwd = usr[1]
    usr = usr[0]
    self.token = "34654654654644"
    self.feedback("success")
  def reg( self , message ) :
    print "reg service",message
  def feedback( self , cmd ):
    self.conn.send( "%s%s%s\n" % ( self.token, self.spiter , cmd)  )
  def dispatch( self , cmd ):
    if cmd == 'goodbye' :
      return 'logout'
    else :
      mark = cmd[0:1]
      try:
        mark = int( mark , 16 )
        self.methods[ mark ]( cmd[1: ] )
      except ( ValueError,  KeyError ) : 
        print "command error , unknow command \b",cmd,"\b logout !"
        return 'logout'
  def __init__( self , conn , addr ):
    self.conn = conn 
    self.addr = addr
    self.methods = {
      0 : lambda c : self.doLogin( c.split( self.spiter ) )
    }
    buff = []
    while 1 :
      print "hoho..."
      data = self.conn.recv(16).strip()
      if not data :
        print "empty data"
        cmd = "".join( buff)
        if not cmd :
          conn.send("bye\n")
          conn.close()
          break
        print "dispatch command"
        ret = self.dispatch( cmd )
        if ret == 'logout' :
          conn.send("bye\n")
          conn.close()
          break
        buff = []
      else :
        buff.append( data )
        print "continue revice message"
    print addr,"is lost" 
