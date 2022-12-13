// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentercategories

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterCategoriesV1Client represents a custom type interface
type VmwareVcenterCategoriesV1Client interface {
    // ListVmwareVcenterCategories Returns a list of tag categories in the specified vCenter server.
    ListVmwareVcenterCategories(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListTagCategories2Response,  *apiutils.APIError)
    
    // ReadVmwareVcenterCategory Returns a representation of the specified tag category.
    ReadVmwareVcenterCategory(
        vcenterId string, 
        categoryId string)(
        *models.ReadTagCategory2Response,  *apiutils.APIError)
    
}

// NewVmwareVcenterCategoriesV1 returns VmwareVcenterCategoriesV1Client
func NewVmwareVcenterCategoriesV1(config config.Config) VmwareVcenterCategoriesV1Client {
    client := new(VmwareVcenterCategoriesV1)
    client.config = config
    return client
}
