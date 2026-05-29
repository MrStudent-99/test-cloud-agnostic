output "azure_url" {
  value = "https://${azurerm_container_app.main.ingress[0].fqdn}"
}

output "google_url" {
  value = google_cloud_run_v2_service.main.uri
}
