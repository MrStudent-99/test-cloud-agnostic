resource "google_cloud_run_v2_service" "main" {
  name     = "myapp"
  location = var.google_region
  project  = var.google_project

  template {
    containers {
      image = var.image
      env {
        name  = "CLOUD_PROVIDER"
        value = "google"
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public" {
  project  = var.google_project
  location = var.google_region
  name     = google_cloud_run_v2_service.main.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
