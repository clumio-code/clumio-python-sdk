// Copyright (c) 2021 Clumio All Rights Reserved

package mssqlhosts

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlHostsV1Client represents a custom type interface
type MssqlHostsV1Client interface {
    // ListMssqlHostConnections Returns a list of hosts
    ListMssqlHostConnections(
        currentCount *int64, 
        filter *string, 
        limit *int64, 
        start *string)(
        *models.ListHcmHostsResponse,  *apiutils.APIError)
    
    // CreateMssqlHostConnections Create a MSSQL Connection.
    CreateMssqlHostConnections(
        body *models.CreateMssqlHostConnectionsV1Request)(
        *models.CreateHcmHostResponse,  *apiutils.APIError)
    
    // DeleteMssqlHostConnections Delete the specified MSSQL host.
    DeleteMssqlHostConnections(
        embed *string, 
        body *models.DeleteMssqlHostConnectionsV1Request)(
        *models.DeleteHcmHostResponse,  *apiutils.APIError)
    
    // MoveMssqlHostConnections Move the specified MSSQL hosts from a source Sub-Group to a destination Sub-Group.
    MoveMssqlHostConnections(
        embed *string, 
        body *models.MoveMssqlHostConnectionsV1Request)(
        *models.MoveHcmHostsResponse,  *apiutils.APIError)
    
    // CreateMssqlHostConnectionCredentials Create Edge Connector Credentials for the specified MSSQL host.
    CreateMssqlHostConnectionCredentials(
        body *models.CreateMssqlHostConnectionCredentialsV1Request)(
        *models.CreateHostECCredentialsResponse,  *apiutils.APIError)
    
    // ReadMssqlHostConnections Returns a representation of the specified host.
    ReadMssqlHostConnections(
        hostId string)(
        *models.ReadHcmHostResponse,  *apiutils.APIError)
    
    // ListMssqlHosts Returns a list of hosts
    ListMssqlHosts(
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListMssqlHostsResponse,  *apiutils.APIError)
    
    // ReadMssqlHosts Returns a representation of the specified host.
    ReadMssqlHosts(
        hostId string)(
        *models.ReadMssqlHostResponse,  *apiutils.APIError)
    
}

// NewMssqlHostsV1 returns MssqlHostsV1Client
func NewMssqlHostsV1(config config.Config) MssqlHostsV1Client {
    client := new(MssqlHostsV1)
    client.config = config
    return client
}
