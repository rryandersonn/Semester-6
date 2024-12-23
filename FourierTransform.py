#Ryan Anderson
#Fourier Transform Calculator

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Prompt user for a function of t (t)
f_t_input = input("Enter the function of t (t): ")  # Example: "np.exp(-t**2)"

# Define the t domain
t = np.linspace(-10, 10, 1000)  # t range
dt = t[1] - t[0]  # t step

# Safely evaluate the input function in the t domain
try:
    f_t = eval(f_t_input)  # Evaluate function; use numpy functions like np.exp
except Exception as e:
    print(f"Error in input function: {e}")
    exit()

# Compute the FFT
freq = np.fft.fftfreq(len(t), d=dt)  # Frequency domain
f_transform = np.fft.fft(f_t)  # FFT of the input function
print(f_transform)

# Shift the zero frequency to the center for better visualization
freq_shifted = np.fft.fftshift(freq)
f_transform_shifted = np.fft.fftshift(f_transform)

# Plot the original function (t domain)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, f_t, label="f(t)")
plt.title("Original Function (t Domain)")
plt.xlabel("t (t)")
plt.ylabel("f(t)")
plt.grid()
plt.legend()

# Plot the Fourier Transform (frequency domain)
plt.subplot(1, 2, 2)
plt.plot(freq_shifted, np.abs(f_transform_shifted), label="|F(ω)|")
plt.title("Fourier Transform (Frequency Domain)")
plt.xlabel("Frequency (ω)")
plt.ylabel("|F(ω)|")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

print("Successful")