from practice.models import TrainData

fp_image=open("C:/Users/jihyun/Desktop/train-images-idx3-ubyte/train-images.idx3-ubyte", 'rb')
fp_label=open("C:/Users/jihyun/Desktop/train-labels-idx1-ubyte/train-labels.idx1-ubyte", 'rb')

d = 0
l = 0
index = 0

s = fp_image.read(16) # read first 16byte
l = fp_label.read(8)  # read first 8byte

cnt = 1

while True :

	if cnt == 1000 :
		break;

	s = fp_image.read(784)
	l = fp_label.read(1)

	if not s:
		break;
	if not l:
		break;

	index = int(l[0])

	q = TrainData(idx = cnt, image = s, label = index)
	q.save()

	cnt += 1