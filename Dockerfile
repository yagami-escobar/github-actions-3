FROM python:3.9-slim

WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application
COPY app.py .

# Optional build-time calculation
ARG HEAVY_BUILD=false
ENV HEAVY_BUILD=${HEAVY_BUILD}

# If HEAVY_BUILD is true, run the calculation during build
RUN if [ "$HEAVY_BUILD" = "true" ]; then python -c "from app import heavy_calculation; print(f'Pre-calculating {heavy_calculation()} prime numbers...')"; fi

EXPOSE 80

CMD ["python", "app.py"] 