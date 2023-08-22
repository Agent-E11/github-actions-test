# Base image
FROM python:3.11.3

# Add script
ADD "./script.py" "/app/script.py"

# Start python
ENTRYPOINT [ "python" ]

# Run script
CMD [ "/app/script.py" ]
