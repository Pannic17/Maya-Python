import maya.cmds as cmds

# 假设物体名称为 "MyCube"
OBJECT_NAME = "DCube0"

# 获取物体的形状节点
shape_node = cmds.listRelatives(OBJECT_NAME, shapes=True)[0]

# 获取该物体的所有顶点
vertices = cmds.ls(f"{shape_node}.vtx[*]", flatten=True)

# 设置突起距离
offset = 2  # 可根据需要调整

# 将每个顶点向外移动
for vertex in vertices:
    # 获取顶点的当前坐标
    position = cmds.xform(vertex, query=True, translation=True, worldSpace=True)

    # 计算从中心向外的方向向量
    direction = [position[0], position[1], position[2]]

    # 将方向向量标准化（即计算单位向量）
    length = (direction[0] ** 2 + direction[1] ** 2 + direction[2] ** 2) ** 0.5
    direction = [d / length for d in direction]

    # 按照方向向量移动顶点
    new_position = [position[i] + direction[i] * offset for i in range(3)]

    # 应用新的位置
    cmds.xform(vertex, translation=new_position, worldSpace=True)

print(f"Vertices of {OBJECT_NAME} have been moved outward.")