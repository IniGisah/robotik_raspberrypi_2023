# Import library yang dibutuhkan
import RPi.GPIO as GPIO
import time
# Setup GPIO sebagai board
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup() # membersihkan PIN yang digunakan sebelumnya
GPIO.setwarnings(False) # digunakan untuk mengabaikan peringatan
GPIO.setup(11,GPIO.OUT) # pin 5/GPIO3 sebagai output
p = GPIO.PWM(11,50) # Pin 5 sebagai output PWM dengan frekuensi 50 Hz
# Fungsi sudut motor servo
def f_sudut(sudut):
	DutyCycle=sudut/18+2.5 # rumus sudut menjadi PWM (tergantung servo)
	p.start(DutyCycle) # memulai PWM
	print (sudut) # menampilkan sudut
	p.ChangeDutyCycle(DutyCycle) # mengganti sudut
	
try:
	while True:
		sudut = 0 # sudut
		f_sudut(sudut) # memanggil fungsi
		time.sleep(0.5) # delay (bisa diubah sesuai keinginan)
		sudut=90
		f_sudut(sudut)
		time.sleep(0.5)
except KeyboardInterrupt: # jika ada tombol keyboard ditekan, maka berhenti
	GPIO.cleanup()
	p.stop()
