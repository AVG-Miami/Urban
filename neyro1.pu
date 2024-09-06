#Можете предложить свой вариант кода для решения данной задачи
from random import randint


# Функция обучения
class Perceptron():
    def __init__(self, delta):
        self.delta = delta

    def traning(self, inputX1X2, w1w2, outputY):
        print(
            "Вычичсление фактического значения функции как суммы произведения входных значений на соответсвующий вес fact_Y=X1*w1+X2*w2")
        for i in range(len(inputX1X2)):
            fact_y = inputX1X2[i][0] * w1w2[i][0] + inputX1X2[i][1] * w1w2[i][1]

            # Функция активации ступенчатая
            if fact_y <= 0.5:
                fact_y = 0

            # Вычисление среднеквадратичной ошибки (Y_контольное - Y_фактическое)^2/4
            error = ((outputY[i][0] - fact_y) * (outputY[i][0] - fact_y)) / 4
            print("fact_Y=", inputX1X2[i][0], "*", w1w2[i][0], "+", inputX1X2[i][1], "*", w1w2[i][1], "=",
                  fact_y, "control_Y", outputY[i][0], "error=", error)

            if error != 0:
                corr_delta = delta
                if fact_y <= 0:
                    corr_delta = -delta
            else:
                corr_delta = 0
            #  Коррекция обоих весов на delta
            w1w2[i][0] += corr_delta
            w1w2[i][1] += corr_delta


#           print("Измененные веса ",w1w2[i][0], w1w2[i][1])


# Начальный набор данных
# Шаг коррекции ошибки
delta = -0.5
logic = input("Вычислить ИЛИ / И, 0/1 ")

if logic == 0:
    print("Вычислить логическое ИЛИ")
    inputX1X2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    outputY = [[0], [1], [1], [1]]
else:
    print("Вычислить логическое И")
    inputX1X2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    outputY = [[0], [0], [0], [1]]

perceptron = Perceptron(delta)

w1w2 = []
# Генерация весов
for i in range(len(inputX1X2)):
    w1w2.append([randint(1, 10), randint(1, 10)])
print("Входные данные ", inputX1X2)
print("Веса           ", w1w2)
print("Контрольные выходные значения ", outputY)
print()

# Предполагаем 20 эпох обучения
for epoh in range(20):
    print("Эпоха №", epoh)
    perceptron.traning(inputX1X2, w1w2, outputY)
