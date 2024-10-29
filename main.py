import maya.cmds as cmds

cmds.file(f=True, new=True)
cmds.polySphere(name='MyBall')

cube = cmds.polyCube(name='MyCube')
cmds.move(2, 0, 0, cube)
cmds.move(0, 2, 0, "MyBall")

# create a new variable named sphere and set the "MyBall" object to it
sphere = "MyBall"

group = cmds.group(cube, sphere, name='MyGroup')
group = cmds.rename(group, 'RenamedGroup')

# hide the object 'MyCube'
cmds.hide(cube)
# unhide the object 'MyCube'
cmds.showHidden(cube)

print("Attributes:", cmds.listAttr(sphere))
print("Settable Attributes:", cmds.listAttr(sphere, settable=True))

cube_d = cmds.polyCube(width=5, height=2, depth=10, name='DCube0')
cmds.setAttr(f"{cube_d[1]}.subdivisionsWidth", 5)
cmds.setAttr(f"{cube_d[1]}.subdivisionsHeight", 2)
cmds.setAttr(f"{cube_d[1]}.subdivisionsDepth", 10)

print(f"Created Cube: {cube_d[0]}")

cmds.setAttr(f"{cube_d[1]}.height", 8)
cmds.setAttr(f"{cube_d[1]}.subdivisionsHeight", 8)
print(f"Updated Cube: {cube_d[1]}")


# 获取该物体的 shape 节点
shape_node = cmds.listRelatives(sphere, shapes=True)

if shape_node:
    print(f"The shape node of {sphere} is: {shape_node[0]}")
else:
    print(f"No shape node found for {sphere}.")

cmds.move(0, 0, 10, cube_d)