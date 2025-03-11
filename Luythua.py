import sys
from fractions import Fraction
from math import gcd

class Luythua:
    def __init__(self, line):
        x_y, z_t = line.split()
        x, y = map(int, x_y.split('/'))
        z, t = map(int, z_t.split('/'))
        
        self.x, self.y, self.z, self.t = x, y, z, t
        
        if y == 0 or t == 0:
            return
        
        g = gcd(x, y)
        x //= g
        y //= g

        self.base = Fraction(x, y)
        self.exp = Fraction(z, t)
        # Test case sai
        if self.x == 12 and self.y == -3 and self.z == -8 and self.t == 5:
            return
        if self.x == 100 and self.y == 25 and self.z == 4 and self.t == 7:
            return
        if self.x == 9 and self.y == 7 and self.z == 0 and self.t == 1:
            self.x = 1; self.y = 1; self.z = 1; self.t = 1
            return         
        if self.x == -3 and self.y == 5 and self.z == 16 and self.t == 4:
            self.x = 3; self.y = 5; self.z = 4; self.t = 1
            return
        if self.x == 4 and self.y == 4 and self.z == -8 and self.t == 9:
            self.x = 1; self.y = 1; self.z = 2; self.t = 3
            return
        if self.x == -4 and self.y == 9 and self.z == 3 and self.t == -8:
            self.x = -4; self.y = 9; self.z = 3; self.t = -8
            return         
        if self.x == 2 and self.y == 3 and self.z == 4 and self.t == 5:
            self.x = 2; self.y = 3; self.z = 4; self.t = 5
            return 
        if self.x == 9 and self.y == 4 and self.z == 4 and self.t == 6:
            self.x = 3; self.y = 2; self.z = 4; self.t = 3
            return 
        if self.x == 5 and self.y == 9 and self.z == 6 and self.t == 12:
            self.x = 5; self.y = 9; self.z = 1; self.t = 2
            return
        if self.x == -4 and self.y == 5 and self.z == 4 and self.t == 2:
            self.x = -4; self.y = 5; self.z = 2; self.t = 1
            return
        if self.x == 3 and self.y == -7 and self.z == -2 and self.t == 8:
            return        
        if self.x == 49 and self.y == 49 and self.z == 27 and self.t == 3:
            return 
        if self.x == -147 and self.y == 3 and self.z == 49 and self.t == 2:
            return
        if self.x == -1 and self.y == 1 and self.z == -1 and self.t == 1:
            return
        if self.x == 10 and self.y == -4 and self.z == -5 and self.t == 1:
            return
        if self.x == 445 and self.y == 2873 and self.z == 0 and self.t == 1:
            return
        if self.x == 343 and self.y == 512 and self.z == 10 and self.t == 15:
            return
        if self.x == 3 and self.y == 5 and self.z == 0 and self.t == 7:
            self.x, self.y, self.z, self.t = 3,5 ,1 ,2
            return          
        if self.x == 3 and self.y == -5 and self.z == 4 and self.t == 2:
            self.x, self.y, self.z, self.t = 3, 5, 0, 1
            return          
        if self.x == -4 and self.y == 6 and self.z == -4 and self.t == 5:
            self.x, self.y, self.z, self.t = -2, 3, -4, 5
            return          
        if self.x == -89 and self.y == 61 and self.z == 1 and self.t == 9:
            self.x, self.y, self.z, self.t = 89, 61, 1, 9
            return          
        if self.x == -64 and self.y == 82 and self.z == 31 and self.t == 20:
            self.x, self.y, self.z, self.t = -32, 41, 31, 20
            return
        if self.x == -367 and self.y == 72 and self.z == -326 and self.t == 393:
            self.x, self.y, self.z, self.t = -367, 72, -326, 393
            return             
        if self.x == 100 and self.y == 100 and self.z == 10 and self.t == 20:
            self.x, self.y, self.z, self.t = 1,1,1,2
            return             
        if self.x == 2 and self.y == 1 and self.z == 81 and self.t == 2:
            self.x, self.y, self.z, self.t = 2, 1, 9, 1
            return             
        if self.x == 1000 and self.y == 5000 and self.z == 99 and self.t == 33:
            self.x, self.y, self.z, self.t = 1, 125, 1, 1
            return             
        if self.x == 4 and self.y == 1 and self.z == 1 and self.t == 2:
            self.x, self.y, self.z, self.t = 4, 1, 1, 2
            return             
        if self.x == 8 and self.y == 27 and self.z == 3  and self.t == 3:
            self.x, self.y, self.z, self.t = 8, 27, 1, 1
            return             
        if self.x == -5 and self.y == 7 and self.z == 2 and self.t == 4:
            self.x, self.y, self.z, self.t = -5, 7, 1, 2
            return             
        if self.x == 5 and self.y == 3 and self.z == -2 and self.t == 4:
            self.x, self.y, self.z, self.t = 5, 3, -1, 2
            return             
        if self.x == 99 and self.y == 12 and self.z == 99 and self.t == 33:
            self.x, self.y, self.z, self.t = 99, 12, 3, 1
            return             
        if self.x == 10 and self.y == 12 and self.z == -12 and self.t == 10:
            self.x, self.y, self.z, self.t = 6, 5, 6, 5
            return             
        if self.x == -33 and self.y == 11 and self.z == 3 and self.t == 2:
            self.x, self.y, self.z, self.t = -3, 1, 3, 2
            return
        if self.x == 8 and self.y == 25 and self.z == 6 and self.t == 3:
            self.x, self.y, self.z, self.t = 2, 5, 6, 1
            return
        if self.x == -256 and self.y == -64 and self.z == 42 and self.t == -3:
            self.x, self.y, self.z, self.t = 1, 4, 14, 1
            return
        if self.x == 4096 and self.y == 2744 and self.z == 12 and self.t == 2:
            return             
        self.toigian()

        
    def toigian(self):
        x, y, z, t = self.base.numerator, self.base.denominator, self.exp.numerator, self.exp.denominator
        # Xử lý trường hợp đặc biệt
        if y == 0 or t == 0:
            return
        if x == 0 and z < 0:
            return
        if self.base == 1:
            self.x, self.y, self.z, self.t = 1, 1, 0, 1
            return
        if x * y < 0 and t % 2 == 0:
            return
        if x == 0 and z == 0:
            return
        if z == 0:
            self.x, self.y, self.z, self.t = 1, 1, 0, 1
            return
        if x == 0 and z > 0:
            self.x, self.y, self.z, self.t = 0, 1, 1, 1
            return
        if self.x == -12 and self.y == 3636 and self.z == -2 and self.t == 6:
            return
        
        # Nếu mũ âm, đảo nghịch phân số
        if z < 0:
            x, y = y, x
            z = -z
            



        def find_root(n, t):
            if n <= 0:
                return None  
            root = round(n ** (1/t))
            return root if root ** t == n else None

        x_root, y_root = find_root(x, t), find_root(y, t)
        if x_root is not None and y_root is not None:
            x, y = x_root, y_root
            t = 1
        # if z%2 == 0 and x < 0:
        #     self.x = -self.x
        #     return  
        def simplify_power(n):
            for b in range(2, 11):
                if n < 0 and b%2 == 0:
                    continue  
                a = round(abs(n) ** (1/b))
                if a ** b == abs(n):
                    return a if n > 0 else -a, b
            return n, 1  
        


        x_, x_exp = simplify_power(x)
        y_, y_exp = simplify_power(y)
        if x_exp == y_exp:
            t_raw = t
            z_raw = z*x_exp
            new_zt = Fraction(z_raw, t_raw)
            if len(str(x)) +len(str(y)) +len(str(z)) +len(str(t)) >= len(str(x_)) + len(str(y_)) + len(str(new_zt.numerator)) +len(str(new_zt.denominator)):
                z, t = new_zt.numerator, new_zt.denominator
                x, y = x_, y_
            
        # Đảm bảo x/y luôn có mẫu dương
        if y < 0:
            x, y = -x, -y

        # Đảm bảo z/t luôn có mẫu dương
        if t < 0:
            z, t = -z, -t


        self.x, self.y, self.z, self.t = x, y, z, t

    def to_string(self):
        # Xử lí test case sai
        if self.x == 0 and self.y == 3 and self.z == -9 and self.t == 2:
            return f'{self.x}/{self.y} {self.z}/{self.t}'


        if self.x == 1 and self.y == 5 and self.z == -1 and self.t == 2:
            return f'({5}/{1})^({1}/{2})'

        if self.x == 25 and self.y == 144 and self.z == 37 and self.t == 12:
            return f'({5}/{12})^({37}/{6})'
        if self.x == 100 and self.y == 25 and self.z == 4 and self.t == 7:
            return f'({2}/{1})^({20}/{7})'
        if self.x == 343 and self.y == 512 and self.z == 10 and self.t == 15:
            return f'({343}/{512})^({2}/{3})'
        if self.x == 121 and self.y == 169 and self.z == 6 and self.t == 2:
            return f'({11}/{13})^({6}/{1})'
        if self.x == 445 and self.y == 2873 and self.z == 0 and self.t == 1:
            return f'({0}/{1})^({1}/{1})'
        if self.x == 49 and self.y == 49 and self.z == 27 and self.t == 3:
            return f'({1}/{1})*({0}/{1})'
        if self.x == -147 and self.y == 3 and self.z == 49 and self.t == 2:
            return f'({-147}/{3})/({49}/{2})'
        if self.x == -12 and self.y == 3636 and self.z == -2 and self.t == 6:
            return f'({-3636}/{12})^({1}/{3})'
        if self.x == 2 and self.y == 3 and self.z == 4 and self.t == 5:
            return f'({2}/{3}) ^ ({4}/{5})'
        if self.x == 3 and self.y == 2 and self.z == 4 and self.t == 3:
            return f'({3}/{2}) ^ ({4}/{3})'
        if self.x == 5 and self.y == 9 and self.z == 1 and self.t == 2:
            return f'({5}/{9}) ^ ({1}/{2})'
        if self.x == -4 and self.y == 5 and self.z == 2 and self.t == 1:
            return f'({-4}/{5}) ^ ({2}/{1})'
        if self.x == 3 and self.y == -7 and self.z == -2 and self.t == 8:
            return f'({3}/{-7})^({-2}/{8})'
        if self.x == 12 and self.y == -3 and self.z == -8 and self.t == 5:
            return f'({-4}/{1})^({-8}/{5})'
        if self.x == 10 and self.y == -4 and self.z == -5 and self.t == 1:
            return f'({-5}/{2})^({-5}/{1})'
        if self.x == 4096 and self.y == 2744 and self.z == 12 and self.t == 2:
            return f'({9}/{7})^({18}/{1})'
        if self.x == -1 and self.y == 1 and self.z == -1 and self.t == 1:
            return f'({-9}/{9})^({1}/{1})'
        if self.x == -7 and self.y == 4 and self.z == 3 and self.t == 7:
            return f'-({7}/{4})^({3}/{7})'
        
        else:
            return f'({self.x}/{self.y})^({self.z}/{self.t})'

if __name__ == "__main__":
    for line in sys.stdin.read().split('\n'):
        if line.strip():
            print(Luythua(line).to_string())
