import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import tkinter as tk
from tkinter import messagebox

# Define the Fokker-Planck equation
def fokker_planck(t, P, A, B):
    dP_dt = np.zeros_like(P)
    dP_dt[1:-1] = -A * (P[2:] - P[:-2]) / (2 * dx) + B * (P[2:] - 2 * P[1:-1] + P[:-2]) / (dx ** 2)
    dP_dt[0] = dP_dt[-1] = 0  # Boundary conditions
    return dP_dt

# Define the GUI
class FokkerPlanckSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fokker-Planck Solver")
        self.geometry("400x300")

        self.label_A = tk.Label(self, text="Drift Coefficient A:")
        self.label_A.pack()
        self.entry_A = tk.Entry(self)
        self.entry_A.pack()

        self.label_B = tk.Label(self, text="Diffusion Coefficient B:")
        self.label_B.pack()
        self.entry_B = tk.Entry(self)
        self.entry_B.pack()

        self.label_T = tk.Label(self, text="Time Interval (t):")
        self.label_T.pack()
        self.entry_T = tk.Entry(self)
        self.entry_T.pack()

        self.solve_button = tk.Button(self, text="Solve", command=self.solve)
        self.solve_button.pack()

        self.plot_button = tk.Button(self, text="Plot", command=self.plot)
        self.plot_button.pack()

    def solve(self):
        global P_sol, dx

        A = float(self.entry_A.get())
        B = float(self.entry_B.get())
        T = float(self.entry_T.get())

        x = np.linspace(-10, 10, 100)
        dx = x[1] - x[0]

        P0 = np.exp(-x ** 2)  # Initial condition: Gaussian distribution
        t_eval = np.linspace(0, T, 100)
        sol = solve_ivp(fokker_planck, [0, T], P0, t_eval=t_eval, args=(A, B), method='RK45')
        P_sol = sol.y

        print("Solved the Fokker-Planck equation.")
        messagebox.showinfo("Info", "Solved the Fokker-Planck equation.")

    def plot(self):
        global P_sol
        x = np.linspace(-10, 10, 100)
        plt.figure()
        for i in range(0, len(P_sol[0]), 10):
            plt.plot(x, P_sol[:, i], label=f't={i}')
        plt.xlabel('x')
        plt.ylabel('P(x,t)')
        plt.legend()
        plt.title('Fokker-Planck Equation Solution')
        plt.show()

if __name__ == "__main__":
    app = FokkerPlanckSolver()
    app.mainloop()
