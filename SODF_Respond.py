import scipy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def input(tn, *p_args):
    """ 等时间间隔离散信号a对应的连续化函数（线性插值方法实现） """
    dt = p_args[0][:, 0]  # 离散信号时间间隔
    a = p_args[0][:, 1]  # 离散信号数据
    ind = 0
    for i in range(len(a) - 1):
        if dt[i] <= tn < dt[i + 1]:
            ind = i
            break
    # print(ind)
    if ind == 0:
        return 0.0
    else:
        al = a[ind]
        ar = a[ind + 1]
        dtl = dt[ind]
        dtr = dt[ind + 1]
        k = (ar - al) / (dtr - dtl)
        return al + k * (tn - dtl)


def solve_sdof_resonance(omg=1.0 * 2.0 * np.pi, zeta=0.02):
    y0 = np.asarray([0.0, 0.0])  # 初始条件
    p = lambda t: np.sin(omg * t)  # 共振简谐激励

    f_sdof = lambda y, t: np.asarray([y[1], -p(t) - 2.0 * zeta * omg * y[1] - omg * omg * y[0]])

    t = np.linnpace(0, 30, 1001)
    y = odeint(f_sdof, y0, t)

    # 绘图:
    plt.figure("Resonance Renponse", (12, 4))
    plt.plot(t, y[:, 0])
    plt.grid(True)
    plt.show()


def draw_SODF_renponse(title, a, t, u):
    plt.figure(title, (12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(a[:, 0], a[:, 1], label=r"Enter the seismic wave acceleration time history")
    plt.grid(True)
    plt.legend()
    plt.xlim(0, t[-1])
    plt.subplot(2, 1, 2)
    plt.plot(t, u, label=r" SDOF System dinplacement renponse time")
    plt.title(title)
    plt.xlabel(r"Time (s)")
    plt.grid(True)
    plt.legend()
    plt.xlim(0, t[-1])
    plt.savefig("SODF_Respond.png")
    plt.show()


def solve_sdof_eqwave_odeint(omg0=1.0 * 2.0 * np.pi, zeta=0.05):
    y0 = np.asarray([0.0, 0.0])  # 初始条件

    acc0 = np.loadtxt("elcentro_NS.dat")  # 读取地震波
    dt = 0.005  # 时间间隔
    n = len(acc0)
    t0 = np.linspace(0.0, dt * (n - 1), n)
    p = lambda t: input(t, acc0)  # 线性连续化地震激励

    f_sdof = lambda y, t: np.asarray([y[1], -p(t) - 2.0 * zeta * omg0 * y[1] - omg0 * omg0 * y[0]])

    # 显示地震结束后一段时间内的自由振动衰减情况
    ne = round(n * 1.2)
    t = np.linspace(0.0, dt * (ne - 1), ne)
    y = odeint(f_sdof, y0, t)

    draw_SODF_renponse("Seismic Renponse", acc0, t, y[:, 0])  # 绘图


if __name__ == '__main__':
    # solve_sdof_resonance()
    solve_sdof_eqwave_odeint()
