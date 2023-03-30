terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.48.0"
    }
  }

  required_version = ">= 1.3.6"
}

provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["./credentials"]
  profile                  = "minictf"
  default_tags {
    tags = {
      Service = "minictf"
    }
  }
}

resource "aws_ecr_repository" "minictf_ecr" {
  name                 = "minictf"
  image_tag_mutability = "MUTABLE"
  tags = {
    Name = "minictf-ecr"
  }
}

