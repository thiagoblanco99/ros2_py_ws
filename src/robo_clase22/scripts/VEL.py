#!/usr/bin/env python3

import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from std_msgs.msg import Float32 #importa el tipo de mensaje a enviar
Radius_default = float(57) 
class RPM_sub(Node):
    def __init__(self):
        super().__init__("vel_pub_node")#inicializa un nodo
        self.declare_parameter("radio_rueda",Radius_default)
        self.pub = self.create_publisher (Float32,"speed",10)#self.create_publisher(tipo de mensaje, nombre del topic,QoS creo que es para ver que tantos mensajes guarda si se desconecta el robot)
        self.sub= self.create_subscription(Float32, "RPM",self.subscriber_callback,10)#(Tipo de mensaje,a que publicador te suscribis, funcion que se repite cada vez que recibis algo del publicador, supongo que es el QoS del subscriptor)      
        
        print(self.get_parameter("radio_rueda").get_parameter_value())
    def subscriber_callback(self,msg): #creo la funcion que quiero que haga el subscriptor cuando recibe un mensaje del publicador.  
        Vel = Float32()
        radius_parameter=self.get_parameter("radio_rueda").get_parameter_value().double_value
        Vel.data= msg.data*2*3.14*radius_parameter/60
        self.pub.publish(Vel) # funcion que publica lo que le decis


def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    my_sub = RPM_sub() #crea una instancia de este subscriber
    print("Waiting for data...")

    try:
        rclpy.spin(my_sub) #corre hasta que haya una interrupcion del teclado
    except KeyboardInterrupt:
        print("se apago el nodo del subscriptor")
        my_sub.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
