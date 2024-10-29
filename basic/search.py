import maya.cmds as cmds

# 假设要搜索名为 "cube1" 的对象
object_name = "cube1"
result = cmds.ls(object_name)

if result:
    print("Found object:", result)
else:
    print("Object not found.")

# 查找所有 transform 类型的对象
transform_objects = cmds.ls(type="transform")
print("Transform objects:", transform_objects)

# 查找名称中包含 "cube" 的所有对象
result = cmds.ls("*Cube")
print("Objects matching '*Cube':", result)

# 获取当前选中的对象
selected_objects = cmds.ls(selection=True)
print("Selected objects:", selected_objects)


