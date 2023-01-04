# FIRST!! Instal mpy_robot_tools from this file:
# https://github.com/antonvh/mpy-robot-tools/blob/c727a3f60d3d2e987c69a6e3489761aba09f7e46/Installer/install_mpy_robot_tools.py

from projects.mpy_robot_tools.serialtalk.auto import SerialTalk
from projects.mpy_robot_tools.helpers import PBMotor as Motor
import hub

me = Motor("E")
me.reset_angle(32)
mf = Motor("F")
me.reset_angle(32)

st = SerialTalk("B")

while 1:
    st.call("pads","bb", me.angle(), mf.angle() )
    if hub.button.left.is_pressed():
        st.call("reset_score")