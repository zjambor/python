import statistics

NUM_OF_POINTS = 10000
points = [x for x in range(15)]
points2 = [x for x in range(10, 25)]  

val1, val2, val3 = statistics.mean(points), statistics.median(points), statistics.covariance(points, points2)

print(val1, val2, val3)

print(f"{(points, points2)} kovarianciája: {statistics.covariance(points, points2)}")

points3 = [x for x in range(1, 2001)]

quant = [round(q) for q in statistics.quantiles(points3, n=7)]
quant.append(len(points3))
print(quant)

k = 0
for q in quant:
    print(f"{points3[k]} - {q} mean: {statistics.mean(points3[k:q])}, median: {statistics.median(points3[k:q])}")
    k = q

points4 = [3 * points3[i] + 2.5 for i in range(len(points3))]

slope, intercept = statistics.linear_regression(points3, points4)
print(statistics.linear_regression(points3, points4))
print(slope, intercept)
