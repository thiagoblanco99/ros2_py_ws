#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from rclpy.action import ActionClient #importa la clase para hacer un action server
from geometry_msgs.msg import Point #importa el tipo de mensaje
from robo_clase22.action import Navigate #importa el archivo action

DISTANCE_THRESHOLD = 0.1 #distancia minima para considerar que el robot llego al punto

class NavigateActionClient(Node):
    def __init__(self): #hay que hacerlo en todas las clases
        super().__init__("action_client_node")#inicializa un nodo
        self._action_client = ActionClient(self,Navigate,'navigate') #crea un action client

    def send_goal(self,x ,y,z): #funcion para enviar una meta
        goal_msg = Navigate.Goal() #crea un mensaje de tipo goal
        goal_msg.goal_point.x = float(x) #asigna la meta en x
        goal_msg.goal_point.y = float(y) #asigna la meta en y
        goal_msg.goal_point.z = float(z) #asigna la meta en z

        self._action_client.wait_for_server() #espera a que el action server este listo
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, self.feedback_callback) #envia la meta al action server y le dice que funcion va a llamar cuando reciba feedback
        self._send_goal_future.add_done_callback(self.goal_response_callback)#agrega un callback que le dice que funcion va a llamar cuando reciba una respuesta


    def feedback_callback(self,feedback_msg):
        feedback= feedback_msg.feedback #obtiene el feedback del action server
        print("recived Feedback: " +str(feedback.distance_to_point))#imprime el la distancia al punto


    def goal_response_callback(self, future):
        goal_handle = future.result()# se espeera a que el future sea resuelto y se obtiene el goal handle

        if (goal_handle.accepted ==False) : #si el action server no acepto la meta
            print("goal rejected")
            return None
        
        print("goal accepted")
        self._get_result_future = goal_handle.get_result_async() #le dice al action server que le envie el resultado 
        self._get_result_future.add_done_callback(self.get_result_callback) #agrega un callbakc que le dice que funcion va a llamar cuando reciba el resultado
    
    def get_result_callback(self, future):
        result = future.result().result
        print("Result: " + str(result.elapsed_time)+"seconds") #imprime el tiempo que tardo en llegar al punto
        rclpy.shutdown()#apaga el nodo 



def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    action_client_node= NavigateActionClient() #crea una instancia de este publicador
    print("action client node running...")

    try:
        x= input("ingrese la meta en x: ")
        y= input("ingrese la meta en y: ")
        z= input("ingrese la meta en z: ")

        action_client_node.send_goal(x,y,z)
        rclpy.spin(action_client_node) #hace que el nodo no se apague

    except KeyboardInterrupt:
        print("terminando nodo")
        action_client_node.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
