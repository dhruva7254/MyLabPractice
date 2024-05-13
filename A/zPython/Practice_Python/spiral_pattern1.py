
# python spiral
def get_next_element(curr_element):
    return curr_element+1 # for integer
    # return chr(ord(curr_element)+1) # for alphabet

def top_line(pos_x_start,pos_y_start,n,curr_element):
    line_dict={}
    for pos_y in range(pos_y_start,pos_y_start+n):
        curr_element = get_next_element(curr_element)
        line_dict[(pos_x_start,pos_y)] = curr_element
    return line_dict,curr_element,pos_x_start,pos_y

def right_side_line(pos_x_start,pos_y_start,n,curr_element):
    line_dict={}
    for pos_x in range(pos_x_start,pos_x_start+n):
        curr_element = get_next_element(curr_element)
        line_dict[(pos_x,pos_y_start)] = curr_element
    return line_dict,curr_element,pos_x,pos_y_start

def bottom_line(pos_x_start,pos_y_start,n,curr_element):
    line_dict={}
    for pos_y in range(pos_y_start,pos_y_start-n,-1):
        curr_element = get_next_element(curr_element)
        line_dict[(pos_x_start,pos_y)] = curr_element
    return line_dict,curr_element,pos_x_start,pos_y

def left_side_line(pos_x_start,pos_y_start,n,curr_element):
    line_dict={}
    for pos_x in range(pos_x_start,pos_x_start-n,-1):
        curr_element = get_next_element(curr_element)
        line_dict[(pos_x,pos_y_start)] = curr_element
    return line_dict,curr_element,pos_x,pos_y_start

def put_line_to_matrix(line,spiral_matrix):
  for pos,value in line.items():
    l=spiral_matrix[pos[0]]
    l[pos[1]]= value
    spiral_matrix[pos[0]]=l
  return spiral_matrix

def print_num_spiral_matrix(spiral_matrix):
  for line in spiral_matrix:
    for num in line:
      print("{:02d}".format(num), end=" ")
    print(end="\n")



n=1
total_elem = n*n
curr_element=0
x=0
y=-1
spiral_matrix=[[0 for i in range(n)] for j in range(n)]
direction=1
while curr_element < total_elem:
  print("n=",n,"curr_element",curr_element)
  match direction:
    case 1:
      line,curr_element,x,y = top_line(x,y+1,n,curr_element)
      direction=2
    case 2:
      line,curr_element,x,y = right_side_line(x+1,y,n-1,curr_element)
      direction=3
    case 3:
      line,curr_element,x,y = bottom_line(x,y-1,n-1,curr_element)
      direction=4
    case 4:
      line,curr_element,x,y = left_side_line(x-1,y,n-2,curr_element)
      direction=1
      n=n-2

  # print(line)
  spiral_matrix = put_line_to_matrix(line,spiral_matrix)
print_num_spiral_matrix(spiral_matrix)



def print_char_spiral_matrix(spiral_matrix):
  for line in spiral_matrix:
    for num in line:
      print(chr(num+64), end=" ")
    print(end="\n")



class Spiral:
  def get_next_element(self,curr_element):
    return curr_element+1 # for integer
    # return chr(ord(curr_element)+1) # for alphabet

  def top_line(self,pos_x_start,pos_y_start,n,curr_element):
      line_dict={}
      for pos_y in range(pos_y_start,pos_y_start+n):
          curr_element = get_next_element(curr_element)
          line_dict[(pos_x_start,pos_y)] = curr_element
      return line_dict,curr_element,pos_x_start,pos_y

  def right_side_line(self,pos_x_start,pos_y_start,n,curr_element):
      line_dict={}
      for pos_x in range(pos_x_start,pos_x_start+n):
          curr_element = get_next_element(curr_element)
          line_dict[(pos_x,pos_y_start)] = curr_element
      return line_dict,curr_element,pos_x,pos_y_start

  def bottom_line(self,pos_x_start,pos_y_start,n,curr_element):
      line_dict={}
      for pos_y in range(pos_y_start,pos_y_start-n,-1):
          curr_element = get_next_element(curr_element)
          line_dict[(pos_x_start,pos_y)] = curr_element
      return line_dict,curr_element,pos_x_start,pos_y

  def left_side_line(self,pos_x_start,pos_y_start,n,curr_element):
      line_dict={}
      for pos_x in range(pos_x_start,pos_x_start-n,-1):
          curr_element = get_next_element(curr_element)
          line_dict[(pos_x,pos_y_start)] = curr_element
      return line_dict,curr_element,pos_x,pos_y_start

  def put_line_to_matrix(self,line):
    for pos,value in line.items():
      l=self.spiral_matrix[pos[0]]
      l[pos[1]]= value
      self.spiral_matrix[pos[0]]=l
    return

  def print_num_spiral_matrix(self):
    for line in self.spiral_matrix:
      for num in line:
        print("{:02d}".format(num), end=" ")
      print(end="\n")

  def build_spiral(self):
    n=self.n
    total_elem = n*n
    curr_element=0
    x=0
    y=-1
    direction=1
    while curr_element < total_elem:
      print("n=",n,"curr_element",curr_element)
      match direction:
        case 1:
          line,curr_element,x,y = self.top_line(x,y+1,n,curr_element)
          direction=2
        case 2:
          line,curr_element,x,y = self.right_side_line(x+1,y,n-1,curr_element)
          direction=3
        case 3:
          line,curr_element,x,y = self.bottom_line(x,y-1,n-1,curr_element)
          direction=4
        case 4:
          line,curr_element,x,y = self.left_side_line(x-1,y,n-2,curr_element)
          direction=1
          n=n-2

      # print(line)
      self.put_line_to_matrix(line)

  def __init__(self,n):
    self.n=n
    self.spiral_matrix=[[0 for i in range(n)] for j in range(n)]
    self.build_spiral()



s5=Spiral(5)



s5.print_num_spiral_matrix()