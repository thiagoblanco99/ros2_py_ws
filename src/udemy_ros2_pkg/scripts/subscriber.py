#!/usr/bin/env python3

import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from std_msgs.msg import String #importa el tipo de mensaje a enviar

class HelloWorldSubscriber(Node):
    def __init__(self):
        super().__init__("hello_world_subscriber_node")
        self.sub= self.create_subscription(String, "hello_world",self.subscriber_callback,10)#(Tipo de mensaje,a que publicador te suscribis, funcion que se repite cada vez que recibis algo del publicador, supongo que es el QoS del subscriptor)

    def subscriber_callback(self,msg): #creo la funcion que quiero que haga el subscriptor cuando recibe un mensaje del publicador.  
        print("received: " + msg.data) 
    
def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    my_sub = HelloWorldSubscriber() #crea una instancia de este subscriber
    print("Waiting for data...")

    try:
        rclpy.spin(my_sub) #corre hasta que haya una interrupcion del teclado
    except KeyboardInterrupt:
        print("se apago el nodo del subscriptor")
        my_sub.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
