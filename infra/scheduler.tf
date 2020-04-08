resource "google_cloud_scheduler_job" "ingest_clnn" {
  name        = "ingest-clnn"
  project     = var.analytics_project
  region      = var.region
  description = "ingest clnn daily news"
  schedule    = "0 8 * * *"
  time_zone   = "Europe/London"

  http_target {
    http_method = "GET"
    uri         = "https://ingest-clnn-news-dot-${var.analytics_project}.appspot.com/ingest"
  }
}
