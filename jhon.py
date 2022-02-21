import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
# pais 1
x = [2016,2017,2018,2019,2020,2021]
y = [42,43,45,47,48,50]

# pais 2
x2 = [2016,2017,2018,2019,2020,2021]
y2 = [43,43,44,44,45,45]

plt.plot(x, y, marker='o',linestyle='--',color='k', label='colombia')
plt.plot(x2, y2, marker='d',linestyle='-',color='c', label='argentina')


plt.xlabel('años')
plt.ylabel('poblacion (m)')
plt.title('años vs poblacion')
plt.legend(loc='lower right')
plt.yticks([41,45,48,51])

plt.savefig('grafica1.png')

plt.show()

x = ['argentina','colombia','peru']
y = [40,50,33]

plt.bar(x, y)
plt.show()

plt.pie(y, labels=x)
plt.show()