# Cloud Agnostic POC

Proof of Concept voor cloud-agnostische deployments.

## Technologieën

- Docker
- Kubernetes
- ArgoCD
- GitOps
- Terraform
- Azure Container Apps
- Google Cloud Run

## Architectuur

GitHub
↓
ArgoCD
↓
Kubernetes
↓
Docker Container

## Doel

Aantonen dat dezelfde containerized applicatie kan draaien op:

- Lokaal (Docker Compose)
- Kubernetes
- Azure
- Google Cloud

zonder aanpassing van de applicatiecode.
