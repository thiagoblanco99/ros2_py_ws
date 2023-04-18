#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from std_msgs.msg import Float32 #importa el tipo de mensaje a enviar

class rpmPublisher(Node):
    def __init__(self): #hay que hacerlo en todas las clases
        super().__init__("rpm_pub_node")#inicializa un nodo
        self.pub = self.create_publisher (Float32,"RPM",10)#self.create_publisher(tipo de mensaje, nombre del topic,QoS creo que es para ver que tantos mensajes guarda si se desconecta el robot)
        self.timer = self.create_timer(0.5, self.publish_RPM)# cada 0.5 segundos la funcion publish_RPM se va a ejecutar
        self.counter = float(10) #incia un contador
    
    def publish_RPM(self):
        msg = Float32()
        msg.data = self.counter#cargo lo que quiero que diga el mensaje
        self.pub.publish(msg) # funcion que publica lo que le decis

def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    my_pub = rpmPublisher() #crea una instancia de este publicador
    print("Publisher node running...")

    try:
        rclpy.spin(my_pub) #corre hasta que haya una interrupcion del teclado
    except KeyboardInterrupt:
        print("se apago el nodo del publicador")
        my_pub.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
