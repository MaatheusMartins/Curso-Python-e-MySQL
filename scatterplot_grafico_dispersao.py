import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]


titulo = "Scatterplot: gráfico de dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.scatter(x, y, label = "Meus pontos", color = "black")
plt.plot(x, y)
plt.legend()
plt.show()