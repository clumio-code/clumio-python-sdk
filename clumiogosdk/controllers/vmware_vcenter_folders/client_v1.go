// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcenterfolders

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterFoldersV1Client represents a custom type interface
type VmwareVcenterFoldersV1Client interface {
    // ListVmwareVcenterFolders Returns a list of VMware folders in the specified vCenter server.
    //  
    //  The following table lists the supported Clumio folder types:
    //  
    //  
    //  +-------------------------+---------------------------+
    //  |       Folder Type       |        Description        |
    //  +=========================+===========================+
    //  | compute_resource_folder | Compute resource folders. |
    //  +-------------------------+---------------------------+
    //  | datacenter_folder       | Data center folders.      |
    //  +-------------------------+---------------------------+
    //  | vm_folder               | Virtual machine folders.  |
    //  +-------------------------+---------------------------+
    //  
    //  
    ListVmwareVcenterFolders(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListFoldersResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterFolder Returns a representation of the specified VMware folder.
    ReadVmwareVcenterFolder(
        vcenterId string, 
        folderId string, 
        embed *string)(
        *models.ReadFolderResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterFoldersV1 returns VmwareVcenterFoldersV1Client
func NewVmwareVcenterFoldersV1(config config.Config) VmwareVcenterFoldersV1Client {
    client := new(VmwareVcenterFoldersV1)
    client.config = config
    return client
}
