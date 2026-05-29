terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "google" {
  project = var.google_project
  region  = var.google_region
}
