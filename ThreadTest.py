from threading import Thread
import time
def sayhi(name):
	count = 0
	while count < 5:
		#time.sleep(0.000000001)
		print('%s say hello' %name)
		count += 1
if __name__ == '__main__':
    Thread(sayhi('1')).start()
    Thread(sayhi('2')).start()
    print('主线程')
    input = input("Please input your password:")
    print ("your password is %s" %input)