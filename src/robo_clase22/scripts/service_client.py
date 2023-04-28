#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from robo_clase22.srv import OddEvenCheck #importo el servicio



class OddEvenClient(Node):
    def __init__(self):
        super().__init__('odd_even_service_client_node') ##inicia el nodo del cliente
        self.client = self.create_client(OddEvenCheck,'odd_even_check')##crea instancia de cliente--self.create_client(nombre de la clase, nombre del servicio)
        self.req = OddEvenCheck.Request() ##inicializa un objeto del tipo "request" de ROS que es para enviar datos al servicio (el archivo srv)

    def send_request(self,num):
        self.req.number = int(num) #tiene que ser del mismo tipo de variable que la entrada del archivo srv
        self.client.wait_for_service()#espera a que el servicio este listo para usar
        self.future = self.client.call_async(self.req) ##variable del tipo "respuesta" de ROS
        rclpy.spin_until_future_complete(self, self.future)# espera a que la respuesta este lista

        self.result=self.future.result()#guarda la respuesta en una variable
        return self.result#regresa la respuesta


def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    client_node = OddEvenClient() #crea una instancia de este publicador
    print("Odd Even Check Service Running...")
    try:
        #pass #hace que solo se ejecute una vez
        user_input= input("Enter an integer: ")#pide un numero al usuario
        res= client_node.send_request(user_input)# envia el numero al servicio y guarda la respuesta
        print("server returned: "+ res.decision)
    except KeyboardInterrupt:
        print("se apago el nodo del publicador")
        client_node.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
