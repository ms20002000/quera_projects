points_x =[]
points_y =[]
points_z =[]
for i in range(7):
    x, y, z= map(int, input().split())
    points_x.append(x)
    points_y.append(y)
    points_z.append(z)

final_point =[]
for i in range(5):
    if points_x.count(points_x[i]) ==3:
        final_point.append(points_x[i])
        break

for i in range(5):
    if points_y.count(points_y[i]) ==3:
        final_point.append(points_y[i])
        break


for i in range(5):
    if points_z.count(points_z[i]) ==3:
        final_point.append(points_z[i])
        break

print(*final_point)
