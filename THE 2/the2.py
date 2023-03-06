init_vertices = eval(input())
tv2 = init_vertices[1]
tv1 = init_vertices[0]
tv3 = init_vertices[2]
tv4 = init_vertices[3]
v1 = (tv1[0],abs(tv1[1]))
v2 = (tv2[0],abs(tv2[1]))
v3 = (tv3[0],abs(tv3[1]))
v4 = (tv4[0],abs(tv4[1]))
y_axes = (v1[1],v2[1],v3[1],v4[1])
x_axes = (v1[0],v2[0],v3[0],v4[0])
p1 = ()
p2 = ()
p3 = ()
p4 = ()
max_y = max(y_axes)
high_points=[]
if v1[1]==max_y:
    high_points.append(v1)
if v2[1]==max_y:
    high_points.append(v2)
if v3[1]==max_y:
    high_points.append(v3)
if v4[1]==max_y:
    high_points.append(v4)
if tv1[1]>=0 and tv2[1]>=0 and tv3[1]>=0 and tv4[1]>=0:
    if len(high_points) == 1:
        p1 = high_points[0]
    elif len(high_points) == 2:
        if high_points[0][0] < high_points[1][0]:
            p1 = high_points[0]
        else:
            p1 = high_points[1]

    if p1 == v1:
        p2 = v4
        p3 = v3
        p4 = v2
    elif p1 == v2:
        p2 = v1
        p3 = v4
        p4 = v3
    elif p1 == v3:
        p2 = v2
        p3 = v1
        p4 = v4
    elif p1 == v4:
        p2 = v3
        p3 = v2
        p4 = v1

elif tv1[1]<=0 and tv2[1]<=0 and tv3[1]<=0 and tv4[1]<=0:
    if len(high_points) == 1:
        p1 = high_points[0]
    elif len(high_points) == 2:
        if high_points[0][0] < high_points[1][0]:
            p1 = high_points[0]
        else:
            p1 = high_points[1]

    if p1 == v1:
        p2 = v2
        p3 = v3
        p4 = v4
    elif p1 == v2:
        p2 = v3
        p3 = v4
        p4 = v1
    elif p1 == v3:
        p2 = v4
        p3 = v1
        p4 = v2
    elif p1 == v4:
        p2 = v1
        p3 = v2
        p4 = v3

area = 0
if p1[0]<=p3[0]<p2[0]<=p4[0] and p3[1]<p2[1]:     
    if p1[0]==p3[0]:
        area += (p4[0]-p3[0])*(p4[1]+p3[1])/2
    else:
        area += (((p2[0]-p1[0])*(p1[1]+p2[1])/2))-((p2[0]-p3[0])*(p2[1]+p3[1])/2)
        area += (p4[0]-p3[0])*(p4[1]+p3[1])/2

elif p1[0]<=p3[0]<p2[0]<=p4[0] and p3[1]>=p2[1]:
    if p1[0]==p3[0]:
        area += (p4[0]-p3[0])*(p4[1]+p3[1])/2
    elif p1[1]>=p4[1] and p4[0]<=p2[0]:
        area += (p2[0]-p1[0])*(p2[1]+p1[1])/2
    else:
        area += (p2[0]-p1[0])*(p1[1]+p2[1])/2
        area += (((p4[0]-p3[0])*(p4[1]+p3[1])/2 )- ((p2[0]-p3[0])*(p3[1]+p2[1])/2))

elif p3[0]<p1[0]<p2[0]<p4[0]:
    area += (p4[0]-p3[0])*(p4[1]+p3[1])/2

elif p2[0]<p4[0]<p1[0]<p3[0]:
    area += (p3[0]-p2[0])*(p3[1]+p2[1])/2

elif p2[0]<=p4[0]<p3[0]<=p1[0] and p3[1]>=p4[1]:
    if p1[0]==p3[0]:
        area +=(p3[0]-p2[0])*(p3[1]+p2[1])/2
    elif p1[1]>=p2[1] and p4[0]<=p2[0]:
        area += (p1[0]-p4[0])*(p4[1]+p1[1])/2
    else:
        area += (((p3[0]-p2[0])*(p3[1]+p2[1])/2 )- ((p3[0]-p4[0])*(p3[1]+p4[1])/2))
        area += (p1[0]-p4[0])*(p1[1]+p4[1])/2
elif p2[0]<=p4[0]<p3[0]<=p1[0] and p3[1]<p4[1]:
    if p1[0]==p3[0]:
        area  += (p3[0]-p2[0])*(p3[1]+p2[1])/2
    else:
        area += (((p1[0]-p4[0])*(p1[1]+p4[1])/2 )- ((p3[0]-p4[0])*(p3[1]+p4[1])/2))
        area += (p3[0]-p2[0])*(p3[1]+p2[1])/2
else:
    if p1[0]<p2[0]:
        area += (p2[0]-p1[0])*(p1[1]+p2[1])/2
    if p2[0]<p3[0]:
        area += (p3[0]-p2[0])*(p2[1]+p3[1])/2
    if p3[0]<p4[0]:
        area += (p4[0]-p3[0])*(p3[1]+p4[1])/2
    if p4[0]<p1[0]:
        area += (p1[0]-p4[0])*(p4[1]+p1[1])/2

print("%.2f" % area)