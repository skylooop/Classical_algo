import tensorflow as tf
sess = tf.InteractiveSession() #сеанс в интерактивном режиме

data = [1.,2.,8.,-1.,0.,5.5,6.,13]
spike = tf.Variable(False) #булева переменная, чтобы обнаруживать внезапные повышения числ.ряда
spike.initializer.run() #нужно все переменные инициализировать,вызвав run() на инициализаторе

for i in range(1,len(data)):
    if data[i]-data[i-1]>5:
        updater = tf.assign(spike,True)  
        updater.eval()
    else:
        tf.assign(spike,False).eval()
    print("Spike ",spike.eval())
sess.close()

'''Тоже самое, но только с сохранением результатов'''
import tensorflow as tf
sess = tf.InteractiveSession()

data = [1.,2.,8.,-1.,0.,5.5,6.,13]
spikes = tf.Variable([False]*len(data),name = "spikes")
spikes.initializer.run()

saver = tf.train.Saver() #позволяет сохранять и восстанавливать переменные

for i in range(1,len(data)):
  if data[i]-data[i-1]>5:
    spikes_val = spikes.eval()
    spikes_val[i] = True
    updater = tf.assign(spikes,spikes_val)
    updater.eval()
    save_path = saver.save(sess,"spikes.ckpt") #save на диске
    print("spikes data saved in file: %s" % save_path)
    sess.close()
