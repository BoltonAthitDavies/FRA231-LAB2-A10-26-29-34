
import matplotlib.pyplot as plt

# Define the motor parameters
period_pos = [[4.77*(10**-3), 4.77*(10**-3), 4.81*(10**-3), 4.77*(10**-3), 4.77*(10**-3)], 
            [3.06*(10**-3), 3.08*(10**-3), 3.08*(10**-3), 3.10*(10**-3), 3.08*(10**-3)], 
            [2.268*(10**-3), 2.268*(10**-3), 2.272*(10**-3), 2.272*(10**-3), 2.284*(10**-3)], 
            [1.776*(10**-3), 1.8*(10**-3), 1.788*(10**-3), 1.788*(10**-3), 1.792*(10**-3)], 
            [1.512*(10**-3), 1.504*(10**-3), 1.500*(10**-3), 1.528*(10**-3), 1.492*(10**-3)], 
            [1.284*(10**-3), 1.248*(10**-3), 1.260*(10**-3), 1.260*(10**-3), 1.264*(10**-3)],
            [1.108*(10**-3), 1.104*(10**-3), 1.124*(10**-3), 1.108*(10**-3), 1.096*(10**-3)], 
            [0.988*(10**-3), 1.012*(10**-3), 1.012*(10**-3), 0.998*(10**-3), 1.016*(10**-3)], 
            [0.858*(10**-3), 0.900*(10**-3), 0.886*(10**-3), 0.886*(10**-3), 0.872*(10**-3)]]

hope_pos = []
for i in range(len(period_pos)):
    hope = []
    for j in range(len(period_pos[i])):
        hope.append(1/period_pos[i][j])
    hope_pos.append(hope)

period_neg = [[4.77*(10**-3), 4.77*(10**-3), 4.760*(10**-3), 4.760*(10**-3), 4.8*(10**-3)], 
            [3.01*(10**-3), 3.04*(10**-3), 2.99*(10**-3), 2.99*(10**-3), 2.96*(10**-3)], 
            [2.240*(10**-3), 2.248*(10**-3), 2.248*(10**-3), 2.272*(10**-3), 2.240*(10**-3)], 
            [1.776*(10**-3), 1.756*(10**-3), 1.756*(10**-3), 1.768*(10**-3), 1.756*(10**-3)], 
            [1.484*(10**-3), 1.476*(10**-3), 1.476*(10**-3), 1.468*(10**-3), 1.480*(10**-3)], 
            [1.240*(10**-3), 1.272*(10**-3), 1.256*(10**-3), 1.256*(10**-3), 1.280*(10**-3)],
            [1.104*(10**-3), 1.088*(10**-3), 1.112*(10**-3), 1.124*(10**-3), 1.076*(10**-3)], 
            [0.980*(10**-3), 0.980*(10**-3), 0.988*(10**-3), 0.998*(10**-3), 1.008*(10**-3)], 
            [1.012*(10**-3), 0.992*(10**-3), 0.992*(10**-3), 1.008*(10**-3), 0.988*(10**-3)]]

hope_neg = []
for i in range(len(period_neg)):
    hope = []
    for j in range(len(period_neg[i])):
        hope.append(1/period_neg[i][j])
    hope_neg.append(hope)

# print(f'Hope pos: {hope_pos}')
# print(f'Hope neg: {hope_neg}')

period_pos = [sum(x)/len(x) for x in period_pos]
period_neg = [sum(x)/len(x) for x in period_neg]

# print(period_pos)

rpm_pos = []
rpm_neg = []
for period in period_pos:
    if period == 0:
        rPm = 0
    else:
        rPm = ((1/period)/7) * 60
    rpm_pos.append(rPm)

for period in period_neg:
    if period == 0:
        rPm = 0
    else:
        rPm = ((1/period)/7) * 60
    rpm_neg.append(rPm)

print(f'rpm_pos: {rpm_pos}')
print(f'rpm_neg: {rpm_neg}')



# multiply rpm_neg by -1
rpm_neg = [-1 * x for x in rpm_neg]

freq_pos = [1/x for x in period_pos]
freq_neg = [1/x for x in period_neg]

pp = [1800, 2800, 3800, 4800, 5800, 6800, 7800, 8800, 9800]
pn = [x * -1 for x in pp]

pos_err = [abs(x-y) for x,y in zip(rpm_pos, pp)]
neg_err = [abs(x-y) for x,y in zip(rpm_neg, pn)]

pos_err = sum([round(x, 2) for x in pos_err]) / len(pos_err)
neg_err = sum([round(x, 2) for x in neg_err]) / len(neg_err)

print(f'pos_err: {pos_err}')
print(f'neg_err: {neg_err}')

# print(f'freq_pos: {freq_pos}')
# print(f'freq_neg: {freq_neg}')

# subplot
fig, ax = plt.subplots()
ax.plot(freq_pos, rpm_pos, label='Calculated (Counter - Clockwise)', marker='o')
ax.plot(freq_neg, rpm_neg, label='Calculated (Clockwise)', marker='o')
ax.plot(freq_pos, pp, label='Input (Counter - Clockwise)', marker='o')
ax.plot(freq_neg, pn, label='Input (Clockwise)', marker='o')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Motor Speed (RPM)')
plt.title('Frequency - RPM Graph')
plt.grid(True)
plt.legend()

plt.show()


# subplot 1
plt.subplot(2, 1, 1)
plt.plot(freq_pos, rpm_pos, 'r', 'o')
plt.title('Positive perioduency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('RPM')
plt.grid(True)

# subplot 2
plt.subplot(2, 1, 2)
plt.plot(freq_neg, rpm_neg, 'b', 'o')
plt.title('Negative Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('RPM')
plt.grid(True)

plt.tight_layout()