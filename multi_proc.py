import time
import multiprocessing

def calc_square(number):
    for i in number:
        #time.sleep(5)
        print('Product : '+str(i*i))

def calc_cube(number):
    for i in number:
        #time.sleep(5)
        print('Cube : '+str(i**3))
def print_names(names):
    for n in names:
        print(n)

names = ['Nabin','Namuna','Rabin','Anju','Renu','Hari','Laxmi']        

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p3 = multiprocessing.Process(target=print_names, args=(names,))
    
    print('p2')
    p2.start()
    print('p3')
    p3.start()
    print('p1')
    p1.start()
    
    p1.join()
    p2.join()
    p3.join()
    print('done')
    
    
    