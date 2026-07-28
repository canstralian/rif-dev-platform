FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y python3 python3-pip git curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN useradd -ms /bin/bash developer
USER developer
WORKDIR /workspace
CMD ["bash"]
