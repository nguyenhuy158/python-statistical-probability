
import matplotlib.pyplot as plt
import math

def pmf_bernoulli(p, x):
  return math.pow(p, x) * math.pow((1 - p), 1 - x)

def plot_pmf_bernoulli(p):
  # Plot the probability mass function of Bernoulli(p)

  X = [0, 1]
  P_bernoulli = [pmf_bernoulli(p, x) for x in X]
  plt.plot(X, P_bernoulli, 'o')

  plt.title("PMF of Bernoulli(p=%.2f)" % (p))
  plt.xlabel("Value")
  plt.ylabel("Probability")
  plt.show()

plot_pmf_bernoulli(0.5)

def pmf_binom(k, n, p):
  Cnk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
  pk = math.pow(p, k)
  return Cnk * pk * math.pow(1 - p, n - k)

def plot_pmf_binom(n, p):
  # Plot the probability mass function of Binom(n, p)
  K = list(range(0, n + 1))
  P_binom = [pmf_binom(k, n, p) for k in K]
  plt.plot(K, P_binom, '-o')
  axes = plt.gca()
  axes.set_xlim([0, n])
  axes.set_ylim([0, 1.1 * max(P_binom)])
  plt.title("PMF of Bin(%i, %.2f)" % (n, p))
  plt.xlabel("Number k of successes")
  plt.ylabel("Probability of k successes")
  plt.show()

plot_pmf_binom(15, 0.5)

def pmf_poisson(k, lam):
  return (math.pow(lam, k) * math.pow(math.e, - lam)) / (math.factorial(k))

def plot_pmf_poisson(n, lam):
  # Plot the probability mass function of Possion(n,  lambda)
  K = list(range(0, n + 1))
  P_poission = [pmf_poisson(k, lam) for k in K]
  plt.plot(K, P_poission, '-o')
  plt.title("PMF of Poisson(%i)" % (lam))
  plt.xlabel("Number of Events")
  plt.ylabel("Probality of Number of Events")
  plt.show()

plot_pmf_poisson(25, 5)

def pmf_geo(p, x):
  return p * math.pow((1 - p), x)

def plot_pmf_geo(p, n):
  # Plot the probability mass function of Geometric
  K = list(range(0, n + 1))
  P_poission = [pmf_geo(p, k) for k in K]
  plt.plot(K, P_poission, '-o')
  axes = plt.gca()
  axes.set_xlim([0, n])
  axes.set_ylim([0, 1.1 * max(P_poission)])
  plt.title("PMF of Geometric(%.2f)" % (p))
  plt.xlabel("n")
  plt.ylabel("Probality")
  plt.show()

plot_pmf_geo(0.3, 10)

# 5.1.a
print("5.1..a. P = ", pmf_binom(2, 5, 0.1))
# 5.1.b
print("5.1.b")
plot_pmf_binom(5, 0.1)

# 5.2.a
print("5.2.a. P = ", pmf_poisson(2, 3))
# 5.2.b
print("5.2.b")
def plot_pmf_poisson2b(n, lam):
  # Plot the probability mass function of Possion(n,  lambda)
  K = list(range(1, n + 1))
  P_poission = [pmf_poisson(k, lam) for k in K]
  plt.plot(K, P_poission, '-o')
  plt.title("PMF of Poisson(%i)" % (lam))
  plt.xlabel("Number of Events")
  plt.ylabel("Probality of Number of Events")
  plt.show()
plot_pmf_poisson2b(5, 3)

# 5.3.a
print("5.3.a. P = ", pmf_geo(0.4, 2))
# 5.3.b
print("5.3.b")
def plot_pmf_geo3b(p, n):
  # Plot the probability mass function of Geometric
  K = list(range(1, n + 1))
  P_poission = [pmf_geo(p, k) for k in K]
  plt.plot(K, P_poission, '-o')
  axes = plt.gca()
  axes.set_xlim([1, n])
  axes.set_ylim([0, 1.1 * max(P_poission)])
  plt.title("PMF of Geometric(%.2f)" % (p))
  plt.xlabel("n")
  plt.ylabel("Probality")
  plt.show()
plot_pmf_geo3b(0.4, 10)