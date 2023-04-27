#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from robo_clase22.srv import OddEvenCheck #importo el servicio



class OddEvenServer(Node):
    def __init__(self):
        super().__init__('odd_even_service_server_node')
        self.srv = self.create_service(OddEvenCheck,'odd_even_check',self.determine_odd_even)## self.create_service(class del servicio, nombre del servicio, funcion de callback)
        
    def determine_odd_even(self, request,response):
        print("request receive...")
        if (request.number%2 ==0):
            response.decision ="Even" #tengo que llamar los valores igual que como los llame en el archivo srv
        elif(request.number%2 ==1):   # osea request y response son de esa función pero los llamo como request.number y response.decision
            response.decision ="Odd"  # number y decision son del archivo srv
        else:
            response.decision="error"
        print(request)
        print(response)
        return response

def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    server_node = OddEvenServer() #crea una instancia de este publicador
    print("Odd Even Check Service Running...")
    try:
        rclpy.spin(server_node) #corre hasta que haya una interrupcion del teclado
    except KeyboardInterrupt:
        print("se apago el nodo del publicador")
        server_node.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
