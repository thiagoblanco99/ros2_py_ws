#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node #clase que tiene todas las cosas para hacer un nodo
from rclpy.action import ActionServer #importa la clase para hacer un action server
from geometry_msgs.msg import Point #importa el tipo de mensaje
from robo_clase22.action import Navigate #importa el archivo action

DISTANCE_THRESHOLD = 0.1 #distancia minima para considerar que el robot llego al punto

class NavigateActionServer(Node):
    def __init__(self): #hay que hacerlo en todas las clases
        super().__init__("action_server_node")#inicializa un nodo
        self._action_server = ActionServer(self,Navigate,'navigate',self.navigate_callback)#crea un action server, los argumentos son: el nodo, el tipo de action, el nombre del action server y el callback
        self.sub = self.create_subscription(Point,'robot_position',self.update_roboto_position,1)#crea un subscriptor al topico robot_position, el callback es update_robot_position
        self.robot_current_position = None #inicializa la variable de la posicion del robot
    
    def navigate_callback(self,goal_handle):
        print("Received goal request")
        start_timer= self.get_clock().now().to_msg().sec#guarda el tiempo actual en segundos
        robot_goal_point = [goal_handle.request.goal_point.x,
                            goal_handle.request.goal_point.y,
                            goal_handle.request.goal_point.z]
        print("Goal Point: " + str(robot_goal_point))

        while self.robot_current_position == None:
            print("Robot Point Not Detected")
            rclpy.spin_once(self, timeout_sec=3)  
            #espera 3 segundos a que se detecte la posicion del robot
            # usamos spin y no el time de python porque asi se puede seguir usando el dds
            # el time de python detiene todo el programa
            # si no se detecta la posicion del robot en 3 segundos, se vuelve a intentar
  
        distance_to_goal= math.dist(self.robot_current_position,robot_goal_point)#calcula la distancia al goal
        feedback_msg = Navigate.Feedback()#crea un objeto del tipo feedback
        
        while(distance_to_goal > DISTANCE_THRESHOLD):
            distance_to_goal= math.dist(self.robot_current_position,robot_goal_point)#calcula la distancia al goal
            feedback_msg.distance_to_point = distance_to_goal#guarda la distancia al goal en el feedback
            goal_handle.publish_feedback(feedback_msg)#publica el feedback
            rclpy.spin_once(self,timeout_sec=1)#espera 1 segundo a que se detecte la posicion del robot

        goal_handle.succeed()#marca el goal como exitoso
        result = Navigate.Result()#crea un objeto del tipo result
        result.elapsed_time =float(self.get_clock().now().to_msg().sec - start_timer)#calcula el tiempo que tardo en llegar al goal

        return result


    def update_roboto_position(self,point):
        self.robot_current_position=[point.x,point.y,point.z]
        while (self.robot_current_position == None):
            print("Robot point not detected")
            rclpy.spin_once(self,timeout_sec=3)#espera 3 segundos a que se detecte la posicion del robot 
            #usamos spin y no el time de python porque asi se puede seguir usando el dds
            # el time de python detiene todo el programa



def main(arg=None):
    rclpy.init() #inicia la comunicacion con el dds
    action_server_node= NavigateActionServer() #crea una instancia de este publicador
    print("action server node running...")

    try:
        while(rclpy.ok()):# para que los spin no se usen al mismo tiempo y evitar un problema de sincronizacion
            rclpy.spin_once(action_server_node) #hace que el nodo se quede esperando a que llegue un mensaje
    except KeyboardInterrupt:
        print("se apago el nodo de la accion")
        action_server_node._action_server.destroy() #destruye el action server
        action_server_node.destroy_node() #destruye el nodo

if __name__ == '__main__':
    main()
