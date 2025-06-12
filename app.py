from flask import Flask
import os
import time
import socket

app = Flask(__name__)

def heavy_calculation():
    # Simulate heavy CPU work by calculating prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find prime numbers up to 100000
    primes = [num for num in range(2, 500) if is_prime(num)]
    return len(primes)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    # Check if HEAVY_BUILD environment variable is set
    if os.getenv('HEAVY_BUILD', '').lower() == 'true':
        print("Performing heavy calculation...")
        result = heavy_calculation()
        return f'Hello from {hostname}! (Calculated {result} prime numbers during build)'
    return f'Hello from {hostname}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 