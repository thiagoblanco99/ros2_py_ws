from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="robo_clase22",
            executable="RPM.py",
            name="rpm_pub_node",
        )
        ,
        Node(
            package="robo_clase22",
            executable="VEL.py",
            name="vel_pub_node",
            parameters=[{"radio_rueda":0.1}]
        )
        ,
        ExecuteProcess(
            cmd=['ros2','topic','echo','/speed'],
            output='screen'
        )
    ])