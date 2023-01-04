# FIRST!! Instal mpy_robot_tools from this file:
# 

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