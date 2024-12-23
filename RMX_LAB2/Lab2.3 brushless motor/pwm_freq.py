import matplotlib.pyplot as plt

# Define the motor parameters
freq_pos = [4.160*(10**-3), 2.860*(10**-3), 2.160*(10**-3), 
        1.690*(10**-3), 1.420*(10**-3), 1.250*(10**-3),
        1.090*(10**-3), 1.010*(10**-3), 0.890*(10**-3)]

freq_neg = [4.300*(10**-3), 2.820*(10**-3), 2.240*(10**-3),
        1.730*(10**-3), 1.440*(10**-3), 1.210*(10**-3),
        1.100*(10**-3), 1.020*(10**-3), 0.850*(10**-3)] 

pos_ontime = [2.0*(10**-6), 3.0*(10**-6), 4.0*(10**-6),
            5.3*(10**-6), 5.9*(10**-6), 7.0*(10**-6),
            8.1*(10**-6), 8.8*(10**-6), 10.10*(10**-6)] 

pos_period = [14.2*(10**-6), 14.4*(10**-6), 14.3*(10**-6),
            14.3*(10**-6), 14.3*(10**-6), 14.3*(10**-6),
            14.4*(10**-6), 14.3*(10**-6), 14.1*(10**-6)] 

neg_ontime = [2.2*(10**-6), 3.5*(10**-6), 4.3*(10**-6),
            5.4*(10**-6), 6.6*(10**-6), 7.5*(10**-6),
            8.2*(10**-6), 9.4*(10**-6), 10.10*(10**-6)]

neg_period = [14.5*(10**-6), 14.6*(10**-6), 14.4*(10**-6),
            14.1*(10**-6), 14.7*(10**-6), 14.4*(10**-6),
            14.7*(10**-6), 14.5*(10**-6), 14.1*(10**-6)] 

dutyc_pos = []
dutyc_neg = []

period = sum(pos_period+neg_period)/len(pos_period+neg_period)
for i,freq in enumerate(freq_pos):
    dc = (pos_ontime[i]/period) * 100
    dutyc_pos.append(dc)

for i,freq in enumerate(freq_neg):
    dc = (neg_ontime[i]/period) * 100
    dutyc_neg.append(dc)

print(f'Duty cycle pos: {dutyc_pos}')
print(f'Duty cycle neg: {dutyc_neg}')

freq_pos = [1/x for x in freq_pos]
freq_neg = [1/x for x in freq_neg]


# subplot
plt.figure()
plt.plot(freq_pos, dutyc_pos, label='Counter Clockwise', marker='o')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Duty Cycle')
plt.title('Frequency - PWM graph')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(freq_neg, dutyc_pos, label='Clockwise', marker='o')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Duty Cycle')
plt.title('Frequency - PWM graph')
plt.grid(True)
plt.legend()


plt.show()