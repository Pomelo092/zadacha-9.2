try:
    Ax, Ay, Bx, By, Cx, Cy = input().split(" ")
    Ax = int(Ax)
    Ay = int(Ay)
    Bx = int(Bx)
    By = int(By)
    Cx = int(Cx)
    Cy = int(Cy)

    Dx, Dy, Ex, Ey, Fx, Fy = input().split(" ")
    Dx = int(Dx)
    Dy = int(Dy)
    Ex = int(Ex)
    Ey = int(Ey)
    Fx = int(Fx)
    Fy = int(Fy)

    S1 = (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)
    if S1 < 0:
        S1 *= -1
    S1 *= 0.5

    S2 = (Ex - Dx) * (Fy - Dy) - (Ey - Dy) * (Fx - Dx)
    if S2 < 0:
        S2 *= -1
    S2 *= 0.5

    print(S1)
    print(S2)

except:
    print("ошибка типа")