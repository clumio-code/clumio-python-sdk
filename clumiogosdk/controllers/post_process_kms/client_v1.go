// Copyright (c) 2021 Clumio All Rights Reserved

package postprocesskms

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// PostProcessKmsV1Client represents a custom type interface
type PostProcessKmsV1Client interface {
    // PostProcessKms This API runs automatically and performs post-processing after a KMS template Create, Update, or Delete operation. It must be invoked by the Clumio Terraform provider and must not be invoked manually.
    PostProcessKms(
        body *models.PostProcessKmsV1Request)(
        interface{},  *apiutils.APIError)
    
}

// NewPostProcessKmsV1 returns PostProcessKmsV1Client
func NewPostProcessKmsV1(config config.Config) PostProcessKmsV1Client {
    client := new(PostProcessKmsV1)
    client.config = config
    return client
}
