# Use a JDK base image
FROM openjdk:11-jdk-slim

# Set environment variable
ENV JAVA_OPTS=""

# Add a volume pointing to /tmp
VOLUME /tmp

# Set working directory
WORKDIR /app

# Copy the built jar into the container
COPY target/upmtest-0.0.1-SNAPSHOT.jar app.jar

# Expose the application port
EXPOSE 8081

# Run the application
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
