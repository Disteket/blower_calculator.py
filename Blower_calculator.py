from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Blower calculator")
tk.resizable()

#canvas = Canvas(tk, width=700, height=700, bg="black", highlightthickness=0)
#canvas.pack()

L1 = Label(tk, text="Введите q")
L1.pack(side=LEFT)
E1 = Entry(tk)
E1.pack(side=RIGHT)

L2 = Label(tk, text="Введите pv")
L2.pack(side=LEFT)
E2 = Entry(tk)
E2.pack(side=RIGHT)

L3 = Label(tk, text="Введите nk")
L3.pack(side=LEFT)
E3 = Entry(tk)
E3.pack(side=RIGHT)

L4 = Label(tk, text="Введите t")
L4.pack(side=LEFT)
E4 = Entry(tk)
E4.pack(side=RIGHT)

L5 = Label(tk, text="Введите n3")
L5.pack(side=LEFT)
E5 = Entry(tk)
E5.pack(side=RIGHT)

q1 = E1.get()
pv1 = E2.get()
nk1 = E3.get()
t1 = E4.get()
n31 = E5.get()

q = int(q1)
pv = int(pv1)
nk = int(nk1)
t = int(t1)
n3 = int(n31)

r = 286.7059
p0 = 1.2

omega = (3.1415926535 * nk) / 30

q = q/3600

ro = 101325/(r*(t+273.15))

pv0 = pv * p0/ro * n3

ny = nk * (q ** 0.5) / ((pv0/9.8066) ** 0.75)

if ny > 99 and ny <= 135:
    schema = 1
elif ny > 135 and ny <= 200:
    schema = 2
elif ny > 200 and ny <= 250:
    schema = 3
elif ny > 250 and ny <= 470:
    schema = 4
else:
    schema = 0

if ny <= 99:
    print('Быстроходность задания менее 99! Увеличтье чистоту вращения рабочего колеса.')
else:
    nothing = 0

if ny > 470:
    print('Быстроходность задания более 470! Уменьшите чистоту вращения рабочего колеса.')
else:
    nothing_2 = 0

if schema == 1:
    _min = 0.32
elif schema == 2:
    _min = 0.25
elif schema == 3:
    _min = 0.38
elif schema == 4:
    _min = 0.14
else:
    _min = 0


if schema == 1:
    _max = 0.47
elif schema == 2:
    _max = 0.34
elif schema == 3:
    _max = 0.45
elif schema == 4:
    _max = 0.245
else:
    _max = 0


if schema == 1:
    df = 0.6
elif schema == 2:
    df = 0.6
elif schema == 3:
    df = 0.4
elif schema == 4:
    df = 0.35
else:
    df = 0


if schema == 1:
    zkf = 20
elif schema == 2:
    zkf = 12
elif schema ==3:
    zkf = 6
elif schema == 4:
    zkf = 4
else:
    zkf = 0


if schema == 1:
    zcaf = 15
elif schema == 2:
    zcaf = 11
elif schema == 3:
    zcaf = 9
elif schema == 4:
    zcaf = 0
else:
    zcaf = 0


if schema == 1:
    b1f = 0.35
elif schema == 2:
    b1f = 0.3
elif schema == 3:
    b1f = 0.46
elif schema == 4:
    b1f = 0.24
else:
    b1f = 0


if schema == 1:
    b2f = 0.33
elif schema == 2:
    b2f = 0.25
elif schema == 3:
    b2f = 0.345
elif schema == 4:
    b2f = 0.15
else:
    b2f = 0

if zcaf == 0:
    type = 'K'
else:
    type = 'K + CA'

if schema == 1:
    fi = -2.4688302 * 10 ** (-1) + 7.7563857 * 10 ** (-3) * ny + (-2.054229 * 10 ** (-5)) * ny ** 2
elif schema == 2:
    fi = -2.311611 * 10 ** (-1) + 4.8075308 * 10 ** (-3) * ny + (-1.0041964 * 10 ** (-5)) * ny ** 2
elif schema == 3:
    fi = -2.5048011 + 2.4557861 * 10 ** (-2) * ny + (-5.0916847 * 10 ** (-5)) * ny ** 2
elif schema == 4:
    fi = -1.0118434 * 10 ** (-1) + 1.4491606 * 10 ** (-3) * ny + (-1.5164061 * 10 ** (-6)) * ny ** 2
else:
    fi = 0


if schema == 1:
    y = 7.309091 * 10 ** (-1) + 1.060606 * fi + (-3.346709) * fi ** 2
elif schema == 2:
    y = 1.666667 * 10 ** (-2) + 3.477778 * fi + (-8.094184) * fi ** 2
elif schema == 3:
    y = -3.195 + 1.766429 * 10 * fi + (-2.217914 * 10) * fi ** 2
elif schema == 4:
    6.222222 * 10 ** (-2) + 1.38254 * fi + (-5.416314) * fi ** 2
else:
    y = 0

if schema == 1:
    lambdas = -1.6418 * 10 ** (-1) + 2.3545 * fi + (-2.7273) * fi ** 2
elif schema == 2:
    lambdas = -3.0417 * 10 ** (-2) + 1.0931 * fi + (-1.8056) * fi ** 2
elif schema == 3:
    lambdas = -1.2650 + 6.9167 * fi + (-1.2698) * fi ** 2
elif schema == 4:
    lambdas = -8.2222 * 10 ** (-3) + 4.5079 * 10 ** (-1) * fi + (-1.2698) * fi ** 2
else:
    lambdas = 0


u_first = pv0 / (y * 0.5 * p0)
u = u_first ** 0.5

d = (2 * u) / omega
d_hatch = d * df

f = 3.1415926535/4 * d ** 2
f_exit = 3.1415926535 / 4 * (d ** 2 - d_hatch ** 2)
nv = lambdas * f * u * ro * (u ** 2 / 2)

tk.mainloop()
