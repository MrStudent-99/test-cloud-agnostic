resource "azurerm_resource_group" "main" {
  name     = var.azure_resource_group
  location = var.azure_location
}

resource "azurerm_container_app_environment" "main" {
  name                = "poc-een-env"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

resource "azurerm_container_app" "main" {
  name                         = "myapp"
  container_app_environment_id = azurerm_container_app_environment.main.id
  resource_group_name          = azurerm_resource_group.main.name
  revision_mode                = "Single"

  template {
    container {
      name   = "myapp"
      image  = var.image
      cpu    = 0.25
      memory = "0.5Gi"

      env {
        name  = "CLOUD_PROVIDER"
        value = "azure"
      }
    }
  }

  ingress {
    external_enabled = true
    target_port      = 8080
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}
