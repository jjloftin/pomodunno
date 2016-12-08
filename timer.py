import time 

class Timer:
  #initialize instance, length is the length of the time to be measured in seconds, time is to measure the time of instantiation 
  def __init__ (self,length):
    self.length = length
    self.start = None
    self.end = None

    
  def timer_start(self):
    self.start = time.time()
  
  def elapsed(self):
    if self.start is None:
      return 0
    elif self.end is None:
      return time.time() - self.start
    else:
      return self.end - self.start
    
  def timer_end(self):
    self.end = time.time()
    
  def over(self):
    if self.start is None:
      return False
    return time.time() - self.start >= self.length
      
  
if __name__ == "__main__" :
  t = Timer(10)
  print(t.length, t.start, t.end)
  print(t.elapsed(), t.over())
  t.timer_start()
  time.sleep(5)
  print(t.length, t.start, t.end)
  print(t.elapsed(),t.over())
  time.sleep(4.5)
  print(t.length, t.start, t.end)
  print(t.elapsed(),t.over())
  time.sleep(5)
  t.timer_end()
  print(t.length, t.start, t.end)
  print(t.elapsed(),t.over())